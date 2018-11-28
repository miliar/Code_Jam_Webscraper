#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

void writeCaseNumber(int num) { printf("Case #%d: ",num); }

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;

	for (int tst=0; tst<tn; tst++) {
		writeCaseNumber(tst+1);
		int a,n,m;
		cin>>n>>m>>a;
		int X1,Y1,X2,Y2=-1;
		for (int x1=0; x1<=n; x1++)
			for (int y1=0; y1<=m; y1++)
				for (int x2=0; x2<=n; x2++)
					for (int y2=0; y2<=m; y2++) {
						if (x1*y2-x2*y1==a) 
							X1=x1, Y1=y1, X2=x2, Y2=y2;
					}
		if (Y2==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d %d %d %d %d %d\n",0,0,X1,Y1,X2,Y2);
	}

	return 0;
}
