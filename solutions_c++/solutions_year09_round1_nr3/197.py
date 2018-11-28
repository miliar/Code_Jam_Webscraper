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
//typedef long long LL;
typedef __int64 LL;

LL ncr[42][42];

void NCR()
{
	int i,j;
	for(i=0;i<=40;i++) ncr[i][0]=1;
	for(i=1;i<=40;i++) for(j=1;j<=i;j++) ncr[i][j]=ncr[i-1][j]+ncr[i-1][j-1];
}

int n,c,seen[50];
double memo[50];

double solve(int k)
{
	int i;
	double ret=0.0;

	if(seen[k])
		return memo[k];

	for(i=1;i<=n;i++)
	{
		if(k+i>=c) break;
		double p=(double)(ncr[c-k][i]*ncr[k][n-i])/(double)ncr[c][n];
		//printf("%d %lf\n",i,p);
		ret+=p*solve(k+i);
	}
	ret+=1.0;
	ret*=(double)ncr[c][n]/(double)(ncr[c][n]-ncr[k][n]);
	seen[k]=1;

	return memo[k]=ret;
}

int main()
{
	int i,j,k,tests,cs=0;
	
//	freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("D:\\gcj\\A-large.out","w",stdout);


	NCR();
	scanf("%d",&tests);
	while(tests--)
	{
		double ans;

		MEM(seen,0);

		scanf("%d%d",&c,&n);

		if(n>=c)
			ans=1.0;
		else
			ans=1.0+solve(n);


		printf("Case #%d: %.8lf\n",++cs,ans);
	}

	return 0;
} 


