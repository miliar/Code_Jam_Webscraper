#include <fstream>
#include <iostream>

using namespace std;
char M[101][101];
double WP[101];
double OWP[101];
double OOWP[101];


int main()
{
	ifstream input ("A-large.in");
	ofstream output ("A-large.out");
	
	int T, tt;

	input >> T;

	for(tt = 0; tt < T; ++tt)
	{
		int N;
		input >> N;

		char temp;
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < N; ++j)
			{
				input >> temp;
				M[i][j] = temp;
			}
		}

		//WP
		for(int i = 0; i < N; ++i)
		{
			double win = 0;
			double total = 0;
			
			for(int j = 0; j < N; ++j)
			{
				if(M[i][j] == '.')
					continue;
				total = total + 1;
				win = win + M[i][j] - '0';
			}

			WP[i] = win / total;
		}

		//cout << "WP" << endl;
		//for(int i = 0; i < N; ++i)
			//cout << WP[i] << endl;


		//OWP
		for(int t = 0; t < N; ++t)
		{
			
			double tempWP[101];
			for(int k = 0; k < N; ++k)
			{
				if(t == k)
					tempWP[k] = -1;
				else
					tempWP[k] = 0;
			}

			for(int i = 0; i < N; ++i)
			{
				if(i == t)
					continue;
				if(M[i][t] == '.')
				{
					tempWP[i] = -1;
					continue;
				}

				double win = 0;
				double total = 0;

				for(int j = 0; j < N; ++j)
				{
					if(j == t)
						continue;
					if(M[i][j] == '.')
						continue;

					total = total + 1;
					win = win + M[i][j] - '0';
				}

				tempWP[i] = win / total;
			}

			double x = 0;
			double total = 0;
			for(int k = 0; k < N; ++k)
			{
				if(tempWP[k] == -1)
					continue;
				total = total + 1;
				x = x + tempWP[k];
			}

			OWP[t] = (x / total); 
		}

		//cout << "OWP" << endl;
		//for(int i = 0; i < N; ++i)
			//cout << OWP[i] << endl;


		//OOWP
		for(int i = 0; i < N; ++i)
		{
			double total = 0;
			double y = 0;
			for(int j = 0; j < N; ++j)
			{
				if(j == i)
					continue;

				if(M[i][j] == '.')
					continue;
				
				total = total + 1;
				y = y + OWP[j];

			}

			OOWP[i] = (y / total);
		}
		
		//cout << "OOWP" << endl;
		//for(int i = 0; i < N; ++i)
			//cout << OOWP[i] << endl;


		output << "Case #" << tt+1 << ":" << endl;		
		for(int i = 0; i < N; ++i)
		{
			double temp = 0;
			temp = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];

			output << temp << endl;
		}
			
		
	}

	//system("pause");
	return 0;
}