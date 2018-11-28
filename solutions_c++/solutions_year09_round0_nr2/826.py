#include <iostream>

using namespace std;

const int nmax=100;
const int xmax=10000;
const int di[4]={-1,0,0,1};
const int dj[4]={0,-1,1,0};

int id[xmax],sz[xmax];
int num[nmax][nmax];
char label[xmax];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int n,m,i,j,k,ii,jj;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++) scanf("%d",&num[i][j]);
		int x=n*m;
		for(i=0;i<x;i++) id[i]=i, sz[i]=1;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				int best=num[i][j];
				int d=-1;
				for(k=0;k<4;k++)
				{
					ii=i+di[k];
					jj=j+dj[k];
					if (ii<0||jj<0||ii>=n||jj>=m) continue;
					if (num[ii][jj]<best) best=num[ii][jj], d=k;
				}
				if (best>=num[i][j]) continue;
				ii=i+di[d];
				jj=j+dj[d];
				int a=i*m+j;
				int b=ii*m+jj;
				for(a=id[a];a!=id[a];a=id[a]);
				for(b=id[b];b!=id[b];b=id[b]);
				if (sz[a]<sz[b])
				{
					id[a]=b;
					sz[b]+=sz[a];
				} else
				{
					id[b]=a;
					sz[a]+=sz[b];
				}
			}
		char cur='a';
		memset(label,0,sizeof(label));
		printf("Case #%d:\n",t);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				for(k=id[i*m+j];k!=id[k];k=id[k]);
				if (!label[k]) label[k]=cur++;
				printf("%c",label[k]);
				if (j<m-1) printf(" "); else puts("");
			}
	}


	return 0;
}