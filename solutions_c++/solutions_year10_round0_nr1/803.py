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

string solve(int n, int k)
{
	if ((k+1) % (1<<(n)) == 0)
		return "ON";
	return "OFF";
}

int main()
{
/*	time_t ct = time(0);
	int dt = 10*60 + 0*1800 + 0*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		std::cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		std::cout<<char(7);
	}

	return 0;*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t, tn = 0;
	cin>>t;
	while (tn < t)
	{
		++tn;
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<tn<<": "<<solve(n,k);
		if (tn != t)
			cout<<endl;
	}




	return 0;
}