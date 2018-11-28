#include <cstring>
#include <stdio.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int compFloats(const double &a, const double &b) {
  if (fabs(a - b) < eps)
    return 0;
  return a > b ? 1 : -1;
}

deque<char> Final;
char conversions[26][26];
vector<vector<char > > conflicts;
int inQueue[26];

void calc(string s)
{
	char crrnt,last;
	bool conf ;
	for (int i = 0; i < (int)s.size(); ++i) {
		crrnt = s[i];
		if(!Final.size())
		{
			Final.pb(crrnt);
			inQueue[crrnt-'A']++;
		}
		else
		{
			last = Final.back();
			if(conversions[crrnt-'A'][last-'A'])
			{
				Final.pop_back();
				Final.pb(conversions[last-'A'][crrnt-'A']);
				inQueue[last-'A']--;
				inQueue[conversions[last-'A'][crrnt-'A']-'A']++;
			}
			else
			{
				conf = false;
				for (int j = 0; j < (int)conflicts[crrnt-'A'].size(); ++j) {
					if(inQueue[conflicts[crrnt-'A'][j]-'A'])
					{
						conf = true;
						break;
					}
				}
				if(conf)
				{
					while(Final.size())
					{
						inQueue[Final.back()-'A']--;
						Final.pop_back();
					}
				}
				else
				{
					Final.pb(crrnt);
					inQueue[crrnt-'A']++;
				}
			}
		}
	}
}


int main()
{
//	freopen("bSmall.in","r",stdin);
//	freopen("bSmall.out","w",stdout);
	freopen("bLarge.in","r",stdin);
	freopen("bLarge.out","w",stdout);

	int tc,convCount, oppCount , invokCount;
	string str;
	cin>>tc;
	for (int t = 0; t < tc; ++t) {

		Final.clear();
		conflicts.clear();
		conflicts.resize(26);
		for (int i = 0; i < 26; ++i) {
			inQueue[i] = 0;
			for (int j = 0; j < 26; ++j) {
				conversions[i][j] = 0;
			}
		}

		cout<<"Case #"<<t+1<<": [";
		cin>>convCount;
		for (int i = 0; i < convCount; ++i) {
			cin>>str;
			conversions[str[0]-'A'][str[1]-'A'] = str[2];
			conversions[str[1]-'A'][str[0]-'A'] = str[2];
		}
		cin>>oppCount;
		for (int i = 0; i < oppCount; ++i) {
			cin>>str;
			conflicts[str[0]-'A'].pb(str[1]);
			conflicts[str[1]-'A'].pb(str[0]);
		}
		cin>>invokCount;
		if(invokCount)
			cin>>str;
		calc(str);

		for (int i = 0; i < (int)Final.size(); ++i) {
			if(i)
				cout<<", ";
			cout<<Final[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
