#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <list>
#include <algorithm>

using namespace std;


int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cout << "Case #"<<i<<":"<<endl;
		int n;
		
		cin >> n;
		char data[200][200];
		for ( int j=0; j<n; j++)
		{
			string s;
			cin >> s;
			for(int k=0; k<n; k++)
			{
				data[j][k] = s[k];
			}
		}
		
		long double wp[200];
		long double owp[200];
		long double oowp[200];

		int win[200];
		int lost[200];
		int tot[200];

		for(int j=0; j<n; j++)
		{
			int w = 0;
			int l = 0;
			for(int k=0; k<n; k++)
			{
				if (data[j][k] == '1')
					w++;
				if (data[j][k] == '0')
					l++;
			}
			win[j] = w;
			lost[j] = l;
			tot[j] = w+l;
			wp[j] = ((long double)(w)); 
		}

		for(int j=0; j<n; j++)
		{
			long double twp = 0;
			for(int k=0; k<n; k++)
			{
				if(data[j][k] == '0')
					twp += ((long double)(win[k]-1))/(tot[k]-1);
				if(data[j][k] == '1')
					twp += ((long double)(win[k]))/(tot[k]-1);
			}
			owp[j] = twp;
		}

		for(int j=0; j<n; j++)
		{
			long double towp = 0;
			for(int k=0; k<n; k++)
			{
				if (data[j][k] != '.')
					towp += owp[k];
			}
			oowp[j] = towp;
		}

		for(int j=0; j<n; j++)
		{
			long double res = (0.25 * wp[j] + 0.5*owp[j] + 0.25*oowp[j])/tot[j];
			cout.precision(10);
			cout << res<<endl;
		}

	}
}
