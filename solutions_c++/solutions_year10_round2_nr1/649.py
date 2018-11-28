#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef long long ULL;

const ULL mod = 1000000000000037;
const ULL let = 61;

ULL hashm(string s){
	int len = s.length();
	ULL res = 0;
	for (int i = 0; i < len; i++){
		if (s[i] >= '0' && s[i] <= '9')
			res = res * 61 + s[i] - '0';
		else
			res = res * let + s[i] - 'a' + 10;
		res %= mod;
	}
	return res;
}

void solution(int tstNum){
	int n, m;
	scanf("%d%d", &n, &m);
	map<ULL, set<ULL> > nodes;

	for (int i = 0; i < n; i++){
		string tmp;
		cin >> tmp;
		int len = tmp.length();
		string w;
		ULL par = -1;
		for (int i = 1; i < len; i++){
			if (tmp[i] == '/'){
				ULL h = hashm(w);
				nodes[par].insert(h);
				par = h;
				//w = "";
			}else{
				w += tmp[i];
			}
		}
		if (w.length() > 0){
			ULL h = hashm(w);
			nodes[par].insert(h);
		}
	}
	
	int res = 0;
	for (int i = 0; i < m; i++){
		string tmp;
		cin >> tmp;
		int len = tmp.length();
		string w;
		ULL par = -1;
		for (int i = 1; i < len; i++){
			if (tmp[i] == '/'){
				ULL h = hashm(w);
				if (nodes[par].find(h) == nodes[par].end()){
					nodes[par].insert(h);
					++res;
				}
				par = h;
				//w = "";
			}else{
				w += tmp[i];
			}
		}
		if (w.length() > 0){
			ULL h = hashm(w);
			if (nodes[par].find(h) == nodes[par].end()){
				nodes[par].insert(h);
				++res;
			}
		}
	}
	printf("Case #%d: %d\n", tstNum + 1, res);
}

int main(){

	freopen("A-small.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}