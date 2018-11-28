#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<string>
#include<map>
#include<queue>
#include<cmath>
#include<vector>
#include<bitset>
#include<sstream>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		long long k,l,p,c;
		cin>>l>>p>>c;
		k=(p-1)/l+1;
		int da=0;
		for(da=0;c<k;da++)
		{
			c*=c;
		}

		printf("Case #%d: %d\n",cas++,da);
	}

}