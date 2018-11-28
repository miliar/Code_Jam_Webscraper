#include <stdio.h>
#include <iostream>
using namespace std;

int C,D,N;

char cf[40][4];
char df[40][4];
char str[110];
int flag[30];
char result[110];
int rn=1;

int main()
{
	int cas,T;
	freopen("B-large.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		int i,j;
		scanf("%d",&C);
		for(i=1;i<=C;++i)
			scanf("%s",cf[i]);
		scanf("%d",&D);
		for(i=1;i<=D;++i)
			scanf("%s",df[i]);
		scanf("%d",&N);
		scanf("%s",str);
		printf("Case #%d: [",cas);
		bool IsFirst=false;
		memset(flag,0,sizeof(flag));
		result[0]=str[0];
		rn=1;
		flag[str[0]-'A']++;
		for(i=1;i<N;++i)
		{
			for(j=1;j<=C;++j)
			{
				if((str[i]==cf[j][0]&&result[rn-1]==cf[j][1]) || (str[i]==cf[j][1]&&result[rn-1]==cf[j][0]) )
				{	
					result[rn-1]=cf[j][2];
					flag[str[i-1]-'A']--;
					break;
				}
			}
			if(j<=C) continue;
			for(j=1;j<=D;++j)
			{
				if( (str[i]==df[j][0]&&flag[df[j][1]-'A']) || (str[i]==df[j][1]&&flag[df[j][0]-'A']))
				{
					break;
				}
			}
			if(j<=D)
			{
				memset(flag,0,sizeof(flag));
				rn=0;
				continue;
			}
			flag[str[i]-'A']++;
			result[rn++]=str[i];
		}
		if(rn) printf("%c",result[0]);
		for(i=1;i<rn;++i) printf(", %c",result[i]);
		printf("]\n");
	}


	return 0;
}

