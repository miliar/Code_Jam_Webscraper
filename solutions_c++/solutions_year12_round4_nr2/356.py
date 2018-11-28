#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;


bool reversed;

double dist(double x, double y)
{
	return sqrt(x*x + y*y);
}

bool check(int w, int h, vector<int> r, vector <pair<int,int> > ans)
{
	int n = r.size();
	for (int i = 0; i < n; ++i)
	{
			if (ans[i].first < 0 || ans[i].first > w || ans[i].second < 0 || ans[i].second > h)
				throw 4242;
		for (int j = i+1; j < n; ++j)
		{
			double d = dist(ans[i].first - ans[j].first, ans[i].second - ans[j].second);
			if (d < r[i] + r[j])
				throw 4242;
		}
	}
	return true;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int tc = 0;
	cin >> tc;
	for (int t = 1 ; t <= tc; ++t) {
		int n;
		int w,h;
		cin >> n >> w >> h;
		if (w < h)
		{
			reversed = true;
			swap(w,h);
		}
		else 
			reversed = false;

		vector <pair<int,int> > arr(n);
				vector <int> r(n);
		for (int i =0 ; i < n ;++i )
		{
			cin >> arr[i].first;
			r[i] = arr[i].first;
			arr[i].second = i;
		}
		sort(arr.rbegin(),arr.rend());
		vector <pair<int,int> > ans(n);
		int rw = w;
		int rh = h;
		vector <bool> placed(n, false);
		int cnt = 0;
		int last = 0;
		int noww = 0;
		while (cnt < n)
		{
			while (placed[last])
				last++;
			if (rh == h)
			{
				int idx = arr[last].second;
				if (rw == w)
				{
					rw -= arr[last].first;
					noww = arr[last].first;
					ans[idx].first = 0;
				}
				else
				{
					ans[idx].first = w-rw+arr[last].first;
					rw -= 2*arr[last].first;
					noww = 2*arr[last].first;
				}
				ans[idx].second = 0;
				rh -= arr[last].first;
				placed[last] = true;
				cnt ++;
				continue;
			}
			bool ok = false;
			for (int fit = last;fit < n; ++fit)
			{
				if (!placed[fit] && 2*arr[fit].first <= noww &&
					rh >= arr[fit].first)
				{
					int idx = arr[fit].second;
					ans[idx].first = w - rw - noww + arr[fit].first;
					ans[idx].second = h-rh + arr[fit].first;
					rh -= 2* arr[fit].first;
					placed[fit] = true;
					cnt ++;
					ok = true;
					break;
				}
			}
			if (!ok)
			{
				rh = h;
			}
		}


		if (!check(w,h,r,ans))
			throw 4242;
		
		cout << "Case #" << t << ":";
		for (int i = 0; i < n; ++i)
			if (reversed)
				cout << " " << ans[i].second << " " << ans[i].first;
			else
				cout << " " << ans[i].first << " " << ans[i].second;
		cout << endl;
	}

	return 0;
}