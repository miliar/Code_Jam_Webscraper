#include <stdio.h>

#define MAX 310

char comb[MAX][MAX];
int forb[MAX][MAX];

int main()
{
	int t, ccnt;
	int i,j;

	int n;

	char t1,t2,t3;

	char v[MAX];

	scanf("%d",&t);
	for(ccnt=1;ccnt<=t;++ccnt)
	{
		int nv=0;
		for(i='A';i<='Z';++i) for(j='A';j<='Z';++j)
			comb[i][j]=forb[i][j]=0;

		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf(" %c %c %c",&t1,&t2,&t3);
			comb[t1][t2]=comb[t2][t1]=t3;
		}

		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf(" %c %c",&t1,&t2);
			forb[t1][t2]=forb[t2][t1]=1;
		}

		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf(" %c",&t1);
			v[nv++]=t1;
			int chg=1;
			while(chg)
			{
				chg=0;
				if(nv<2)
					continue;
				if(comb[v[nv-1]][v[nv-2]])
				{
					v[nv-2]=comb[v[nv-1]][v[nv-2]];
					--nv;
					chg=1;
				}
			}
			for(j=0;j<nv-1;++j)
				if(forb[v[j]][v[nv-1]])
					nv=0;
		}
		printf("Case #%d: ",ccnt);
		printf("[");
		for(i=0;i<nv;++i)
		{
			if(i>0)
				printf(", ");
			printf("%c",v[i]);
		}
		printf("]\n");

	}
	return 0;
}

		







		
