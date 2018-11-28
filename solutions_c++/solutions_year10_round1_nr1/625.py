#include <stdio.h>
#include <string.h>

#define MAX 60 

int di[]={1,0,1,1};
int dj[]={0,1,-1,1};

char tab[MAX][MAX];

int main()
{
	int i,j,k,l;
	int ni,nj;
	int n,K;
	int t, ccnt;
	char tmp;
	int v1,v2;
	scanf("%d",&t);
	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d %d",&n,&K);
		for(j=n-1;j>=0;--j)
			for(i=0;i<n;++i)
				scanf(" %c",&tab[i][j]);
		/*
		for(i=0;i<n;++i)
		{
			for(j=0;j<n;++j)
				printf("%c",tab[i][j]);
			printf("\n");
		}
		*/
		for(i=n-1;i>0;--i)
			for(j=0;j<n;++j)
			{
				for(k=i;k>=0 && tab[k][j]=='.';--k);
				if(k<0)
					continue;
				tmp=tab[k][j];
				tab[k][j]='.';
				tab[i][j]=tmp;
			}
		/*
		printf("\n\n");
		for(i=0;i<n;++i)
		{
			for(j=0;j<n;++j)
				printf("%c",tab[i][j]);
			printf("\n");
		}
		*/
		v1=v2=0;
		tmp='B';
		for(i=0;i<n;++i)
			for(j=0;j<n;++j) for(k=0;k<4;++k)
			{
				ni=i;
				nj=j;
				l=0;
				while(ni>=0 && ni<n && nj>=0 && nj<n)
				{
					if(tab[ni][nj]!=tmp)
						break;
					++l;
					if(l>=K)
						break;
					ni+=di[k];
					nj+=dj[k];
				}
				if(l>=K)
					v1=1;
			}
		tmp='R';
		for(i=0;i<n;++i)
			for(j=0;j<n;++j) for(k=0;k<4;++k)
			{
				ni=i;
				nj=j;
				l=0;
				while(ni>=0 && ni<n && nj>=0 && nj<n)
				{
					if(tab[ni][nj]!=tmp)
						break;
					++l;
					if(l>=K)
						break;
					ni+=di[k];
					nj+=dj[k];
				}
				if(l>=K)
					v2=1;
			}
		printf("Case #%d: ",ccnt);
		if(v1 && v2)
			printf("Both\n");
		else if(v1)
			printf("Blue\n");
		else if(v2)
			printf("Red\n");
		else
			printf("Neither\n");
	}
	return 0;
}

