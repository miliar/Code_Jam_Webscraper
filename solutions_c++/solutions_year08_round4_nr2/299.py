#include <cstdio>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T,i,n,m,s,x1,y1,x2,y2;
	bool f;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d%d",&n,&m,&s);
		f=false;
		for(int x1=0;x1<=n&&!f;x1++)
			for(int x2=0;x2<=n&&!f;x2++)
				for(int y1=0;y1<=m&&!f;y1++)
					for(int y2=0;y2<=m&&!f;y2++)
						if (x1*y2-x2*y1==s || x1*y2-x2*y1==-s) 
						{
							printf("Case #%d: %d %d %d %d %d %d\n",t,0,0,x1,y1,x2,y2);
							f=true;
						}
		if (!f) printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}