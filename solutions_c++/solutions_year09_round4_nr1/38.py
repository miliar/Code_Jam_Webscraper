#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn = 50;

int p[maxn];
int a[maxn];
char s[maxn];
bool vis[maxn];
int id[maxn];
int n;
bool cmp( int a,int b )
{
	return p[a] > p[b];
}
int main()
{
	int T,ans;
	scanf("%d",&T);
	bool flag;
	int tr;
	for(int num=1;num<=T;num++)
	{
		scanf("%d",&n);gets(s);
		for(int i=1;i<=n;i++)
		{
			gets(s+1);
			p[i] = n;while( p[i]>1 && s[p[i]]!='1' ) p[i]--;
		}
		for(int i=1;i<=n;i++) vis[i] = true;

		for(int i=1;i<=n;i++)
		for(int j=p[i];j<=n;j++) if(vis[j])
		{
			vis[j] = false;
			flag = true;
			for(int k=i+1;k<=n;k++) id[k-i] = k;
			sort( id+1,id+n-i+1,cmp );

			tr = 1;
			for(int k=n;k;k--) if(vis[k])
			{
				if( k<p[id[tr]] )
				{
					flag = false;break;
				}
				tr++;
			}

			if(flag)
			{
				a[i] = j;
				break;
			}else vis[j] = true;
		}

		ans = 0;
		for(int i=1;i<=n;i++)
		for(int j=i+1;j<=n;j++) if(a[i]>a[j]) ans++;
		printf("Case #%d: %d\n",num,ans);
	}
	return 0;
}
