#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

vector<long> data;
long op;
long long val;
long length;
long long cval;
long long ugly;

void sub( long k )
{
	if (k == length)
	{
		val = val + op * cval;
		if (((val)%2 == 0) || ((val)%3 == 0) || ((val)%5 == 0) || ((val) %7 ==0))
		{
			ugly++;
		}
		val = val - op * cval;
	} else
	{
		long long oval = val, oop = op, ocval = cval;
		cval = cval*10 + data[k];
		assert(cval>=0);
		sub(k+1);
		cval = ocval;
		val = oval;
		op = oop;
		val = val + op * cval;
		op = 1;
		cval = data[k];
		assert(cval>=0);
		sub(k+1);
		val = oval + oop * ocval;
		op = -1;
		cval = data[k];
		assert(cval>=0);
		sub(k+1);
		val = oval, op = oop, cval = ocval;
	}
}

int main()
{
	long n;
	long tc;
	cin >> n;
	string str;
	getline(cin,str);
	for (tc = 0; tc < n; tc++)
	{
		ugly = 0;
		val = 0;
		getline(cin,str);
		data.clear();
		for (long i=0; i<str.length(); i++)
		{
			data.push_back(str[i] - '0');
			assert((data[i] >= 0) && (data[i] <= 9));
		}
		length = str.length();
		op = 1;
		cval = data[0];
		sub(1);
		cout << "Case #" << tc+1 << ": " << ugly << endl;
	}
}

