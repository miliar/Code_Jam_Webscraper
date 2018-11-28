#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define rep(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define sz(a) ((int)(a).size())
#define ALL(a) (a).begin(),(a).end()

const int maxn=40;

int n,test,t,i,j,k,ans;
int a[maxn][maxn],rightmost[maxn];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&test);
	forr(t,1,test)
	{
		scanf("%d",&n);
		getchar();
		rep(i,n)
		{
			rep(j,n)
				a[i][j]=getchar()-'0';
			getchar();
		}
		rep(i,n)
		{
			j=n-1;
			while(j>=0 && a[i][j]==0) j--;
			rightmost[i]=j;
		}
		ans=0;
		rep(i,n)
		{
			j=i;
			while(rightmost[j]>i) j++;
			ans+=(j-i);
			ford(k,j,i+1)
			{
				rep(l,n)
					swap(a[k][l],a[k-1][l]);
				swap(rightmost[k],rightmost[k-1]);
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
