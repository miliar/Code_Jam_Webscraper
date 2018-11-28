#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int Maxn=2010;

int a[Maxn];
int h[Maxn];
int n,m,Test;
bool Find;

int Det(int x1,int y1,int x2,int y2)
{
	return x1*y2-x2*y1;
}

inline bool Check()
{
	for (int i=1;i<n;++i)
	{
		int t=i+1;
		for (int j=i+2;j<=n;++j)
			if (Det(j-i,h[j]-h[i],t-i,h[t]-h[i])<0) t=j;
		if (t!=a[i]) return false;
	}
	return true;
}

inline void Dfs(int x)
{
	if (x>n)
	{
		if (Check())
		{
			Find=true;
			for (int i=1;i<n;++i) printf("%d ",h[i]);
			printf("%d\n",h[n]);
		}
		return;
	}
	
	for (int i=0;i<16;++i)
	{
		h[x]=i;
		Dfs(x+1);
		if (Find) return;
	}
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	scanf("%d",&Test);
	for (int ii=0;ii<Test;++ii)
	{
		printf("Case #%d: ",ii+1);
		scanf("%d",&n);
		for (int i=1;i<n;++i) scanf("%d",&a[i]);
		bool flag=true;
		for (int i=1;i<n;++i)
			for (int j=i+1;j<n;++j)
				if (a[i]>j && a[j]>a[i])
					flag=false;
		if (!flag)
		{
			printf("Impossible\n");
			continue;
		}
		
		Find=false;
		Dfs(1);
	}
	
	return 0;
}
		
		
		
		
		
		
		
					