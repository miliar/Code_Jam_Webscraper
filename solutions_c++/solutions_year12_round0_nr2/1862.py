#include <stdio.h>
#include <algorithm>
using namespace std;

const int N=110;
int c[31][2];
int TC,tc;
int n,s,p,a[N],y;
bool b[N];

int main()
{
	int i,u,v,w;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	for(u=0;u<=30;++u)
		c[u][0]=c[u][1]=-1;
	for(u=0;u<=10;++u)
		for(v=u;v<=10&&v<=u+2;++v)
			for(w=v;w<=10&&w<=u+2;++w)
				if(w>c[u+v+w][w!=u+2])
					c[u+v+w][w!=u+2]=w;
	for(scanf("%d",&TC),tc=1;tc<=TC;++tc)
	{
		if(tc==22)
			tc=tc;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;++i)
			scanf("%d",&a[i]),b[i]=0;
		y=0;
		for(i=0;i<n && s;++i)
			if(c[a[i]][0]>=p && c[a[i]][1]<p)
				b[i]=1,--s,++y;
		for(i=0;i<n;++i)
			if(c[a[i]][1]>=p)
				b[i]=1,++y;
		printf("Case #%d: %d\n",tc,y);
	}
	return 0;
}