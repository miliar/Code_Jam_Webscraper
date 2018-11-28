#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

double V[202];
double P[202];
double VS[202];
int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int C,D;
		cin >> C >> D;
		memset(VS,0,sizeof(VS));
		for(int j=1;j<=C;j++) 
		{
			cin >> P[j] >> V[j];
			VS[j] = VS[j-1] + V[j];
		}
		double maxi = 0;
		for(int j=1;j<=C;j++)
		{
			for(int k=j;k<=C;k++)
			{
				double totalVal = VS[k]-VS[j-1];
				double initDist = P[k]-P[j];
				maxi = max(maxi, ((totalVal-1)*D-initDist)/2.0);
			}
		}
		cout << "Case #" << i << ": " << maxi << endl;
	}
}
