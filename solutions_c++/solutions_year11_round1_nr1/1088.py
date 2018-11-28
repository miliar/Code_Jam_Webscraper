#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,n,p,g;
    bool f=false;
	scanf("%lld",&t);
	for(int j=1; j<=t; j++){
	f=false;
	scanf("%lld %lld %lld",&n,&p,&g);
	for (long long i=1; i<=n; i++)
		if(i*p%100==0) {f=true;  break;}
	if (f==false) {printf("Case #%d: Broken\n",j); continue;}
	else
		if (g==0&&p>0) {printf("Case #%d: Broken\n",j); continue;}
		else
			if (g==100&&p<100) {printf("Case #%d: Broken\n",j); continue;}
			else
				printf("Case #%d: Possible\n",j);
	}
    return 0;
}
