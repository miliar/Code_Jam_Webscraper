#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

string usedL;

struct Word {
	string str;
	vint pos[32];
	int lost;
	int org;
	
	void init() {
		lost = 0;
	}
	
	void setStr(const char *other, int i) {
		org = i;
		str = other;
		rep(k, 32) pos[k].clear();
		int size = str.size();
		rep(k, size) {
			pos[str[k] - 'a'].pb(k);
		}
		init();
	}
	bool operator < (const Word &other) const {
		if(str.size() != other.str.size()) return str.size() < other.str.size();
		rep(i, 26) {
			if(pos[usedL[i] - 'a'] != other.pos[usedL[i] - 'a']) {
				return pos[usedL[i] - 'a'] < other.pos[usedL[i] - 'a'];
			}
		}
		return true;
	}
} words[10010];

int main() {
	int T = in();
	rep(tst, T) {
		//cerr << tst << endl;
		printf("Case #%d: ", tst + 1);
		int N = in();
		int M = in();
		
		string L[110];
		
		rep(i, N) {
			char temp[256];
			gets(temp);
			words[i].setStr(temp, i);
		}
		words[N].setStr("", N);
		rep(i, M) {
			char temp[256];
			gets(temp);
			L[i] = temp;
		}
		
		rep(i, M) {
			rep(k, N) words[k].init();
			usedL = L[i];
			sort(words, words + N);
			/*
			if(tst == 2) {
				rep(k, N) {
					printf("%s, ", words[k].str.c_str());
				}
				cout << endl;
			}
			*/
			bool sal[10010];
			sal[N - 1] = false;
			rep(k, N) {
				sal[k] = words[k].str.size() == words[k + 1].str.size();
			}
			
			rep(c, 26) {
				/*
				bool empc = true;
				rep(k, N) {
					bool identified = k == 0 ? sal[k] == false : sal[k - 1] == false && sal[k] == false;
					if(! identified && ! words[k].pos[usedL[c] - 'a'].empty()) {
						empc = false;
						break;
					}
				}
				if(empc) continue;
				*/
				//cout << usedL[c] << endl;
				int from = 0;
				rep(k, N) {
					bool identified = k == 0 ? sal[k] == false : sal[k - 1] == false && sal[k] == false;
					if(identified) {
						from = k + 1;
					}
					else {
						if(! words[k].pos[usedL[c] - 'a'].empty()) {
							for(;;) {
								if(words[from].pos[usedL[c] - 'a'].empty()) words[from].lost++;
								bool old = sal[from];
								if(sal[from]) {
									if(words[from].pos[usedL[c] - 'a'] != words[from + 1].pos[usedL[c] - 'a']) {
										sal[from] = false;
									}
								}
								from++;
								if(! old) break;
							}
							k = from - 1;
						}
						else if(! sal[k]) {
							from = k + 1;
						}
					}
				}
			}
			
			int maxLost = -1;
			int ind = -1;
			rep(k, N) {
				//pr(words[k].lost);
				if(words[k].lost > maxLost || (words[k].lost == maxLost && words[k].org < words[ind].org)) {
					maxLost = words[k].lost;
					ind = k;
				}
			}
			
			printf("%s", words[ind].str.c_str(), maxLost);
			if(i != M - 1) printf(" ");
		}
		puts("");
	}
	return 0;
}
