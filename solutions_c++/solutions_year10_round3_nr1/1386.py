#include <iostream>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int main()
{
	long t;
	cin >> t;
	for (long z = 1; z <= t; z ++)
	{
		long long n, s = 0;
		cin >> n;
		vector < pair <long long, long long> > v(n);

		for(long long i = 0; i < n; i ++)	{
			cin >> v[i].first >> v[i].second;
		}

		for(long long i = 0; i < n; i ++)	{
			if(v[i].first == v[i].second)	continue;

			for (long long j = i + 1; j < n; j ++)	{
//			if (v[i].first < v[i].second)	{
				if ((v[j].first < v[i].first && v[j].second > v[i].second) || (v[j].first > v[i].first && v[j].second < v[i].second))	s ++;
//			} else	{
//				if ((v[j].first < v[i].first && v[j].second > v[i].second) || ())	s ++;
//			}
			}
		}
		cout << "Case #" << z << ": " << s << endl;
	}
	return 0;
}




