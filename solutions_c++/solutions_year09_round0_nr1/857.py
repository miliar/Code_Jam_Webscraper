#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define M make_pair
#define pB push_back
#define _1 first
#define _2 second
#define foreach(t,i) RI(i,t)
#define CLEAR(x,v) memset((x),(v),sizeof((x))
#define PRINT(o,b) RI(i,b) o << *i << (--b.end()==i ? "" : " ");
#define PE(s,e) cout << #s << " : "; for(typeof(s) i=s; i!=e; ++i) cout << (*i) << " "; cout << endl;

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<" "; return o;}

//Cake please.

int main()
{
	int l, n, d;
	cin >> l >> d >> n;
	
	vs dict;
	RP(i, 0, d)
	{
		string w;
		cin >> w;
		dict.pB(w);
	}
	
	RP(cs, 1, n+1)
	{
		string w;
		cin >> w;
		
		vector<set<char> > lets(l, set<char>());
		int cp = 0;
		bool ins = false;
		RI(ll, w)
		{
			if (*ll == '(')
			{
				ins = true;
			}
			else if (*ll == ')')
			{
				ins = false;
				cp++;
			}
			else
			{
				lets[cp].insert(*ll);
				if (!ins) cp++;
			}
		}
		
		//cout << lets << endl;
		
		int c = 0;
		
		RI(dw, dict)
		{
			bool kk = true;
			RP(i, 0, l)
			{
				if (lets[i].find((*dw)[i]) == lets[i].end())
				{
					kk = false;
					break;
				}
			}
			
			if (kk) ++c;
		}
		
		cout << "Case #" << cs << ": " << c << endl;
	}
	
	return 0;
}