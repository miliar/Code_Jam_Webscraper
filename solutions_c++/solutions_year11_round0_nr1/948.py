#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i=0; i<n; i++)
#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define RFOR(i, x, y) for(ll i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
const double pi=acos(-1.0);

vector<pair<int, int> > a;


int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int test;
	cin>>test;

	REP(t, test)
	{
		a.clear();
		int n;
		string s;
		int k;

		cin>>n;
		REP(i, n)
		{
			cin>>s>>k;
			if (s == "O")
				a.pb(pair<int, int>(1, k));
			else a.pb(pair<int, int>(2, k));
		}

		int p1 = 1, p2 = 1;
		int t1 = -1, t2 = -1;
		ll counter = 0;
		REP(i, n)
			if (a[i].first == 1)
			{
				t1 = i;
				break;
			}

		REP(i, n)
			if (a[i].first == 2)
			{
				t2 = i;
				break;
			}

		while(!(t1 == -1 && t2 == -1))
		{
			++counter;


			if ((t1 < t2 || t2 == -1) && t1 != -1)
			{
				if (t2 != -1)
				{
					if (p2 > a[t2].second)
						p2--;

					if (p2 < a[t2].second)
						p2++;
				}

				if (p1 == a[t1].second)
				{
					bool flag = false;
					FOR(i, t1+1, n-1)
						if (a[i].first == 1)
						{
							flag = true;
							t1 = i;
							break;
						}	
					
					if (flag == false)
						t1 = -1;
				}
				else
				{
					if (p1 > a[t1].second)
						p1--;
					else p1++;
				}
			}

			else

			{
				if (t1 != -1)
				{
					if (p1 > a[t1].second)
						p1--;

					if (p1 < a[t1].second)
						p1++;
				}

				if (p2 == a[t2].second)
				{
					bool flag = false;
					FOR(i, t2+1, n-1)
						if (a[i].first == 2)
						{
							flag = true;
							t2 = i;
							break;
						}	
					
					if (flag == false)
						t2 = -1;
				}
				else
				{
					if (p2 > a[t2].second)
						p2--;
					else p2++;
				}
			}
		}


		printf("Case #%d: %d\n", t+1, counter);
	}

}