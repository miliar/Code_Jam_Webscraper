#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	long long tt;
	cin >> tt;
	for(long long test = 1; test <= tt; test++)
	{
		long long l, t, n, c, a;
		cin >> l >> t >> n >> c;
		l = min(l, n);
		vector<long long> s(n, 0LL);
		for(int i = 0; i < c; i++)
		{
			cin >> a;
			for(long long k = 0; k*c+i < n; k++)
				s[k*c+i] = a;
		}

		vector<bool> boost(n);
		for(long long i = n-1; i >= n-l; i--)
			boost[i] = true;

		long long sum = 0LL;
		long long place = -1LL;
		bool e = false;
		for(long long i = 0LL; i < n; i++)
		{
			sum += s[i]*2LL;
			if(sum >= t)
			{
				if(sum == t) e = true;
				place = i;
				break;
			}
		}

		if(place == -1LL)
		{
			long long res = 0LL;
			for(long long i = 0LL; i < n; i++)
				res += 2LL*s[i];
			cout << "Case #" << test << ": " << res << endl;
			continue;

		}

		long long res = 0LL;
		if(e == true)
		{
			place++;
			vector<long long> srt(s.begin()+place, s.end());
			sort(srt.rbegin(), srt.rend());
			for(long long i = 0LL; i < place; i++)
				res += s[i]*2LL;
			long long kk = 0LL;
			for(long long i = 0LL; i < srt.size(); i++)
			{
				if(kk < l)
				{
					kk++;
					res += srt[i];
				}
				else
					res += srt[i]*2LL;
			}
		}
		else
		{
			double _res = 0.0;
			vector<double> ds(s.begin(), s.end());
			ds.insert(ds.begin()+place, ds[place]-double(sum-t)/2.0);
			ds[place+1] = ds[place+1] - ds[place];



			place++;
			vector<double> srt(ds.begin()+place, ds.end());
			sort(srt.rbegin(), srt.rend());
			for(long long i = 0; i < place; i++)
				_res += ds[i]*2;
			long long kk = 0;
			for(long long i = 0; i < srt.size(); i++)
			{
				if(kk < l)
				{
					kk++;
					_res += srt[i];
				}
				else
					_res += srt[i]*2;
			}
			res = (long long)(_res + 0.5);
		}

		cout << "Case #" << test << ": " << res << endl;


	}



	return 0;
}