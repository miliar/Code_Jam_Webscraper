#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;
typedef long long ll;

const int maxCards=1000000;
int c[maxCards+1];

int main(int argc,char *argv[])
{
    freopen("Mousetrap.in", "r", stdin);
    freopen("Mousetrap.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	int nc,n;
	scanf("%d%d",&nc,&n);
	int i=0;
	memset(c,0,sizeof(c));
	for(int k=1;k<=nc;k++)
	{
	    for(int j=0;j<k;j++)
		do
		    if(++i>nc)
			i=1;
		while(c[i]>0);
	    //printf("%d %d\n",k,i);
	    c[i]=k;
	}

	printf("Case #%d:",curCase);
	if(n==0)
	    printf(" ");
	else
	    for(int k=0;k<n;k++)
	    {
		scanf("%d",&i);
		printf(" %d",c[i]);
	    }
	printf("\n");
    }
    return 0;
}
   
