#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

int main()
{
    freopen("in1","r",stdin);
    freopen("out1","w",stdout);
    int cas=1,n,t,k,i,pow[30];
    pow[0]=1;
    for (i=1; i<20; i++) pow[i]=pow[i-1]*2;
	scanf("%d",&t);
	while (t--)
    {
        scanf("%d%d",&n,&k);
        k++;
        if (!(k%pow[n])) printf("Case #%d: ON\n",cas++);
        else printf("Case #%d: OFF\n",cas++);
    }

	return 0;
}
