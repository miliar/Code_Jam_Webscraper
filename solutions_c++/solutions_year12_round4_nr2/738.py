#include<stdio.h>
#include<algorithm>
using namespace std;

int xs[10001],ys[10001],rs[10001];

int main()
{
	int t,bk,n,i,j,k,l;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(bk=1;bk<=t;++bk)
	{
		int ww,ll;
		scanf("%d%d%d",&n,&ww,&ll);
		printf("Case #%d: ",bk);
		for(i=1;i<=n;++i)
		{
			int r;
			scanf("%d",&r);
			r*=2;
			rs[i]=r;
			xs[0]=-r/2;
			ys[0]=-r/2;
			for(j=0;j<i;++j)
			{
				int nx=xs[j]+rs[j];
				if(nx+r/2<0||nx+r/2>ww)
					continue;
				for(k=0;k<i;++k)
				{
					int ny=ys[k]+rs[k];
					if(ny+r/2<0||ny+r/2>ll)
						continue;
					for(l=1;l<i;++l)
						if(max(nx,xs[l])<min(nx+r,xs[l]+rs[l])&&max(ny,ys[l])<min(ny+r,ys[l]+rs[l]))
						 	break;
					if(l>=i)
						break;
				}
				if(k<i)
					break;
			}
			xs[i]=xs[j]+rs[j];
			ys[i]=ys[k]+rs[k];
			printf("%d %d ",xs[i]+r/2,ys[i]+r/2);
		}
		printf("\n");
	}
	return 0;
}
