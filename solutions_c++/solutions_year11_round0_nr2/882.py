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

int main() {
	int T = in();
	rep(tst, T) {
		char hoge[40][40];
		bool opp[40][40];
		rep(i, 40) rep(k, 40) hoge[i][k] = opp[i][k] = 0;
		
		int C = in();
		rep(i, C) {
			char from1, from2, to;
			scanf("%c%c%c ", &from1, &from2, &to);
			hoge[from1 - 'A'][from2 - 'A'] = hoge[from2 - 'A'][from1 - 'A'] = to;
		}
		int D = in();
		rep(i, D) {
			char a, b;
			scanf("%c%c ", &a, &b);
			opp[a - 'A'][b - 'A'] = opp[b - 'A'][a - 'A'] = true;
		}
		
		int N = in();
		vector<char> data;
		rep(i, N) {
			char c;
			/*
			rep(k, data.size()) {
				printf("%c", data[k]);
				printf(k == data.size() - 1 ? "\n" : ", ");
			}
			*/
			scanf("%c ", &c);
			if(data.empty()) {
				data.pb(c);
			}
			else {
				char tail = data[data.size() - 1];
				int a = c - 'A';
				int b = tail - 'A';
				
				if(hoge[a][b] != 0) {
					data.pop_back();
					data.pb(hoge[a][b]);
					goto HOGE;
				}
				else {
					// opposed?
					int size = data.size();
					rep(k, size) {
						if(opp[data[k] - 'A'][a]) {
							data.clear();
							goto HOGE;
						}
					}
				}
				data.pb(c);
			}
			HOGE:;
		}
		
		printf("Case #%d: [", tst + 1);
		int size = data.size();
		rep(k, size) {
			printf("%c", data[k]);
			printf(k == size - 1 ? "" : ", ");
		}
		printf("]\n");
	}
	return 0;
}
