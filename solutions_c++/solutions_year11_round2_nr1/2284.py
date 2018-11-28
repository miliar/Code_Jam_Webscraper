#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push back
#define ST first
#define ND second

using namespace std;

struct data
{
	double wp, owp, oowp, rpi;
	int played, wins;
	string s;
	set<int> teams;
};

data t[110];
int n;

int getcount(data tab)
{
	int matchcount = 0;
	REP(i, n)
	{
		if(tab.s[i] != '.')matchcount++;
	}
	return matchcount;
}

int getwins(data tab)
{
	int wins = 0;
	REP(i,n)
	{
		if(tab.s[i] == '1')wins++;
	}
	return wins;
}

void getteams(data tab, int num)
{
	REP(i,n)
	{
		if(tab.s[i] != '.')
		{
			t[num].teams.insert(i);
//			printf("%d %c\n", i, tab.s[i]);
		}
	}
}

double getwp(data tab)
{
	double result;
	result = (double)tab.wins/(double)tab.played;
	return result;
}

double getowp(data tab)
{
	double tabwp[110];
	double arithm = 0;
	double count = 0;
	REP(i,101)tabwp[i] = -1;
	REP(i, n)
	{
		if(tab.teams.find(i)!= tab.teams.end())
		{
//			printf("%d %c\n", i, tab.s[i]);
			int oppplayed;
			int oppwins;
			oppwins = t[i].wins;
			oppplayed = t[i].played;
			if(tab.s[i] == '0')
			{
				oppwins--;
				oppplayed--;
			}
			else if(tab.s[i] == '1')
			{
				oppplayed--;
			}
			tabwp[i] = (double)oppwins/(double)oppplayed;
//			printf("%d %d %lf\n", oppwins, oppplayed, tabwp[i]);
			arithm += tabwp[i];
			count++;
		}
	}
	return arithm/count;
}

double getoowp(data tab)
{
	double tabowp[110], arithm = 0,count = 0;
	REP(i,n)
	{
		tabowp[i] = -1;
		if(tab.teams.find(i) != tab.teams.end())
		{
			tabowp[i] = t[i].owp;
			arithm += tabowp[i];
			count++;
		}
	}
	return arithm/count;
}

double getrpi(data tab)
{
//	printf("%d %d %lf %lf %lf\n", tab.wins, tab.played, tab.wp, tab.owp, tab.oowp);
	return 0.25*tab.wp + 0.5*tab.owp + 0.25*tab.oowp;
}

void solve(int num)
{
	REP(i,101)
	{
		t[i].wp = 0;
		t[i].owp = 0;
		t[i].oowp = 0;
		t[i].played = 0;
		t[i].wins = 0;
		t[i].s.clear();
		t[i].teams.clear();
	}
	scanf("%d", &n);
	REP(i,n)
	{
		cin >> t[i].s;
	}
	REP(i,n)t[i].played = getcount(t[i]);
	REP(i,n)t[i].wins = getwins(t[i]);
	REP(i,n)getteams(t[i],i);
	REP(i,n)t[i].wp = getwp(t[i]);
	REP(i,n)t[i].owp = getowp(t[i]);
	REP(i,n)t[i].oowp = getoowp(t[i]);
	REP(i,n)t[i].rpi = getrpi(t[i]);
	printf("Case #%d:\n", num);
	REP(i,n)printf("%lf\n", t[i].rpi);
}


int main()
{
	int t;
	scanf("%d", &t);
	REP(i,t)solve(i+1);
	return 0;
}