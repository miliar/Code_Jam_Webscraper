#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

struct walkway	{
	int s;
	int e;
	int w;
};

bool operator<(const walkway &a, const walkway &b)	{
	return a.w < b.w;
}

bool cmpr(const walkway &a, const walkway &b)	{
	return a.s < b.s;
}

int x;
int s;
int r;
int n;
int t;

vector<walkway> in;

int main()	{

	int kases;
	cin >> kases;
	forp(0,kases,z)	{
		
		in.clear();
		cin >> x >> s >> r >> t >> n;
		forp(0,n,i)	{
			walkway blah;
			cin >> blah.s >> blah.e >> blah.w;
			in.pb(blah);
		}
		
		sort(in.begin(),in.end(), cmpr);
		double ttime = 0;
		int pe = 0;
		int tempn = in.size();
		forp(0,tempn,i)		{
			if (pe != in[i].s)	{
				walkway blah;
				blah.s = pe;
				blah.e = in[i].s;
				blah.w = 0;
				in.pb(blah);
			}
			
			pe = in[i].e;
		}
		
		if (pe != x)	{
			walkway blah;
			blah.s = pe;
			blah.e = x;
			blah.w = 0;
			in.pb(blah);
		}
		
		sort(in.begin(),in.end());
		
		double runtimeleft = t;
		
		forp(0,in.size(),i)	{
		
			walkway cur = in[i];
			double speed = 0;
			if (runtimeleft > 0)
				speed = r;
			else
				speed = s;
			
			double timetorun = ((double)abs(cur.e - cur.s)) / (cur.w + speed);
// 			cout << runtimeleft << " " << cur.s << " " << cur.e << " " << cur.w << endl;
			if (timetorun <= runtimeleft)	{
				runtimeleft -= timetorun;
				ttime += timetorun;
			} else	{
				double tdist = (cur.w + speed) * runtimeleft;
				ttime += runtimeleft;
				runtimeleft = 0;
				double distleft = abs(cur.e - cur.s) - tdist;
				ttime += distleft / (cur.w + (double)s);
			}
// 			cout << ttime << endl;
		}
		
		printf("Case #%d: %.9lf\n", z+1, ttime);
// 		cout << "Case #" << (z+1) << ": " << ttime << endl;
	}
}