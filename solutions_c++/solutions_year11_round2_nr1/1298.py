#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		vector<string> teams(N);
		for(int j = 0; j < N; j++)
			cin >> teams[j];
		
		cout << "Case #" << i << ":" << endl;
		vector<double> OWP(N);
		vector<double> WP(N);
		for(int j = 0; j < N; j++)
		{
			double wp, owp = 0;
			int num = 0, den = 0;
			for(int k = 0; k < N; k++)
			{
				if(teams[j][k] == '.')
					continue;
				den++;
				num += teams[j][k] - '0';
			}
			wp = num*1.0/den;
			WP[j] = wp;
			int ct = 0;
			for(int k = 0; k < N; k++)
			{
				if(teams[j][k] == '.')
					continue;				
				ct++;			
				num = 0;
				den = 0;
				for(int m = 0; m < N; m++)
				{
					if(m == j)
						continue;
					if(teams[k][m] == '.')
						continue;
					den++;
					num += teams[k][m] - '0';
				}
				owp += (num*1.0)/den;
			}
			owp = owp/ct;
			OWP[j] = owp;
		}
		for(int j = 0; j < N; j++)
		{
			int ct = 0;
			double oowp = 0;
			for(int k = 0; k < N; k++)
			{
				if(teams[j][k] == '.')
					continue;
				ct++;
				oowp += OWP[k];
			}
			oowp /= ct;
			//cout << " wp " << WP[j] << endl;
			//cout << " owp " << OWP[j] << endl;
			//cout << " oowp " << oowp << endl;
			double rpi = 0.25*WP[j] + 0.5*OWP[j] + 0.25*oowp;
			
			cout << rpi << endl;
		}
		
	}
	return 0;
}
