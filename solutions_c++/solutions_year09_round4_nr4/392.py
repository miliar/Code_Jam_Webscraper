#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <iostream>

using namespace std;

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		int n;
		double data[3][3];
		cin>>n;
		for(int i=0;i<n;i++) cin>>data[i][0]>>data[i][1]>>data[i][2];

		double ans;
		if(n<=2)
		{
			ans=0;
			for(int i=0;i<n;i++) ans=max(ans, data[i][2]);
		}
		else
		{
			double tAns;
			tAns=sqrt((data[0][0]-data[1][0])*(data[0][0]-data[1][0]) + (data[0][1]-data[1][1])*(data[0][1]-data[1][1]));
			tAns+=data[0][2]+data[1][2];

			ans=max(tAns/2, data[2][2]);

			tAns=sqrt((data[0][0]-data[2][0])*(data[0][0]-data[2][0]) + (data[0][1]-data[2][1])*(data[0][1]-data[2][1]));
			tAns+=data[0][2]+data[2][2];

			ans=min(ans, max(tAns/2, data[1][2]));

			tAns=sqrt((data[1][0]-data[2][0])*(data[1][0]-data[2][0]) + (data[1][1]-data[2][1])*(data[1][1]-data[2][1]));
			tAns+=data[1][2]+data[2][2];

			ans=min(ans, max(tAns/2, data[0][2]));
		}

		printf("Case #%d: %lf\n", caseN, ans);
	}

	return 0;
}
