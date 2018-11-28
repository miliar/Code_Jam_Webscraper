#include <cstdio>
#include <cstring>
int i,j,k,s,t,n,m;

int a[1500],cut[1500],vi[1500],gain[1500];
int T,I;
int ans,at;
bool f;
int r,c,tmp,tot;
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		printf("Case #%d: ",I);
		scanf("%d%d%d",&r,&c,&n);
		s=0;
		for (i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			s+=a[i];
		}
		if (s<=c) printf("%d\n",s*r);
		else
		{
			ans=0;
			at=0;
			f=0;
			memset(vi,0,sizeof vi);
			while (r>0)
			{
				tmp=c;
				for (;a[at]<=tmp;)
				{
					tmp-=a[at];
					++at;
					if (at==n) at=0;
				}
				cut[++tot]=at;
				gain[tot]=c-tmp;
				--r;
				ans+=gain[tot];
				if (vi[at]==0)
					vi[at]=tot;
				else if (!f)
				{
					f=1;
					tmp=0;
					for (i=tot;i>vi[at];--i)
						tmp+=gain[i];
					ans+=tmp*(r/(tot-vi[at]));
					r%=(tot-vi[at]);
				}
			}
			printf("%d\n",ans);
		}
	}
	return 0;
}
					
				
