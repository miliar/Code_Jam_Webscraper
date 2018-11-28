#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
#define M 100003

//typedef long long LL;
typedef __int64 LL;

LL dp[502][502],ncr[502][502];


int main()
{
	int i,j,k,l,tests,cs=0,n;
	
	for(i=0;i<=500;i++) 
		ncr[i][0]=1;

	for(i=1;i<=500;i++) 
		for(j=1;j<=i;j++) ncr[i][j]=(ncr[i-1][j]+ncr[i-1][j-1])%M;

	for(i=2;i<=500;i++)
	{
		dp[i][1]=1;
		for(l=2;l<i;l++)
			for(j=1;j<l;j++)
			{
				int x=i-l-1,y=l-j-1;
				if(x<y) continue;

				LL v=(dp[l][j]*ncr[x][y])%M;
				dp[i][l]=(dp[i][l]+v)%M;
			}
	}
	//freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d",&n);
		int ans=0;
		for(i=1;i<n;i++)
			ans=(ans+dp[n][i])%M;
		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


