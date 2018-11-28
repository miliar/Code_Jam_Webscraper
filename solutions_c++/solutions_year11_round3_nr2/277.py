#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

long long l, c, n;
long long t;

long long val[1001];
long long num[1001];
long long sta[1001];

long long solve ()
{
	cin >> l >> t >> n >> c;

	for (long long i = 0; i < c; i += 1)
	{
		cin >> val[i];
	}

	for (long long i = 0; i < c; i += 1)
	{
		num[i] = n/c + (i < n%c ? 1 : 0);
	}

	long long result = 0;

	long long k;

	long long i;
	for (i = 0; i < n; i += 1)
	{
		if (t < result + 2*val[i%c])
		{
			k = i;
			break;
		}
		else
		{
			result += 2*val[i%c];
		}
	}

	if (i == n)
	{
		return result;
	}

	for (long long i = 0; i < c; i += 1)
	{
		sta[i] = k/c + (i <= k%c ? 1 : 0);
	}
	
	val[1000] = val[k%c] - (t - result) / 2;
	num[1000] = 1;
	sta[1000] = 0;

	result = t;

//	cout << "result = " << result << endl;
//	for (long long i = 0; i < n; i += 1)
//	{
//		cout << i << ": " << sta[i] << " " << num[i] << " " << val[i] << endl;
//	}
//	cout << 1000 << ": " << sta[1000] << " " << num[1000] << " " << val[1000] << endl;

	priority_queue< pair<long long,long long> > coda;

	for (long long i = 0; i < c; i += 1)
	{
		if (sta[i] < num[i])
		{
			coda.push (make_pair (val[i], i));
		}
	}
	coda.push (make_pair (val[1000], 1000));

	for (long long i = 0; i < l; i += 1)
	{
		if (coda.empty ())
			break;

		pair<long long,long long> top = coda.top ();
		coda.pop ();

		result += top.first;

		sta[top.second] += 1;
		if (sta[top.second] < num[top.second])
		{
			coda.push (top);
		}
	}

//	cout << "result = " << result << endl;
//	for (long long i = 0; i < n; i += 1)
//	{
//		cout << i << ": " << sta[i] << " " << num[i] << " " << val[i] << endl;
//	}
//	cout << 1000 << ": " << sta[1000] << " " << num[1000] << " " << val[1000] << endl;

	for (long long i = 0; i < c; i += 1)
	{
		result += 2 * val[i] * (num[i] - sta[i]);
	}
	result += 2 * val[1000] * (num[1000] - sta[1000]);

	return result;
}

int main ()
{
	long long tc;
	cin >> tc;
	for (long long i = 0; i < tc; i += 1)
	{
		cout << "Case #" << i+1 << ": " << solve () << endl;
	}
}

