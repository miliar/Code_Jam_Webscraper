#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <fstream>
using namespace std;
 
#define MSG(a)  cout << #a << "=" << a << endl;
#define VAR(a,b) __typeof(b) a=b
#define FORIT(it,v) for(VAR(it,(v).begin());it!=(v).end();++(it))
template<class T, class U> T cast (U x) { T y; ostringstream a; a<<x; 
istringstream b(a.str()); b>>y; return y; }
#define SZ(v) ((int)(v).size())
#define FU(i,a,b) for(int i=(a);i<int(b);++i)
#define FD(i,a,b) for(int i=(a);i>=int(b);--i)
#define REP(i,n) FU(i,0,n)
#define ALL(a) a.begin(),a.end()
#define ISS istringstream
#define OSS ostringstream

typedef long long LONG;

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	int TTT;
	in >> TTT;

	FU(CASE,0,TTT)
	{
		int n;
		in >> n;

		vector<LONG> u;
		vector<LONG> v;
		LONG coord;

		FU(i,0,n)
		{
			in >> coord;
			u.push_back(coord);
		}

		FU(i,0,n)
		{
			in >> coord;
			v.push_back(coord);
		}

		sort(ALL(u)); sort(ALL(v));
		
		LONG ans = 0;
		FU(i,0,n) ans += u[i]*v[n-i-1];
	
		out << "Case #" << CASE+1 << ": " << ans << endl;
	}
}