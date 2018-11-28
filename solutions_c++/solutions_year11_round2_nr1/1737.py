#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<sstream>
#include<fstream>
using namespace std;

char table[120][120];
double Nopponent[120];
double WIN[120];
double WP[120][2];
double OWP[120];
double OOWP[120];
double RPI[120];

int main()
{

	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

	int tc;
	cin >> tc;
	for(int TC=1; TC<=tc; TC++)
	{
		memset( table, 0, sizeof table );
		memset( WP, 0, sizeof WP );
		memset( OWP, 0, sizeof OWP);
		memset( OOWP, 0, sizeof OOWP);
		memset( Nopponent, 0, sizeof Nopponent);
		memset( WIN, 0, sizeof WIN);

		int N; 
		cin >> N;
		for(int i=1; i<=N ;i++)
		{
			for(int j=1; j<=N; j++)
			{
				cin >> table[i][j];
				if(table[i][j] != '.') Nopponent[i]++;
				if(table[i][j] == '1') WIN[i]++;
			}
		}
		
		for(int i=1;i<=N; i++)
		{
			WP[i][0] = WIN[i];
			WP[i][1] = Nopponent[i];
		}

		for(int i=1; i<=N; i++)
		{
			double tmpJA = 0, cnt = 0;
			for(int j=1; j<=N; j++)
			{
				if(i == j) continue;
				if(table[j][i] != '.') cnt++;
				if(table[j][i] == '1')
					tmpJA += (WIN[j]-1) / (Nopponent[j]-1);
				if(table[j][i] == '0')
					tmpJA += (WIN[j]) / (Nopponent[j]-1);
			}
			OWP[i] = tmpJA / cnt;
			//cout << OWP[i] << endl;
			//cout << tmpJA << " " << cnt << endl;
		}

		for(int i=1; i<=N; i++)
		{
			double cnt = 0;
			double tmp = 0;
			for(int j=1; j<=N; j++)
			{
				if(table[j][i] != '.')
				{
					tmp += OWP[j];
					cnt++;
				}
			}
			OOWP[i] = tmp / cnt;
		}

		for(int i=1; i<=N; i++)
		{
			RPI[i] = 0;
			RPI[i] += 0.25 * (WP[i][0]/WP[i][1]);
			RPI[i] += 0.50 * OWP[i];
			RPI[i] += 0.25 * OOWP[i];
		}
	
		cout << "Case #"<< TC << ":" << endl;
		for(int i=1; i<=N; i++)
		{
			cout << RPI[i] << endl;
			//cout << WP[i][0] << " " << WP[i][1] << " " << OWP[i] << " " << OOWP[i] << endl;
		}
	}
	return 0;
}