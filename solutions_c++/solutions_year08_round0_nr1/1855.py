#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

const int MAXQ = 1100;
const int MAXS = 110;
const int INF = 1000000000;

int n, s, q, ncas = 0;
string eng;
map<string, int> engid;
int res[MAXQ][MAXS];

int main(){
	scanf("%d", &n);
	while (n--){
		scanf("%d", &s);
		getline(cin, eng);
		engid.clear();
		for (int i = 0; i < s; ++i){
			getline(cin, eng);
			engid[eng] = i;
			res[0][i] = 0;
		}
		scanf("%d", &q);
		getline(cin, eng);
		for (int i = 0; i < q; ++i){
			getline(cin, eng);
			int qid = engid[eng];
			for (int j = 0; j < s; ++j){
				if (j == qid)
					res[i][j] = INF;
				else if (i == 0)
					res[i][j] = 0;
				else
					res[i][j] = min(res[i-1][j], *min_element(&res[i-1][0], &res[i-1][0]+s) + 1);
			}
		}
		if (q > 0)
			printf("Case #%d: %d\n", ++ncas, *min_element(&res[q-1][0], &res[q-1][0]+s));
		else
			printf("Case #%d: 0\n", ++ncas);
	}
	return 0;
}
