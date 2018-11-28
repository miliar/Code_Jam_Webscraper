#define _CRT_SECURE_NO_DEPRECATE 1
#include <vector>     
#include <map>     
#include <set>     
#include <deque>     
#include <algorithm>     
#include <utility>     
#include <sstream>     
#include <iostream>     
#include <cstdio>     
#include <cmath>     
#include <cstdlib>     

using namespace std;

#define SZ(a) ((int)(a).size())
#define pii pair<int,int>
#define mp make_pair
#define ll long long
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

struct TTime
{
	int m, h;
	void addMinutes(int n)
	{
		m += n;
		h += m/60;
		m %= 60;
	}
	void setTime(int hh, int mm)
	{
		h = hh; m = mm;
	}
	void clear()
	{
		m = 0; h = 0;
	}
};

typedef pair<TTime, TTime> Time;

int compare(Time a, Time b)
{
	if (a.first.h < b.first.h) return false;
	if (a.first.h > b.first.h) return true;
	if (a.first.m < b.first.m) return false;
	if (a.first.m > b.first.m) return true;

	if (a.second.h < b.second.h) return false;
	if (a.second.h > b.second.h) return true;
	if (a.second.m < b.second.m) return false;
	if (a.second.m > b.second.m) return true;
	return false;
}
int compare(TTime a, TTime b)
{
	if (a.h < b.h) return false;
	if (a.h > b.h) return true;
	if (a.m < b.m) return false;
	if (a.m > b.m) return true;

	return false;
}
bool canGo(TTime t, Time tt)
{
	return ( t.h < tt.first.h || (t.h == tt.first.h && t.m <= tt.first.m) );
}

string solve(int turnTime, vector<Time> a, vector<Time> b)
{
	int aCnt = 0, bCnt = 0;
	for (int i = 0; i < SZ(a); ++i)
	{
		for (int j = i+1; j < SZ(a); ++j)
		{
			if (compare(a[i], a[j]))
				swap(a[i], a[j]);
		}
	}
	for (int i = 0; i < SZ(b); ++i)
	{
		for (int j = i+1; j < SZ(b); ++j)
		{
			if (compare(b[i], b[j]))
				swap(b[i], b[j]);
		}
	}
	TTime trainTime;
	bool fl = false;
	trainTime.clear();
	trainTime.h = 24;
	while (SZ(a) + SZ(b) > 0)
	{
		if (fl == true && SZ(a) > 0)
		{
			for (int i = 0; i < SZ(a); ++i)
				if (canGo(trainTime, a[i]))
				{
					trainTime = a[i].second;
					trainTime.addMinutes(turnTime);
					a.erase(a.begin()+i);
					fl = false;
					break;
				}
			if (!fl) continue;
		}
		if (fl == false && SZ(b) > 0)
		{
			for (int i = 0; i < SZ(b); ++i)
				if (canGo(trainTime, b[i]))
				{
					trainTime = b[i].second;
					trainTime.addMinutes(turnTime);
					b.erase(b.begin()+i);
					fl = true;
					break;
				}
				if (fl) continue;
		}
		if (SZ(a) > 0 && SZ(b) > 0)
		{
			fl = compare(a[0], b[0]);
			trainTime = !fl ? a[0].second : b[0].second;
		}
		else
		{
			if (SZ(a) == 0)
			{
				fl = true;
				trainTime = b[0].second;
			}
			else
			{
				fl = false;
				trainTime = a[0].second;
			}
		}
		if (fl)
		{
			b.erase(b.begin());
			++bCnt;
		}
		else
		{
			a.erase(a.begin());
			++aCnt;
		}
		trainTime.addMinutes(turnTime);
	}

	return convert<string>(aCnt) + " " + convert<string>(bCnt);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	vector <Time> a, b;
	for (int i = 0; i < testCnt; ++i)
	{
		a.clear(); b.clear();
		int turnTime;
		cin >> turnTime;
		int na, nb;
		cin >> na >> nb;
		for (int j = 0; j < na; ++j)
		{
			string s;
			cin >> s;
			TTime ta, tb;
			ta.setTime(convert<int>(s.substr(0, 2)), convert<int>(s.substr(3, 5)));
			cin >> s;
			tb.setTime(convert<int>(s.substr(0, 2)), convert<int>(s.substr(3, 5)));
			a.push_back(mp(ta, tb));
		}
		for (int j = 0; j < nb; ++j)
		{
			string s;
			cin >> s;
			TTime ta, tb;
			tb.setTime(convert<int>(s.substr(0, 2)), convert<int>(s.substr(3, 5)));
			cin >> s;
			ta.setTime(convert<int>(s.substr(0, 2)), convert<int>(s.substr(3, 5)));
			b.push_back(mp(tb, ta));
		}
		cout << "Case #" << i+1 << ": " << solve(turnTime, a, b) << endl;
	}
	return 0;
}