#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define ISIN(s,a) (s.find(a)!=s.end())
#define VI vector <int>
#define VVI vector <vector <int> >
#define pb push_back
#define mp make_pair
#define pnt pair <int,int>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) (((a)>0)?(a):-(a))
#define LL long long
#define U unsigned
#define ALL(a) a.begin(),a.end()

using namespace std;

#define DOUT(a) cerr << a << endl;
#define SOUT(a) cerr << a << "  ";

int pows[31];

int main()
{
	//freopen("sample.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	pows[0]=1;
	FOR(i,1,31) pows[i]=2*pows[i-1];
	int nn;
	scanf("%d",&nn);
	FOR(i,1,nn+1)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		if ((k+1)%pows[n]!=0) printf("OFF\n");
		else printf("ON\n");
	}
	return 0;
}
