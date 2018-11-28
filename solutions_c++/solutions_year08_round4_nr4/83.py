#include <stdio.h>
#include <string.h>
int T,nT;
int K,slen;
char str[50000];
int be[16][16];
int ibe[16][16];
bool ab[16];
int best;
void search(int bp,int lp,int np,int nv)
{
	int i;
	if (np==K-1)
	{
		for (i=0;!ab[i];i++);
		if (nv+be[lp][i]+ibe[i][bp]>best)
			best=nv+be[lp][i]+ibe[i][bp];
	}
	else
	{
		for (i=0;i<K;i++) if (ab[i])
		{
			ab[i]=false;
			search(bp,i,np+1,nv+be[lp][i]);
			ab[i]=true;
		}
	}
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d",&K);
		scanf("%s",str);
		slen=strlen(str);
		int i,j,k;
		memset(be,0,sizeof(be));
		memset(ibe,0,sizeof(ibe));
		for (i=0;i<K;i++)
			for (j=i+1;j<K;j++)
				for (k=0;k<slen;k+=K)
					if (str[i+k]==str[j+k])
					{
						be[i][j]+=1;
						be[j][i]+=1;
					}
		for (i=0;i<K;i++)
			for (j=0;j<K;j++) if (i!=j)
				for (k=K;k<slen;k+=K)
					if (str[i+k-K]==str[j+k])
						ibe[i][j]+=1;
		memset(ab,1,sizeof(ab));
		best=0;
		for (i=0;i<K;i++)
		{
			ab[i]=false;
			search(i,i,1,0);
			ab[i]=true;
		}
		printf("Case #%d: %d\n",nT-T,slen-best);
	}
	fclose(stdin);
	fclose(stdout);
}