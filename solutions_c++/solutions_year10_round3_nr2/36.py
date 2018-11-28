#include<iostream>
#include<string>
#include<map>
#include<cmath>
using namespace std;

int main()
{
	int CAS;
	cin >> CAS;
	for(int cas=1; cas <= CAS; cas++)
	{
		long long L, P, C;
		cin >> L >> P >> C;
		long long pows = 0, mul = 1;
		while (L * mul < P)
		{
			mul*= C;
			pows ++;
		}
		long long ans = 0;
		mul = 1;
		while(mul < pows)
		{
			mul *= 2;
			ans++;
		}
		cout << "Case #" << cas << ": " << ans << endl;
	}
	return 0;

}
