#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;


long long MOD(long long a, long long p)
{
	if (a >= 0)
		return a % p;
	if (a < 0)
		return ((a%p)+p)%p;
}
vector <bool> Prime;


long long Pow(long long y, long long pow, long long p)
{
	long long res = 1;
	long long t = y;
	while (pow > 0)
	{
		if (pow%2 == 1)
			res = (res*t)%p;
		t = (t*t)%p;
		pow /= 2;
	}
	return res;
}

int main()
{
	Prime.assign(1000003,true);
	Prime[0] = false;
	Prime[1] = false;
	for (long long i = 2; i < Prime.size(); i ++)
	{
		if (!Prime[i])
			continue;
		for (long long j = 2*i; j < Prime.size(); j += i)
			Prime[j] = false;
	}

	//freopen("test.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;

	for (int t = 1; t <= tests; t ++)
	{
		long long d,k;
		cin >> d >> k;
		vector <long long> s;
		s.resize(k);
		long long minp = 0;
		for (int i = 0; i < k; i ++)
		{
			cin >> s[i];
			minp = max(s[i],minp);
		}
		long long tenpow = 1;
		for (int i = 0; i < d; i ++)
			tenpow *= 10;

		if (k == 1)
		{
			cout << "Case #" << t << ": " << "I don't know." << endl;
			continue;
		}
		if (k == 2)
		{
			if (s[0] == s[1])
				cout << "Case #" << t << ": " << s[0] << endl;
			else
			{
				cout << "Case #" << t << ": " << "I don't know." << endl;
			}
			continue;
		}
		if (s[k-1] == s[k-2])
		{
			cout << "Case #" << t << ": " << s[k-1] << endl;
			continue;
		}

		vector <long long> res;
		for (long long p = minp+1; p <= tenpow; p ++)
		{
			if (!Prime[p])
				continue;
			////////
			long long x = MOD(s[2]-s[1],p);
			long long y = MOD(s[1]-s[0],p);
			long long a;

			vector <long long > as;
			long long y1 = Pow(y,p-2,p);
			as.push_back(x*y1);



			for (long long i = 0; i < as.size(); i ++)
			{
				long long a = MOD(as[i],p);

			long long b = MOD(s[1]-a*s[0],p);

			if (s[2] != (a*s[1]+b)%p)
				a = a;


			bool ok = true;
			for (int j = 0; ok && j < k-1; j ++)
			{
				ok = (s[j+1] == (a*s[j]+b)%p);
			}
			if (ok)
			{
				res.push_back( (a*s[k-1]+b)%p);
			}
			else
			{
				 ok = ok;
			}
			}

			//}
			
			////////
		}
		
		if (res.size() == 0)
		{
			cout << "Case #" << t << ": " << "I don't know." << endl;
			continue;
		}


		long long fres=res[0];
		for (int i = 0; i < res.size(); i ++)
			if (res[i] != fres)
			{
				fres = -1;
				break;
			}
		if (fres == -1)
			cout << "Case #" << t << ": " << "I don't know." << endl;
		else
			cout << "Case #" << t << ": " << fres << endl;

	}

	return 0;
}
