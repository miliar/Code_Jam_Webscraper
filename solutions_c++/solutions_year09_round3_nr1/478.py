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
		string w;
		cin >> w;
		
		map<char, int> cs;
		vector<pair<int, char> > ps;
		int cc = 0;
		R(i, w)
		{
			char c = w[i];
			if (cs.find(c) == cs.end())
			{
				cc++;
				cs[c] = i;
				ps.pB(M(i, c));
			}
		}
		
		int b = cc;
		if (cc < 2) b = 2;
		
		sort(ps.begin(), ps.end());
		
		int k = 0;
		RI(i, ps)
		{
			//cout << i->first << ": " << i->second << endl;
			
			if (k == 0) cs[i->second] = 1;
			else if (k == 1) cs[i->second] = 0;
			else cs[i->second] = k;
			k++;
		}
		
		unsigned long long total = 0;
		unsigned long long place = 1;
		for (int i = w.size() - 1; i >= 0; --i)
		{
			//cout << w[i] << " " << i << " -- " << (place * cs[w[i]]) << " " << place << " " << cs[w[i]] << endl;
			total += place * cs[w[i]];
			place *= b;
		}
		
		
		cout << "Case #" << css << ": " << total << endl;
	}
	
	return 0;
}