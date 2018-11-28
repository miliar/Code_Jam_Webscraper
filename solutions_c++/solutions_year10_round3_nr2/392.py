#include <iostream>
#include <cmath>

using namespace std;

int simAns(long long L, long long P, long long C)
{
	long long ut = 0;
	if(L*C >= P)
		return 0;
	while (L < P)
	{
		++ut; L*=C;
	}
	return max((int)ceil(log2(ut)), 1);
}

int main()
{
	int T, t;
       	long long L, P, C;
	cin >> T;
	for(t=1; t<=T; ++t)
	{
		cin >> L >> P >> C;
		cout << "Case #" << t << ": " << simAns(L, P, C) << endl;
	}
}
