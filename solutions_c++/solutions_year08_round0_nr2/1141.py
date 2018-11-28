#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RI( o ) for(typeof(o.begin()) i= (o).begin(); i!=o.end(); ++i)
#define RP3( x, y, z ) RP( x, i ) RP( y, j ) RP( z, k )
#define RP( x, i ) for(int i=0; i<(x); ++i)
#define R( x ) RP((x).size(), i)
#define pB push_back

int t2s(string p)
{
	istringstream in(p);
	int h,m; char b;
	in >> h >> b >> m;
	return h*60+m;
	//return ((p[0]-'0')*10+(p[1]-'0'))*60+(p[3]-'0')*10+p[4]-'0';
}

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		int NA, NB, T;
		string m1,m2;
		cin >> T >> NA >> NB;
		int ta=0, tb=0;
		
		int al[10000],bl[10000];
		int ar[10000],br[10000];
		memset(al,0,sizeof(al));
		memset(bl,0,sizeof(bl));
		memset(ar,0,sizeof(ar));
		memset(br,0,sizeof(br));
		
		RP(NA,i)
		{
			cin >> m1 >> m2;
			al[t2s(m1)]++;
			br[t2s(m2)+T]++;
		}
		
		RP(NB,i)
		{
			cin >> m1 >> m2;
			bl[t2s(m1)]++;
			ar[t2s(m2)+T]++;
		}
		
		int a=0, b=0;
		
		for(int t=0; t<=24*60; ++t)
		{
			a+=ar[t];
			b+=br[t];
			b-=bl[t];
			a-=al[t];
			if(a<0){ta-=a; a=0;}
			if(b<0){tb-=b; b=0;}
		}
		
		cout << "Case #" << cn << ": " << ta << " " << tb << endl;
	}
	return 0;
}
