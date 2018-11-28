#include <iostream>

using namespace std;

int main()
{
	std::cout.precision(12);
	int T, cs = 1;
	cin>>T;

	while(T--)
	{
		int N;
		char stats[100][100];
		double WP[100], OWP[100], OOWP[100];
		double RPI[100];
		int played[100] = {0}, won[100] = {0}, lost[100] = {0};
		cin>>N;
		for(int i = 0; i < N; i ++)
		{
			cin>>stats[i];			
		}
		
		for(int i = 0; i < N; i ++)
		{
			for(int j = 0; j < N; j ++)
			{
				if(stats[i][j] != '.')
					played[i]++;
				
				if(stats[i][j] == '1')
					won[i]++;
				else
					lost[i]++;
			}
			WP[i] = (double) won[i] / played[i];
//			cout<<WP[i]<<endl;
		}

	
		for(int i = 0; i < N; i ++)
		{
			int num = 0;
			double tOWP[100] = {0}, count = 0;
			for(int j = 0; j < N; j ++)
			{
				if(j == i)
					continue;
				
				if(stats[j][i] == '1')
				{
					tOWP[i] += (double)(won[j] - 1) / (played[j] - 1);
					count++;
				}
				else if(stats[j][i] == '0')
				{
					tOWP[i] += (double)(won[j]) / (played[j] - 1);
					count++;
				}
			}
			OWP[i] = (double)tOWP[i] / count;
//			cout<<"OWP["<<i<<"] = "<<OWP[i]<<endl;
		}

		for(int i = 0; i < N; i ++)
		{
			int count = 0;
			double tOOWP = 0; 
			for(int j = 0; j < N; j ++)
			{
				if(i == j)
					continue;					
				if(stats[i][j] == '0' || stats[i][j] == '1')
				{
					count++;
					tOOWP += OWP[j];
				}
			}
			OOWP[i] = (double) tOOWP / count;				
//			cout<<"OOWP["<<i<<"] = "<<OOWP[i]<<endl;
		}

		cout<<"Case #"<<cs++<<":"<<endl;

		for(int i = 0; i < N; i ++)
		{
			RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			cout<<RPI[i]<<endl;
		}
	}

	
	return 0;
}
