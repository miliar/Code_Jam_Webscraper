#include<iostream>
#include<cstdio>
using namespace std;
const int MAX=1100;

int R,K,N;
int a[MAX];
int tim[MAX*MAX];
int v[MAX];
int main()
{
	//freopen("F:\\C-small-attempt0.in","r",stdin);
	//freopen("F:\\C-small-attempt0.out","w",stdout);
	int i,j,T;scanf("%d",&T);
	int CN=0;
	while(T--)
	{
		memset(v,0,sizeof(v));
		scanf("%d%d%d",&R,&K,&N);
		int gs=0;
		for(i=1;i<=N;i++) 
		{
			scanf("%d",&a[i]);
			gs+=a[i];
		}
		printf("Case #%d: ",++CN);
		if(gs<=K)
		{
			printf("%d\n",gs*R);
			continue;
		}
		int beg=1,cnt=1,per=0,f=0;
		while(1)
		{
			v[1]=1;
			int total=0,yy=0;
			for(i=beg;;i++)
			{
				if(i==N+1) i=1;
				if(total+a[i]<=K) total+=a[i];
				else 
				{
					beg=i;
					tim[cnt]=total;
					if(v[beg]) {f=beg;break;}
					else v[beg]=++cnt;
					i--;
					if(i==0) i=N;
					break;
				}
			}
			
			if(f) break;
		}
		int ans=0;
		for(i=1;i<v[f]&&i<=R;i++)
		{
			ans+=tim[i];
		}
		for(i=v[f];i<=cnt;i++) per+=tim[i];
		
		if(R<v[f]) {printf("%d\n",ans);continue;}
		int cly=cnt-v[f]+1;
		R-=v[f]-1;
		ans+=(R/cly)*per;
		for(i=v[f];i<R%cly+v[f];i++)
		{
			ans+=tim[i];
		}
		printf("%d\n",ans);
	}
	//system("pause");
	return 0;
}
