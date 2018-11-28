#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
using namespace std;
int main()
{
	char com[5];
	int opp[30][30];
	int mapp[30][30];
	char temp[5];
	char str[150];
	int t,i,c,d,n,j,k;
	int in[50];
	char que[200];
	int l;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&t);
	for (i = 1;i <= t;i++){
		l = -1;
		memset(mapp,0,sizeof(mapp));
		scanf("%d",&c);
		for (j = 0;j < c;j++){
			scanf("%s",com);
			int a = com[0]-'A'+1;
			int b = com[1]-'A'+1;
			int c = com[2]-'A'+1;
			mapp[a][b] = c;
			mapp[b][a] = c;
		}
		scanf("%d",&d);
		memset(opp,0,sizeof(opp));
		for (j = 0;j < d;j++){
			scanf("%s",temp);
			int num = temp[0]-'A'+1;
			opp[num][++opp[num][0]] = temp[1]-'A'+1;
			num = temp[1]-'A'+1;
			opp[num][++opp[num][0]] = temp[0]-'A'+1;
		}
		memset(in,0,sizeof(in));
		scanf("%d",&n);
		scanf("%s",str);
		int len = strlen(str);
		for (j = 0;j < len;j++){
			int a = str[j]-'A'+1;
			if (l == -1){
				in[a]++;
				que[++l] = str[j];
				continue;
			}
			int b = que[l]-'A'+1;
			in[a]++;
			que[++l] = str[j];
			if (mapp[a][b]!= 0){
				in[a]--;
				in[b]--;
				l--;
				que[l] = (char)('A'+mapp[a][b]-1);
			}
			else{
				for (k = 1;k <= opp[a][0];k++){
					if (in[opp[a][k]] > 0){
						memset(in,0,sizeof(in));
						l = -1;
					}
					break;
				}
			}
		}
		printf("Case #%d: [",i);
		if (l == -1){
			printf("]\n");
			continue;
		}            
		for (j = 0;j < l;j++){
			printf("%c, ",que[j]);
		}
		printf("%c]\n",que[l]);
	}
	return 0;
}

