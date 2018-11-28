#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
bool opp[26][26];
int comb[26][26], L[105], li, cnt[26];
char s[10];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		memset(comb,-1,sizeof(comb));
		memset(opp,0,sizeof(opp));
		memset(cnt,0,sizeof(cnt));
		int C;
		scanf("%d",&C);
		li = 0;
		for(int i=0;i<C;++i) {
			char a,b,c;
			scanf(" %c%c%c",&a,&b,&c);
			a -= 'A'; b -= 'A'; c -= 'A';
			comb[a][b] = comb[b][a] = c;
		}
		scanf("%d",&C);
		for(int i=0;i<C;++i) {
			char a,b;
			scanf(" %c%c",&a,&b);
			a -= 'A'; b -= 'A';
			opp[a][b] = opp[b][a] = 1;
		}
		scanf("%d",&C);
		for(int i=0;i<C;++i) {
			char a;
			scanf(" %c",&a);
			a -= 'A';
			if(li && comb[L[li-1]][a] != -1) {
				--cnt[L[li-1]];
				L[li-1] = comb[L[li-1]][a];
			}
			else {
				bool cl = 0;
				for(int i=0;i<26;++i)
					if(cnt[i] && opp[a][i]) {
						memset(cnt,0,sizeof(cnt));
						li = 0;
						cl = 1;
						break;
					}
				if(!cl) {
					L[li++] = a;
					++cnt[a];
				}
			}
		}
		printf("Case #%d: [",cn);
		for(int i=0;i<li;++i) {
			if(i) printf(", ");
			printf("%c",L[i]+'A');
		}
		printf("]\n");
	}
}
