#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

double getWP (vector <string> arr, int n, int i)
{
	long long cnt = 0,win = 0;
	for (int j = 0; j < n; j++) 
	{
		if (arr[i][j] == '1') win++;
		if (arr[i][j] != '.') cnt++;
	}
	return (double)win/cnt;
}
	
double getOWP (vector <string> arr, int n, int i)
{
	double tot = 0;
	int cnt = 0;
	for (int j = 0; j < n; j++)
	{
		if (arr[i][j] != '.')
		{
			cnt++;
			arr[j][i] = '.';
			double p = getWP(arr,n,j);
			tot += p;
		}
	}
	return tot/cnt;
}

double getOOWP (vector <string> arr, int n, int i)
{
	double tot = 0;
	int cnt = 0;
	for (int j = 0; j < n; j++)
	{
		if (arr[i][j] != '.')
		{
			cnt++;
			double p = getOWP(arr,n,j);
			tot += p;
		}
	}
	return tot/cnt;
}

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		cout << "Case #" << T << ":\n";
		int n;
		cin >> n;
		vector <string> arr(n);

		for (int i = 0; i < n; i++) cin >> arr[i];

		for (int i = 0; i < n; i++)
		{
			double wp = getWP(arr,n,i);
			double owp = getOWP(arr,n,i);
			double oowp = getOOWP(arr,n,i);
			
			
			cout << (0.25*wp + 0.50*owp + 0.25*oowp) << "\n";
		}
	}
}
