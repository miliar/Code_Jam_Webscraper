#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	int T, N;
	char schedule[101][101];
	double WP[101], OWP[101], OOWP[101];
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		cin >> N;
		for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) cin >> schedule[i][j];
		
		for(int i = 0; i < N; i++)
		{
			int vic = 0, total = 0;
			for(int j = 0; j < N; j++)
			{
				if(schedule[i][j] == '.') continue;
				
				if(schedule[i][j] == '1') vic++;
				total++;
			}
			
			WP[i] = (double)vic / total;
		}
		
		for(int i = 0; i < N; i++)
		{
			double total_OWP = 0, total_opponents = 0;
			
			for(int j = 0; j < N; j++)
			{
				if(schedule[i][j] == '.') continue;
				
				int vic = 0, total = 0;
				for(int k = 0; k < N; k++)
				{
					if(k == i) continue;
					if(schedule[j][k] == '.') continue;
					
					if(schedule[j][k] == '1') vic++;
					total++;
				}
				
				total_opponents++;
				total_OWP += (double)vic / total;
			}
			
			OWP[i] = total_OWP / total_opponents;
		}
		
		for(int i = 0; i < N; i++)
		{
			double total_OOWP = 0, total_opponents = 0;
			
			for(int j = 0; j < N; j++)
				if(schedule[i][j] != '.') 
				{
					total_OOWP += OWP[j];
					total_opponents++;
				}
			
			OOWP[i] = (double)total_OOWP / total_opponents;
		}
		
		cout << "Case #" << numCase << ":" << endl;
		for(int i = 0; i < N; i++) printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}	
}
