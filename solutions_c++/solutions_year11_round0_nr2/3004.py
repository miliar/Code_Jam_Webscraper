/* headers & macros  */
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  
#define DBG()   cout << "hello "<< DBG++;

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	/*}}}*/

int DBG = 0;


int main()
{
	int cas, n, c, d;
	bool f, cf;
	char ch, c1, c2;
	string combine[1000], destroy[1000];
	cin >> cas;
	REP(x, cas)
	{
		stack<char> s;
		cin >> c;
		REP(i, c)
			cin >> combine[i];
		cin >> d;
		REP(i, d)
			cin >> destroy[i];
		cin >> n;
//		cout << n << endl;
		REP(i, n)
		{
			cin >> ch;
			s.push(ch);
			f = true;
			while(f)
			{
				if(s.size() > 1)
				{
					c1 = s.top();
					s.pop();
					c2 = s.top();
					cf = true;
					REP(i, c)
					{
						if((combine[i][0] == c2 && combine[i][1] == c1) || (combine[i][0] == c1 && combine[i][1] == c2))
						{
							s.pop();
							s.push(combine[i][2]);
							cf = false;
						}
					}
					if(cf)
					{
						s.push(c1);
						f = false;
						break;
					}
				}
				else
					break;
			}

			deque<char> dq;
			while(!s.empty())
			{
				c1 = s.top();
				s.pop();
				dq.PF(c1);
			}

			bool mf = false;

			REP(j, d)
			{
				IT(dq) it1, it2;
				it1 = find(dq.BN, dq.ED, destroy[j][0]);
				it2 = find(dq.BN, dq.ED, destroy[j][1]);
				if(it1 != dq.ED && it2 != dq.ED)
				{
					mf = true;
					break;
				}
				it1 = find(dq.BN, dq.ED, destroy[j][1]);
				it2 = find(dq.BN, dq.ED, destroy[j][0]);
				if(it1 != dq.ED && it2 != dq.ED)
				{
					mf = true;
					break;
				}				
			}
			if(mf == true)
			{
//				s.clear();
				continue;
			}
			FORIT(it, dq)
				s.push(*it);

		}
		deque<char> dque;
		while(!s.empty())
		{
			c1 = s.top();
			s.pop();
			dque.PF(c1);
		}

		printf("Case #%d: [", x+1);

		FORIT(it, dque)
		{
			if(it != dque.BN)
				cout << ", ";
			cout << (*it);
		}

		cout << "]" << endl;

	}
	return 0;
}
