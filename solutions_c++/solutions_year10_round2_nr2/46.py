#include <string>
#include <iostream> 
#include <fstream>
#include <math.h>
#include <vector>
#include <time.h>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
const double eps = 1e-8;
#define M_PI       3.14159265358979323846

#ifdef _MSC_VER
#else
typedef long long __int64;
#endif

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tn;
	cin>>tn;
	for (int aaa=1;aaa<=tn;aaa++)
	{
		int n,k,b,t;
		cin>>n>>k>>b>>t;

		vector<double> x(n);
		vector<double> v(n);
		vector<double> ta(n);
		vector<bool> vc(n);
		for (int i=0;i<n;i++)
			cin>>x[i];
		for (int i=0;i<n;i++)
			cin>>v[i];
		for (int i=0;i<n;i++)
			ta[i] = (b - x[i]) / v[i];
		for (int i=0;i<n;i++)
			vc[i] = (ta[i] < t + 1e-10);

		vc.push_back(true);
		int r = 0;
		int p = 0;
		for (int i=n-1;i>=0;i--)
			if (vc[i])
				if (k)
				{
					--k;
					++p;
					r += (n - p - i);
				}

		if (k)
			cout<<"Case #"<<aaa<<": "<<"IMPOSSIBLE";
		else
			cout<<"Case #"<<aaa<<": "<<r;
		cout<<endl;
	}




	return 0;
}