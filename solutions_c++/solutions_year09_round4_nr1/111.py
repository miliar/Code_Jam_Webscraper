#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

const int maxn = 50;

int n;
char s[maxn][maxn];
int a[maxn],p[maxn];

bool cmp(const int &x, const int &y)
{
	if(a[x]!=a[y]) return a[x]<a[y];
	else return x<y;
}

int main()
{
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",&s[i]);
			a[i] = -1;
			for(int j=0;j<n;j++)
				if(s[i][j]=='1')
					a[i] = j;
		}
		int ans = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=i;j<n;j++)
				if(a[j]<=i)
				{
					for(int k=j-1;k>=i;k--)
					{
						swap(a[k],a[k+1]);
						ans++;
					}
					break;
				}
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}

