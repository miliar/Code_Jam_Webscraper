#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <iomanip>
#include <ctime>

using namespace std;

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef long double LD;
typedef vector <LL> VLL;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef vector <string> VS;
typedef vector <VS> VVS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(var,pocz,koniec) for(int var=(pocz);var<=(koniec);var++)
#define FORD(var,pocz,koniec) for(int var=(pocz);var>=(koniec>;var--)
#define FOREACH(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

/////////////////////////////////////////////////////////////////////////////////

int ff(string& s)
{
	SS ss;
	ss << s.substr(0,2);
	int m, n;
	ss >> m;
	SS ss1;
	ss1 << s.substr(3, 2);
	ss1 >> n;
	return 60*m+n;
}

int main()
{
	int ncases;
	cin >> ncases;
	int index = 0;
	while(index < ncases)
	{
		index++;
		cout << "Case #" << index << ":";
		/////////////////////////////////

		int turn;
		int na, nb;
		cin >> turn >> na >> nb;
		vector <pair<int, int> > vab (na), vba(nb);
		string tmp1, tmp2;
		REP(i,na) { cin>>tmp1>>tmp2; vab[i]=MP(ff(tmp1), ff(tmp2)); }
		REP(i,nb) { cin>>tmp1>>tmp2; vba[i]=MP(ff(tmp1), ff(tmp2)); }

	//	REP(i, na) cout << vab[i].ST << " " << vab[i].ND << endl;

		sort(vab.begin(), vab.end());
		sort(vba.begin(), vba.end());

		int n1=0, n2=0;
		while( SIZE(vab)!=0 and SIZE(vba)!=0 )
		{
			if(vab[0].ST<=vba[0].ST)
			{
				n1++;

				int curtime = vab[0].ND;

				vab.erase( vab.begin());

				while(true)
				{
					bool sign = false;
					vector<pair<int, int> >::iterator i=vba.begin();
					for(; i!=vba.end(); i++)
					{
						if( curtime + turn <= (*i).first)
						{
							curtime = (*i).ND;
							vba.erase( i);
							sign = true;
							break;
						}
					}
					if(sign==false)	break;
					
					sign = false;
					i = vab.begin();
					for(; i!=vab.end(); i++)
					{
						if( curtime + turn <= (*i).first)
						{
							curtime = (*i).ND;
							vab.erase( i);
							sign = true;
							break;
						}
					}
					if(sign==false)	break;
				}
			}
			else
			{
				n2++;

				int curtime = vba[0].ND;
				vba.erase(vba.begin());

				while(true)
				{
					bool sign = false;
					vector<pair<int, int> >::iterator i=vab.begin();
					for(; i!=vab.end(); i++)
					{
						if( curtime + turn <= (*i).first)
						{
							curtime = (*i).ND;
							vab.erase( i);
							sign = true;
							break;
						}
					}
					if(sign==false)	break;
					sign = false;

					i = vba.begin();
					for(; i!=vba.end(); i++)
					{
						if( curtime + turn <= (*i).first)
						{
							curtime = (*i).ND;
							vba.erase( i);
							sign = true;
							break;
						}
					}
					if(sign==false)	break;
				}
			}

		}

		if(SIZE(vab)>0)
			n1 += SIZE(vab);
		if(SIZE(vba)>0)
			n2 += SIZE(vba);

		cout << " " << n1 << " " << n2 << endl;
	}
	return 0;
}
