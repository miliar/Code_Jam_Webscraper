#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <bitset>
#include <cctype>
#include <numeric>
#include <functional>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
#define pb push_back
#define sz size()
#define all(x) (x).begin(), (x).end()
#define GI ( { int t; scanf("%d",&t); t; } )
#define dbg(x) cout << #x << "= " << x << endl;
#define dbgg(x) cout << #x << endl;
#define eps 1e-8
#define eps1 1e-5
#define pi 2*acos(0.0)
#define mp make_pair
#define ff first
#define ss second

int main()
{
	int opos, otime, bpos, btime;
	int pos, time, t = GI;
	char c;
	int posdiff, timediff;
	
	for( int cas=1; cas<=t; cas++ )
	{
		int n = GI;
		//vector< pair<char,int> > v;
		otime = btime = time = 0;
		opos = bpos = 1;
		

		for( int i=0; i<n; i++ )
		{
			cin >> c >> pos;
			
			if( c == 'O' )
			{
				posdiff = abs(pos - opos);
				timediff = time - otime;

				if( posdiff <= timediff )
				{
					time += 1;
					otime = time;
					opos = pos;
				}
				else
				{
					time += (posdiff-timediff) + 1;
					otime = time;
					opos = pos;
				}
			}

			else if( c == 'B' )
			{
				posdiff = abs(pos - bpos);
				timediff = time - btime;

				if( posdiff <= timediff )
				{
					time += 1;
					btime = time;
					bpos = pos;
				}
				else
				{
					time += (posdiff-timediff) + 1;
					btime = time;
					bpos = pos;
				}
			}
		}

		cout << "Case #" << cas << ": " << time << endl;
	}
	
	return 0;
}
