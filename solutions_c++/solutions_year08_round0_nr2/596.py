#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct mytime
{
	int _hh; int _mm;
	void advance(int amt) { _mm += amt; if (_mm >= 60) {_hh += _mm / 60; _mm %= 60;} }
};

struct mypair
{
	mytime t1; mytime t2;
};

int cmp(mytime t1, mytime t2)
{
	if (t1._hh != t2._hh) return (t1._hh - t2._hh);
	else return (t1._mm - t2._mm);
}

bool operator<(mytime t1, mytime t2)
{
	return cmp(t1, t2) < 0;
}

bool operator<=(mytime t1, mytime t2)
{
	return cmp(t1,t2) <= 0;
}

bool operator<(mypair p1, mypair p2) 
{ return p1.t1 < p2.t1; }

mytime get_time(string s)
{
	mytime t;
	t._hh = (s[0]-'0')*10 + s[1]-'0';
	t._mm = (s[3]-'0')*10 + s[4]-'0';
	return t;
}

void print(vector<mypair> vp)
{
//	cout << "vp: " << vp.size() << endl;
	printf("vp: %d\n", vp.size());
	for(int i=0; i < vp.size(); i++)
	{
		printf("%02d:%02d - %02d:%02d\n", vp[i].t1._hh, vp[i].t1._mm, vp[i].t2._hh, vp[i].t2._mm);
	}
}

void print(mytime t)
{
	printf("%02d:%02d\n", t._hh, t._mm);
}

int get_train(const vector<mypair> &va_sch, const vector<mypair> &vb_sch, int taround)
{
	int ret = va_sch.size();
	int bitmap[110] = {0};
	for(int i=0; i < vb_sch.size(); i++)
	{
		mytime tarr = vb_sch[i].t2; tarr.advance(taround);
		for(int j=0; j < va_sch.size(); j++)
		{
			if (bitmap[j]) continue;
			if (tarr <= va_sch[j].t1) { bitmap[j] = 1; break; }
		}
	}
	for(int i=0; i < va_sch.size(); i++)
		if (bitmap[i]) ret--;
	return ret;
}

void mycount(const vector<mypair> &va_sch, const vector<mypair> &vb_sch, int &na_train, int &nb_train, int taround)
{
	na_train = get_train(va_sch, vb_sch, taround);
	nb_train = get_train(vb_sch, va_sch, taround);
}

int main()
{
	int ncase;
	cin >> ncase;
	for(int ix=0; ix < ncase; ix++)
	{
		int taround;
		cin >> taround;
		vector< mypair > va_sch, vb_sch;
		int na, nb; string dep, arr;
		cin >> na >> nb;
		for(int ia=0; ia < na; ia++)
		{
			cin >> dep >> arr;
			mytime t1 = get_time(dep);
			mytime t2 = get_time(arr);
			mypair pt = {t1,t2};
			va_sch.push_back(pt);
		}
		for(int ib=0; ib < nb; ib++)
		{
			cin >> dep >> arr;
			mytime t1 = get_time(dep);
			mytime t2 = get_time(arr);
			mypair pt = {t1,t2};
			vb_sch.push_back(pt);
		}
		sort(va_sch.begin(), va_sch.end());
		sort(vb_sch.begin(), vb_sch.end());
//		print(va_sch); print(vb_sch);
		int na_train, nb_train;
		mycount(va_sch, vb_sch, na_train, nb_train, taround);
		printf("Case #%d: %d %d\n", ix+1, na_train, nb_train);
	}
}

