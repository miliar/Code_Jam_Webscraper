#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <utility>
#include <string>
#include <algorithm>
#include <string.h>
#include <iomanip>
using namespace std;
double ans,tt;
double X,S,R;
double B,E,w;
long long N;
struct runway
{
	double l;
	double spd;
};

bool operator< (runway a, runway b)
{
	return (a.spd < b.spd);
}
bool operator> (runway a, runway b)
{
	return (a.spd > b.spd);
}

double ll,tmp_e;
int main ()
{
    ifstream fin("A.in");
    ofstream fout("A.out");
    int T;
    fin >> T;
	runway r[10000];
	ll = 0;
	tmp_e = 0;
    for (int t = 0 ; t < T; t++)
    {
		ans = 0;
		tmp_e = 0;
		ll = 0;
		fin >> X >> S >> R >> tt >> N;
		for (int i = 1; i <= N ; i ++)
		{
			fin >> B >> E >> w;
			ll += (B - tmp_e);
			tmp_e = E;
			r[i].spd = w ;
			r[i].l = (E-B);
		}
		sort (&r[1],&r[N+1]);
		r[0].l = ll + (X - tmp_e);
		r[0].spd = 0;
		for (int i = 0; i <= N ; i++)
		{
			if (tt <= 0)
			{
				ans += (double)r[i].l / ((double)r[i].spd + S);
			}
			else
			{
				if (tt >= ((double)r[i].l / (r[i].spd + R)))
				{
					double ttmp = ((double)r[i].l / (r[i].spd + R));
					ans += ttmp;
					tt -= ttmp;
				}
				else
				{
					ans += tt;
					r[i].l -= (tt * (r[i].spd + R));
					tt = 0;
					ans += (r[i].l) / (r[i].spd + S);
				}
			}
		}
        fout << "Case #" << t+1 << ": " << setprecision(10) << ans << endl; 
    }
}
