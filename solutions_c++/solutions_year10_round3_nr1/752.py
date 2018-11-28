#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
using namespace std;

int main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		cout << "Case #" << T << ": ";
		int n;
		cin >> n;
		
		vector <int> A(n);
		vector <int> B(n);
		for (int i = 0; i < n; i++)
		{
		  cin >> A[i] >> B[i];
		}
		//vector < pair <double,double> > p;
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
		  for (int j = i+1; j < n; j++)
		  {
		    if (B[j]-B[i] == A[j]-A[i]) continue;
		    double y = (double)(B[j]*A[i] - B[i]*A[j])/(double)(B[j]-B[i] + A[i] - A[j]);
		    //double x = (y-B[i])/(B[i]-A[i]);
		    double a = (y-B[i])/(B[i]-A[i]);
		    double b = (y-A[i])/(B[i]-A[i]);
		    if (a > 0 || b < 0) { }
		    else ans++;
		  }
		}
		cout << ans << "\n";
	}
	return 0;
}
