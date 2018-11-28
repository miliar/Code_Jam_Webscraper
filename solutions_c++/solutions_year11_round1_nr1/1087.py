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

int gcd(int a, int b)
{
	if(a < b)
		return gcd(b, a);
	if(a % b == 0)
		return b;
	return gcd(b, a % b);
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		long long N;
		cin >> N;
		int Pd, Pg;
		cin >> Pd >> Pg;
		//cout << " N " << N << " Pd " << Pd << " Pg " << Pg << endl;
		if(Pg == 100 && Pd != 100)
		{
			cout << "Case #" << i << ": Broken" << endl;
			continue;
		}
		if(Pd == 0)
		{
			cout << "Case #" << i << ": Possible" << endl;
			continue;
		}
		if(Pg == 0)
		{
			cout << "Case #" << i << ": Broken" << endl;
			continue;
		}		
		int div = gcd(Pd, 100);

		if(100/div <= N)
			cout << "Case #" << i << ": Possible" << endl;
		else
			cout << "Case #" << i << ": Broken" << endl;
		
	}
	//system("pause");
	return 0;
}
