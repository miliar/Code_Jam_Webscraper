#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;
 
#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FORI(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOR(i,a,b) for(LET(i,a);i < (b);++i)
#define FORZ(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define CS c_str()
#define PB push_back
#define SZ size()
#define INF (int)1e9+1
struct Time{
    string rep;
    int mn;
    Time(string x)
    {
	rep = x;
	int a , b;
	sscanf(x.c_str(), "%d:%d",&a,&b);
	mn = a*60+b;
    }
    Time()
    {
	rep = "";
	mn = 0;
    }
    bool operator<(const Time& a) const
    {
	return mn < a.mn;
    }
    bool operator>(const Time&a) const
    {
	return mn > a.mn;
    }
    bool operator==(const Time&a) const
    {
	return mn == a.mn;
    }
    bool operator!=(const Time&a) const
    {
	return mn != a.mn;
    }
};
int allowed;
struct Trip{
    Time st, en;
    Trip(const Time &a, const Time &b):st(a),en(b)
    {
    }
    Trip()
    {
	st = Time();
	en = Time();
    }
    bool isCompatible(const Trip &x)
    {
	return x.st.mn - en.mn >= allowed;
    }
};
typedef pair<Trip,int> PII;
vector<PII> vec;
bool comp(const PII&y, const PII& x)
{
    if(y.first.st != x.first.st)
	return y.first.st < x.first.st;
    if(y.first.en != x.first.en)
	return (y.first.en < x.first.en);
    return y.second < x.second;
}
int nA, nB;
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	/*memset(visA,0,sizeof visA);
	memset(visB,0,sizeof visB);
	memset(dp, -1, sizeof dp);
	*/
	allowed = GI;
	nA = GI, nB = GI;
	vec.clear();
	FORZ(i,nA)
	{
	    string s1, s2;
	    cin >> s1;
	    cin >> s2;
	    vec.PB(PII(Trip(s1,s2),0));
	}
	FORZ(j,nB)
	{

	    string s1, s2;
	    cin >> s1;
	    cin >> s2;
	    vec.PB(PII(Trip(s1,s2),1));
	}
	sort(vec.begin(), vec.end(), comp);
	int retA = 0, retB = 0;
	typedef pair<int, int> PI;
	PI trains[2000];
	int nt = 0;
	for(int i = 0; i < vec.SZ; ++i)
	{
	    if(vec[i].second == 0)
	    {
		bool f = 0;
		for(int j = 0; j < nt; ++j)
		{
		    if(trains[j].second == 0 && vec[i].first.st.mn - trains[j].first >= allowed)
		    {
			trains[j].first = vec[i].first.en.mn;	
			trains[j].second = 1;
			f = 1;
			break;
		    }
		}
		if(f == 0)
		{
		    retA++;
		    trains[nt++] = PI(vec[i].first.en.mn,1);
		}
	    }
	    else
	    {
		bool f = 0;
		for(int j = 0; j < nt; ++j)
		{
		    if(trains[j].second == 1 && vec[i].first.st.mn - trains[j].first >= allowed)
		    {
			trains[j].first = vec[i].first.en.mn;
			trains[j].second = 0;
			f = 1;
			break;
		    }
		}
		if(f == 0)	
		{
		    retB++;
		    trains[nt++] = PI(vec[i].first.en.mn,0);
		}
	    }
	}
	printf("Case #%d: %d %d\n",nc,retA, retB);
    }
}
