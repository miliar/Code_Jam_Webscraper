#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-large.in.txt","r",stdin);
	freopen("outputtttbig.txt","w",stdout);
    
    int T;
    cin>>T;
    int kas=1;
    while (T--)
    {
		int N;
		cin>>N;
		
		vector<string> v(N);
		for (int i=0; i<N; i++)
			cin>>v[i];
		
		vector<int> wins(N);
		vector<int> loss(N);
		
		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				if (v[i][j] == '1')
					wins[i]++;
				else if (v[i][j] == '0')
					loss[i]++;
			}
		}
		//for (int i=0; i<N; i++) cout<<"wins "<<i<<" "<<wins[i]<<endl;
		//for (int i=0; i<N; i++) cout<<"loss "<<i<<" "<<loss[i]<<endl;
		vector<double> owp(N);
		
		for (int i=0; i<N; i++)
		{
			double sum = 0.0;
			int count = 0;
			for (int j=0; j<N; j++)
			{
				if (v[i][j] != '.')
				{
					if (v[j][i] == '1')
					{
						if (wins[j]+loss[j]-1!=0)
						sum = sum + (wins[j]-1) / ((wins[j]+loss[j]-1)*1.0);
					}
					else
					{
						if (wins[j]+loss[j]-1!=0)
						sum = sum + (wins[j]*1.0) / ((wins[j]+loss[j])-1);
					}
					count += 1;
				}
			}
			owp[i] = sum/count;
		}
		
		//for (int i=0; i<N; i++) cout<<"OWP "<<i<<" "<<owp[i]<<endl;
		
		vector<double> result(N);
		cout<<"Case #"<<(kas)<<":"<<endl;
		kas++;
		for (int i=0; i<N; i++)
		{
			result[i] += (0.25*((wins[i]*1.0)/(wins[i]+loss[i])));
			result[i] += (0.50*owp[i]);
			
			double owp_oth = 0.0;
			int count = 0;
			for (int j=0; j<N; j++)
			{
				if (v[i][j] != '.')
				{
					owp_oth += owp[j];
					count +=1;
				}
			}
			if (count !=0)
				result[i] += (0.25*(owp_oth/count));
			printf("%.9f\n", result[i]);
		}
	}
	
	return 0;
}
