#include<iostream>
#include<cstdio>

using namespace std;

int z,zz,n,k;

int main()
{
	freopen("gcj_rand0_a.in","r",stdin);
	freopen("gcj_rand0_a.out","w",stdout);
	cin>>z;
	for(zz=1;zz<=z;++zz)
	{
		cin>>n>>k;
		if(k&&(k+1)%(1<<n)==0)
			printf("Case #%d: ON\n",zz);
		else
			printf("Case #%d: OFF\n",zz);
	}
	return 0;
}
