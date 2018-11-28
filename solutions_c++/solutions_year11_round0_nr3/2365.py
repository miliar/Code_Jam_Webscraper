#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
int a[1231];
int s[1300006];
int bj[13000006];
int mx[1<<21];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for(int i=0;i<(1<<20);i++)
		for(int q=0;q<21;q++)
			if(i&(1<<q))mx[i]=q+1;
	int ts;
	cin>>ts;
	for(int cas=1;cas<=ts;cas++)
	{
		int n,da=0,k,s=0;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			s+=a[i];
			da^=a[i];
		}
		if(da)
		{
			printf("Case #%d: NO\n",cas);
			continue;
		}
		sort(a,a+n);
		s-=a[0];
		
		printf("Case #%d: %d\n",cas,s);
	}
}