#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;
typedef long long ll;

int main(int argc,char *argv[])
{
    freopen("MinimumScalarProduct.in", "r", stdin);
    freopen("MinimumScalarProduct.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	int n=5;
	scanf("%d",&n);
	int x[n],y[n];
	for(int k=0;k<n;k++)
	    scanf("%d",x+k);
	for(int k=0;k<n;k++)
	scanf("%d",y+k);
	
	sort(x,x+n);
	sort(y,y+n);
	int total=0;
	for(int k=0;k<n;k++)
	    total+=x[k]*y[n-k-1];

	printf("Case #%d: %d\n",curCase,total);
    }
    return 0;
}
   
