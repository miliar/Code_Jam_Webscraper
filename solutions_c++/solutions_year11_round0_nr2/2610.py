#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

char comb[27][27], stack[102];
bool op[27][27];
int cnt[27];

int main()
{
	int ind,n,t,T,i,j;
	char s[103];
	
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1; t<=T; ++t) {
		memset(comb,-1,sizeof(comb));
		memset(op,0,sizeof(op));
		memset(cnt,0,sizeof(cnt));
		
		scanf("%d",&n);
		
		for(i=0;i<n;++i) {
			scanf("%s",s);
			comb[s[0]-'A'][s[1]-'A'] = s[2]-'A';
			comb[s[1]-'A'][s[0]-'A'] = s[2]-'A';
		}
		
		scanf("%d",&n);
		
		for(i=0;i<n;++i) {
			scanf("%s",s);
			op[s[0]-'A'][s[1]-'A'] = true;
			op[s[1]-'A'][s[0]-'A'] = true;
		}
		
		scanf("%d %s",&n,s);
		ind = 0;
		
		for(i=0; i<n; ++i) {
			s[i] = s[i] - 'A';
			
			if(ind && comb[stack[ind-1]][s[i]] != -1) {
				--cnt[stack[ind-1]];
				stack[ind-1] = comb[stack[ind-1]][s[i]];
				++cnt[stack[ind-1]];
				
				continue;
			}
			
			for(j=0; j<26; ++j)
				if(cnt[j] && op[j][s[i]]) {
					ind = 0;
					memset(cnt,0,sizeof(cnt));
					break;
				}
			
			if(j==26) {
				stack[ind++] = s[i];
				++cnt[s[i]];
			}
		}
		
		printf("Case #%d: [",t);
		
		for(i=0;i<ind;++i) {
			if(i) printf(", %c",stack[i]+'A');
			else printf("%c",stack[i]+'A');
		}
		
		printf("]\n");
	}	
}





