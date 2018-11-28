#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
int dig[10000010],rev[15];
int sure(int x,int n,int m)
{
    int c=0;
    int y = x;
	map<int,int> ma;
	ma.clear();
	ma[x] = 1;
    for(int i = 1; i < dig[y];i++) {
	    int p = x / rev[dig[y]];
	    int q = (x%rev[dig[y]]) * 10 + p;
	    if(dig[q] == dig[y] && q >=n && q <= m && !ma[q]) c++,ma[q] = 1;
		x = q;
    }
	return c;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	rev[1] = 1;
	rev[2] = 10;
	rev[3] = 100;
	rev[4] = 1000;
	rev[5] = 10000;
	rev[6] = 100000;
	rev[7] = 1000000;
	memset(dig,0,sizeof(dig));
	for(int i=1;i<10000000;i++) {
		if(i<10) dig[i] = 1;
		else if(i<100) dig[i] = 2;
		else if(i < 1000) dig[i] = 3;
		else if(i<10000) dig[i]=4;
		else if(i<100000) dig[i]=5;
		else if(i<1000000) dig[i]=6;
		else dig[i]=7;
	}
	sure(23,10,40);
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++) {
		int ans = 0;
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i = max(10,n); i <= m; i ++) {
			ans+=sure(i,n,m);
		//	if(i>=100000) printf("%d\n",i);
		}
		printf("Case #%d: %d\n",k,ans/2);
	}
	return 0;
}

