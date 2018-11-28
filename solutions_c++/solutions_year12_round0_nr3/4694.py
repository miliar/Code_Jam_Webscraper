#pragma comment(linker,  "/STACK:16777216")
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <locale>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long Ull;

#define VI vector <int>
#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define RFOR(i, a, b) for(int (i) = (a)-1; (i) >= (b); --(i))
#define CLEAR(a) memset((a), , sizeof(a))
#define INF 1000000000
#define PB push_back
#define ALL(c) (c).begin(),  (c).end()
#define pi 2*acos(0.0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-7
#define INF 2000000000

int a,b,l;
string S,A,B;
set<pair<int,int> > s;

int ans()
{
	s.clear();
	FOR(i,a,b+1)
	{
		stringstream ss;
		ss << i;
		ss >> S;
		l = S.size();
		FOR(j,1,l)
		{
			A = S.substr(0,j);
			B = S.substr(j);
			stringstream sss;
			sss << B << A;
			int ans;
			sss >> ans;
			if (ans >= a && ans <= b && ans != i)
			{
				if (s.find(MP(max(ans,i),min(ans,i))) == s.end())
				s.insert(MP(max(ans,i),min(ans,i)));
			}
		}
	}



	return s.size();
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		cin >> a >> b;
		cout << "Case #" << tt+1 << ": " << ans() << endl;
	}

	return 0;
}