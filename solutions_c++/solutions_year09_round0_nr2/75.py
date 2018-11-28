#include <stdio.h>

#define MAX 110

int di[]={-1,0,0,1},dj[]={0,-1,1,0};
int n,m;
int h[MAX][MAX];
int c[MAX][MAX];
int cnt;

int processa(int i, int j)
{
	int k;
	int kmin=-1, hkmin=h[i][j];
	int ni,nj;
	if(c[i][j]>=0)
		return c[i][j];
	for(k=0;k<4;++k)
	{
		ni=i+di[k];
		nj=j+dj[k];
		if(ni>=0 && ni<n && nj>=0 && nj<m)
		{
			if(h[ni][nj]<hkmin)
			{
				kmin=k;
				hkmin=h[ni][nj];
			}
		}
	}
	if(kmin<0)
		return c[i][j]=cnt++;
	return c[i][j]=processa(i+di[kmin],j+dj[kmin]);
}

int main()
{
	int t;
	int i,j,k;
	int ccnt;
	scanf("%d",&t);
	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
			{
				scanf("%d",&h[i][j]);
				c[i][j]=-1;
			}
		cnt=0;
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				processa(i,j);
		printf("Case #%d:\n",ccnt);
		for(i=0;i<n;++i)
		{
			for(j=0;j<m;++j)
			{
				if(j>0)
					printf(" ");
				printf("%c",c[i][j]+'a');
			}
			printf("\n");
		}
	}
	return 0;
}

