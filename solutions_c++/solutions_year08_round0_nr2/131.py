#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}

II Add(II time, int min)
{
	II ret(time);
	ret.second += min;
	ret.first += (ret.second / 60);
	ret.second %= 60;
	return ret;
}

bool comp(const II& a, const II& b)
{
	if (a.first < b.first)
		return true;
	if (a.first > b.first)
		return false;
	if (a.second < b.second)
		return true;
	return false;
}

bool lessorequal(const II& a, const II& b)
{
	if (a.first < b.first)
		return true;
	if (a.first > b.first)
		return false;
	if (a.second <= b.second)
		return true;
	return false;
}

bool comp1(const pair<II, II>& a, const pair<II, II>& b)
{
	return comp(a.first, b.first);
}

int T;

II ToTime(string str)
{
	return II((str[0] - '0')*10 + (str[1] - '0'), (str[3] - '0')*10 + (str[4] - '0'));
}


vector<pair<II, II> > AB, BA;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin>>N;
	REP(test, N)
	{
		int resa = 0, resb = 0;
		cin>>T;
		int na, nb;
		cin>>na>>nb;
		AB.clear();BA.clear();
		REP(i, na)
		{
			string s1, s2;
			cin>>s1>>s2;
			AB.pb(MP(ToTime(s1), ToTime(s2)));
		}
		REP(i, nb)
		{
			string s1,s2;
			cin>>s1>>s2;
			BA.pb(MP(ToTime(s1), ToTime(s2)));
		}
		
		sort(ALL(AB), comp1);
		sort(ALL(BA), comp1);

		vector<II> qa, qb;

		int i = 0, j = 0;
		while (i < AB.sz || j < BA.sz)
		{
			bool flAB = false;
			pair<II, II> now;
			if (i == AB.sz)
			{
				flAB = false;
				now = BA[j];
				j++;
			}
			else
				if (j == BA.sz)
				{
					flAB = true;
					now = AB[i];
					i++;
				}
				else
				{
					if (comp(AB[i].first, BA[j].first))
					{
						flAB = true;
						now = AB[i];
						i++;
					}
					else
					{
						flAB = false;
						now = BA[j];
						j++;
					}
				}

			if (flAB)
			{
				if (qa.sz == 0)
				{
					resa++;
					qb.push_back(Add(now.second, T));
					SORT(qb);
				}
				else
				{
					if (lessorequal(qa[0], now.first))
					{
						qb.push_back(Add(now.second, T));
						SORT(qb);
						qa.erase(qa.begin());
					}
					else
					{
						resa++;
						qb.push_back(Add(now.second, T));
						SORT(qb);
					}
				}
			}
			else
			{
				if (qb.sz == 0)
				{
					resb++;
					qa.push_back(Add(now.second, T));
					SORT(qa);
				}
				else
				{
					if (lessorequal(qb[0], now.first))
					{
						qa.push_back(Add(now.second, T));
						SORT(qa);
						qb.erase(qb.begin());
					}
					else
					{
						resb++;
						qa.push_back(Add(now.second, T));
						SORT(qa);
					}
				}
			}
		}

		cout<<"Case #"<<test+1<<": "<<resa<<" "<<resb<<endl;
	}
	return 0;
}