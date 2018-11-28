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


int a[100][100];
bool b[100][100];
int cnt[100];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int test;
	cin>>test;

	REP(t, test)
	{

		int C, D, N;
		REP(i, 50)
			REP(j, 50)
			a[i][j] = b[i][j] = 0;

		string s;
		cin>>C;
		REP(i, C)
		{
			cin>>s;
			a[s[0] - 'A' + 1][s[1] - 'A' + 1] = a[s[1] - 'A' + 1][s[0] - 'A' + 1] = s[2] - 'A' + 1;
		}

		

		cin>>D;
		REP(i, D)
		{
			cin>>s;
			b[s[0] - 'A' + 1][s[1] - 'A' + 1] = b[s[1] - 'A' + 1][s[0] - 'A' + 1] = true;
		}

		cin>>N;
		cin>>s;

		string result;

		REP(i, 50)
			cnt[i] = 0;

		REP(i, N)
		{

			if (result.size() == 0)
			{
				result.pb(s[i]);
				cnt[s[i] - 'A' + 1] = 1;
				continue;
			}
			else
			{
				
				/*if (a[result[result.size()-1] - 'A' + 1][s[i] - 'A' + 1] > 0)
				{
					char last = result[result.size()-1];
					char next = a[result[result.size()-1] - 'A' + 1][s[i] - 'A' + 1] + 'A' - 1;

					cnt[last - 'A' + 1]--;
					cnt[next + 'A' - 1]++;
					result[result.size() - 1] = next;
				}*/

				result.pb(s[i]);
				cnt[s[i] - 'A' + 1]++;

				while(result.size() > 1)
				{
					char last1 = result[result.size() - 2];
					char last2 = result[result.size() - 1];

					if (a[last1 - 'A' + 1][last2 - 'A' + 1] > 0)
					{
						cnt[last1 - 'A' + 1]--;
						cnt[last2 - 'A' + 1]--;
						result.erase(result.size() - 1);
						result[result.size() - 1] = a[last1 - 'A' + 1][last2 - 'A' + 1] + 'A' - 1;

						cnt[result[result.size() - 1] - 'A' + 1]++;
					}
					else 
						break;
				}

				if (result.size())
				{
					REP(j, 30)
						if (b[result[result.size() - 1] - 'A' + 1][j] == true)
							if (cnt[j] > 0)
							{
								result.clear();
								REP(p, 30)
									cnt[p] = 0;
								break;
							}
				}

			}

		}
		printf("Case #%d: [", t+1);
		if (result.size() > 0)
		{
			REP(i, result.size() - 1)
				cout<<result[i]<<", ";
			cout<<result[result.size() - 1];
		}
		cout<<"]\n";
	}

}