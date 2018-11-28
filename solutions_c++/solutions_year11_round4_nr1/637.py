#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>
#include <string.h>

using namespace std;

#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("A-large.in", "r", stdin);
	outputstream = freopen("A-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

vector<pair<double, int> > wws;

int main()
{
	init();
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i)
	{
		wws.clear();
		int X, S, R, T, N;
		cin >> X >> S >> R >> T >> N;
		int lenw = X;
		for (int j = 0; j < N; ++j)
		{
			int tb, te;
			double tw;
			cin >> tb >> te >> tw;
			lenw -= (te - tb);
			wws.push_back(make_pair(tw, te - tb));
		}
		wws.push_back(make_pair(0, lenw));
		sort(wws.begin(), wws.end());
		double leftt = T;
		double res = 0;
		for (int j = 0; j < wws.size(); ++j)
		{
			double maxt = wws[j].second / (wws[j].first + R);
			double runt = min(leftt, maxt);
			double walkt = (wws[j].second - runt * (wws[j].first + R)) / (S + wws[j].first);
			res += (runt + walkt);
			leftt -= runt;
		}
		printf("Case #%d: %.9f\n", i, res);
	}
	return 0;
}
