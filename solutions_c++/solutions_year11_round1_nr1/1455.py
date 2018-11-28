#include<iostream>
#include<boost/math/common_factor_rt.hpp>

using namespace std;
using namespace boost;

bool R(int N, int PD , int PG)
{
	if(PD < 100 && PG == 100)
		return false;
	if(PD > 0 && PG == 0)
		return false;

	int g = boost::math::gcd(PD , 100);

	int d = 100/g;
	if(d <= N)
		return true;
	return false;
}

int main()
{
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++)
	{
		int N, PD, PG;
		cin >> N;
		cin >> PD;
		cin >> PG;
		if(R(N,PD,PG))
			cout << "Case #" << t << ": " << "Possible" << endl;
		else
			cout << "Case #" << t << ": " << "Broken" << endl;
	}
}

