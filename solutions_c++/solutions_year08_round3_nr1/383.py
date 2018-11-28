#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
using namespace std;
int total[1010];
int dp[1010];
int main()
{
	int i,j,t;
	int p,k,l,ka;
	long long ret= 0;
	
	cin >>t;

	for(ka=1;ka<=t;ka++){
		cin >> p >> k >> l;
		for(i=0;i<l;i++)
			cin >> dp[i];
		sort(dp,dp+l);
		reverse(dp,dp+l);
		memset(total,0,sizeof total);

		int r = l / k;
		int kz = 0;
		int zz = 0;

		for(i=0;i<l;i++){
			if(kz % k == 0)
				kz = 0,zz++;
			total[i] = zz;

			kz++;
		}

		int flag=0;
		ret = 0;
		for(i=0;i<l;i++)
			if(total[i] > p)
				flag=1;
		for(i=0;i<l;i++)
			ret += total[i] * dp[i];

		if(flag)
				cout <<"Case #"<<ka<<": impossible"<<endl;
		else cout <<"Case #"<<ka<<": "<< ret<<endl;
	}
}
