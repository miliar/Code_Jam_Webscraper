#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cmath>
#include <string>

using namespace std;

int main()
{

	int ctr = 0 ;
	int N;
	cin>>N;
	while(N--)
	{
		ctr++;
		int M,Q;
		cin>>M>>Q;
		double p[Q][4];
		for(int i=0;i<Q;i++)
		for(int j=0;j<4;j++)
		cin>>p[i][j];
		
		vector<double> pro;
		for(int i=0;i<(1<<(2*Q));i++)
		{
			double ret = 1.;
			for(int j=0;j<Q;j++)
			{
				int idx = ((i>>(2*j))&3);
				ret*=p[j][idx];
			}
			//cout<<"Adding "<<ret<<"\n";
			pro.push_back(ret);
		}		
		sort(pro.begin(),pro.end());
		double ans = 0;
		for(int i=pro.size()-1;i>=0 && (int)pro.size()-i<=M;i--)
			ans+=pro[i];
		cout<<"Case #"<<ctr<<": "<<ans<<"\n";
	}
	return 0;
}

