#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

const double pi = 3.1415926535897932384626433832795;

//#pragma comment(linker, "/stack:1000000000")
#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORD(i,a,b) for (int i=(a);i>(b);--i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long
#define U unsigned
#define pnt pair <int,int>
int gcd(int a,int b){if (a==0) return b;return gcd(b%a,a);}

using namespace std;

void ifd() 
{
	#ifdef SAMMAX 
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
	beg = clock();
	#else

	#endif
}
void tme()
{
	#ifdef SAMMAX
		fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
	#endif
}


int main() 
{
	ifd();
	
	int t,c,d,n;
	vector <char> q;
	vector <string> comb;
	vector <string> op;
	string s;
	cin >> t;
	
	FOR(i,1,t+1)
	{
		comb.clear();
		op.clear();
		
		cin >> c;
		FOR(j,0,c)
		{
			cin >> s;
			comb.push_back(s);
		}
		
		cin >> d;
		FOR(j,0,d)
		{
			cin >> s;
			op.push_back(s);
		}

		cin >> n;
		cin >> s;
		
		q.clear();
		FOR(j,0,n)
		{
			if (q.empty())
				q.push_back(s[j]);
			else
			{
				q.push_back(s[j]);
				char a=s[j],b=q[q.size()-2];
				bool f=false;
				FOR(k,0,c)
				{
					if (((comb[k][0]==a && comb[k][1]==b) || (comb[k][0]==b && comb[k][1]==a)) && !f)
					{
						f=true;
						q.pop_back(); q.pop_back();
						q.push_back(comb[k][2]);
					}
				}
				
				if (!f)
					FOR(l,0,q.size())
				{
					a=q[q.size()-1];
					b=q[l];
						
						FOR(k,0,d)
						{	
							if (((op[k][0]==a && op[k][1]==b) || (op[k][0]==b && op[k][1]==a)) && !f)
							{
								f=true;
								q.clear();
							}
						}
				}

			}
		}
		
		printf("Case #%d: [",i);
		FOR(j,0,q.size()) 
			if (j!=q.size()-1) cout << q[j] <<", "; 
			else cout << q[j];
		printf("]\n");
	}
        
	tme();
    return 0;
}