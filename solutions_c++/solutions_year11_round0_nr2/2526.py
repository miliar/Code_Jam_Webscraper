#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int com[50][50];
bool opp[50][50];
int q[1000];

int main()
{
	int i, j, k, T;
	int cntCom, cntOpp;
	char tmp[1000];
	int n;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d",&T);
	for(int ca = 1; ca <= T; ca++)
	{
		memset(com, -1, sizeof(com));
		for(scanf("%d", &cntCom); cntCom; cntCom--)
		{
			scanf("%s",tmp);
			com[tmp[0]-'A'][tmp[1]-'A'] = com[tmp[1]-'A'][tmp[0]-'A'] = tmp[2]-'A';
		}
		memset(opp, false, sizeof(opp));
		for(scanf("%d", &cntOpp); cntOpp; cntOpp--)
		{
			scanf("%s",tmp);
			opp[tmp[0]-'A'][tmp[1]-'A'] = opp[tmp[1]-'A'][tmp[0]-'A'] = true;
		}
		scanf("%d",&n);
		scanf("%s",tmp);
		for(i=0,k=0;i<n;i++)
		{
			if(k>0)
			{
				if(com[q[k]][tmp[i]-'A'] != -1)
					q[k] = com[q[k]][tmp[i]-'A'];
				else{
					for(j=1;j<=k;j++){
						if(opp[q[j]][tmp[i]-'A']){
							j = -1;
							k = 0;
							break;
						}
					}
					if(j>k) q[++k] = tmp[i]-'A';
					
				}
			}
			else q[++k] = tmp[i] - 'A';
		}
		printf("Case #%d: [",ca);
		for(i = 1; i < k; i++)
			printf("%c, ",q[i]+'A');
		if(k!=0)
			printf("%c",q[k]+'A');
		printf("]\n");
	}
	return 0;
}
			
			
			
		
