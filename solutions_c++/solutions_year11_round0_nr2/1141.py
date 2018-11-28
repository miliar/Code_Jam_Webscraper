#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <algorithm>
#include <cctype>
#include <functional>
using namespace std;

typedef pair<int, int> PII;

int str[32][32], oppo[32];

int main()
{
	// freopen("G:\\B-small-attempt0.in", "r", stdin);
	// freopen("G:\\B.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		memset(str, -1, sizeof(str));
		memset(oppo, -1, sizeof(oppo));
		int n, m, p;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			char ss[4]; scanf("%s", ss);
			int a = ss[0] - 'A', b = ss[1] - 'A', c = ss[2] - 'A';
			str[a][b] = str[b][a] = c;
		}
		scanf("%d", &m);
		for(int i = 0; i < m; i++) {
			char ss[4]; scanf("%s", ss);
			int a = ss[0] - 'A', b = ss[1] - 'A';
			oppo[a] = b;
			oppo[b] = a;
		}
		scanf("%d", &p);
		vector<int> S;
		for(int i = 0; i < p; i++) {
			char c; scanf("\n%c", &c);
			c -= 'A';
			if(S.size() != 0 && str[S.back()][c] != -1) {
				int a = S.back();
				S.pop_back();
				S.push_back(str[a][c]);
			} else  {
				S.push_back(c);
				for(int j = 0; j < S.size()-1; j++) if(oppo[c] == S[j]) 
					{ S.clear(); break; }
			}
		}
		printf("Case #%d: [", t+1);
		for(int i = 0; i < S.size(); i++) 
			printf("%c%s", S[i] + 'A', i == S.size()-1 ? "]\n" : ", ");
		if(S.size() == 0) printf("]\n");
	}
	
	return 0;
}
