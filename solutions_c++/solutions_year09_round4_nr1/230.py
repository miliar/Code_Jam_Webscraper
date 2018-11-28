#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char map[50][50];
int n;

void swapline(int p,int q)
{
	int i;
	for(i=0;i<n;i++)
		swap(map[p][i],map[q][i]);
}

bool check(int l,int x)
{
	int i;
	for(i=x+1;i<n;i++)
		if(map[l][i]=='1')
			return false;
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j;
	int t,ca=1;
	int ans;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		gets(map[0]);
		for(i=0;i<n;i++)
			gets(map[i]);
		ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
				if(check(j,i))
					break;
			while(j!=i)
			{
				swapline(j,j-1);
				j--;ans++;
			}
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}