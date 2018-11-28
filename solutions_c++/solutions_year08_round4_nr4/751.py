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
    freopen("permrle.in", "r", stdin);
    freopen("permrle.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	int n;
	char s[1001];
	scanf("%d %s",&n,s);
	int p[n];
	for(int k=0;k<n;k++)
	    p[k]=k;
	int minCount=1<<30;
	do
	{
	    char prev=0;
	    int count=0;
	    for(int k=0;s[k]>=97;k++)
	    {
		char ch=s[p[k%n]+k-k%n];
		//printf("%c",ch);
		if(ch!=prev)
		    ++count,prev=ch;
	    }
	    minCount=min(minCount,count);
	    //printf("\n");
		
	} while(next_permutation(p,p+n));
	printf("Case #%d: %d\n",curCase,minCount);
    }
    return 0;
}
