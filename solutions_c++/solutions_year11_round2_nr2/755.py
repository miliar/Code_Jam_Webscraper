# include <iostream>
# include <stack>
# include <vector>
# include <fstream>
# include <iomanip>
# include <algorithm>
using namespace std;

struct interval
{
	int start;
	int end;
	int num;
	double max_length;
	double length;
};

int main()
{
	ifstream cin("B.in");
	ofstream cout("B.out");
	int t;
	cin >> t;
	int testcase = 0;
	while(t - testcase)
	{
		double ans = 0.0;
		int c, d;
		cin >> c >> d;
		vector<int> v(c);
		vector<int> p(c);
		for(int i = 0; i < c; ++i)
			cin >> p[i] >> v[i];

		stack<interval> st;
		for(int i = 0; i < c; ++i)
		{
			interval itv = {i, i, v[i], static_cast<double>((v[i] - 1) * d) / 2.0, static_cast<double>((v[i] - 1) * d) / 2.0};
			while(!st.empty())
			{
				interval last_itv = st.top();
				if(static_cast<double>(p[last_itv.end]) + last_itv.length >= static_cast<double>(p[itv.start]) - itv.length - static_cast<double>(d))
				{
					itv.start = last_itv.start;
					itv.num += last_itv.num;
					itv.length = static_cast<double>(((itv.num - 1) * d) - (p[itv.end] - p[itv.start])) / 2.0;
					itv.max_length = max(itv.max_length, itv.length);
					itv.max_length = max(itv.max_length, last_itv.max_length);
					st.pop();
				}
				else
					break;
			}
			st.push(itv);
		}

		while(!st.empty())
		{
			ans = max(st.top().max_length, ans);
			st.pop();
		}

		cout << "Case #" << testcase + 1 << ": " << setprecision(10) << setiosflags(ios::fixed | ios::showpoint) << ans << endl;
		++testcase;
	}
	return 0;
}

/*
1
3 2
0 3
1 3
2 3

*/