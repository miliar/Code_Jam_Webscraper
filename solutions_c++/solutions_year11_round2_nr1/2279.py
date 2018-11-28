#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <limits>
using namespace std;

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int N;
		cin >> N;

		char teams[100][100]; 
		double teamWP[100];
		
		for (int j = 0; j < N; j++)
		{
			int win = 0;
			int lose = 0;
			for (int k = 0; k < N; k++)
			{
				char c;
				cin >> c;
				teams[j][k] = c;
				if (c == '1') win++;
				if (c == '0') lose++;		
			}			
			teamWP[j] = ((double) win) / ((double) (win + lose));			
			//cout << "TeamWP " << j << " : " << teamWP[j] << " \n";
		}

		cout << "Case #" << (i+1) <<":\n";

		double oWPField[100];
		double ooWPField[100];
		for (int j=0; j < N; j++)
		{
			double oWP = 0.0;
			double ooWP = 0.0;
			double oponents = 0;			
			for (int k=0; k < N; k++)
			{
				if (teams[j][k] != '.')
				{
					oponents++;
					int win = 0;
					int lose = 0;
					double ooWPCount = 0;
					double ooKWP = 0.0;
					for (int w=0; w < N; w++)
					{
						if (teams[k][w] != '.' && w != j)
						{
							if (teams[k][w] == '1') win++;
							if (teams[k][w] == '0') lose++;
						
						}						
					}

					double oponentKWP = ((double) win) / ((double) (win + lose));


					oWP += oponentKWP;
				}
			}
			oWP /= oponents;
			oWPField[j] = oWP;
		}

		for (int j=0; j < N; j++)
		{		
			double ooWP = 0.0;
			double oponents = 0;			
			for (int k=0; k < N; k++)
			{
				if (teams[j][k] != '.')
				{
					oponents++;
					ooWP += oWPField[k];
				}
			}
			ooWPField[j] = ooWP / oponents;
			//cout << j << " " << oWPField[j] << "  " << ooWPField[j] <<"\n";
			double rpi = 0.25 * teamWP[j] + 0.5 *oWPField[j] + 0.25 * ooWPField[j];
			cout.precision(10);
			cout << rpi << "\n";
		}
	
	}

}
