#include <iostream>
using namespace std;

int i,j,k,m,n,g,r,t,x,p,q,z;
__int64 ans;
int a[1001];
bool b[1001];
int d[1001];
int e[1001];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	scanf("%d",&t);
	for (x=1; x<=t; x++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for (j=1; j<=n; j++)
			scanf("%d",&a[j]);
		memset(e,0,sizeof(e));
		memset(b,false,sizeof(b));
		p=1; q=0; ans=0;
		while (1)
		{
			if (b[p]) break;
			b[p]=true;
			q++;
			d[q]=p;
			while (1)
			{
				if (e[q]+a[p]>k) break;
				e[q]+=a[p];
				p++;
				if (p>n) p=1;
				if (p==d[q]) break;
			}
		}
		
		
		for (j=1; j<=n; j++)
			if (p==d[j])
			{
				for (z=1; z<=min(r,j-1); z++)
					ans+=e[z];
				if (r<=j-1) break;
				r-=j-1;
				//j~q
				__int64 tmp=0;
				for (z=j; z<=q; z++)
					tmp+=e[z];
				ans+=r/(q-j+1)*tmp;
				r-=r/(q-j+1)*(q-j+1);
				for (z=j; z<j+r; z++)
					ans+=e[z];
				break;
			}
		printf("Case #%d: %I64d\n",x,ans);
	}

//	system("pause");
	return 0;
}
