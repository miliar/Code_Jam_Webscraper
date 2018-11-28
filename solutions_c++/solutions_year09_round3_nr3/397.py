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
#include <iomanip>

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
	int cst;
	cin >> cst;
	
	RP(css, 1, cst+1)
	{
		int p, q;
		cin >> p >> q;
		
		vi rels;
		RP(i, 0, q)
		{
			int r;
			cin >> r;
			rels.pB(r);
		}
		
		sort(rels.begin(), rels.end());
		
		int minc = INT_MAX;
		
		do
		{
			int b = 0;
			vector<bool> cs(p, true);

			RI(i, rels)
			{
				int cn = *i - 1;
				cs[cn] = false;
				for (int j = cn - 1; j >= 0; --j)
				{
					if (!cs[j]) break;
					b++;
				}
				for (int j = cn + 1; j < p; ++j)
				{
					if (!cs[j]) break;
					b++;
				}
			}
			
			//cout << rels << "    " << b << endl;
			
			minc = min(minc, b);
		} while (next_permutation(rels.begin(), rels.end()));

		
		cout << "Case #" << css << ": " << minc << endl;
	}
}