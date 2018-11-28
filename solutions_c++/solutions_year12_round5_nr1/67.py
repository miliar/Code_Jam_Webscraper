#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

clock_t start=clock();

#define N 1111
int L[N],P[N];

bool cmp(int i,int j)
{
	int Ai=100*L[i]+(100-P[i])*L[j];
	int Aj=100*L[j]+(100-P[j])*L[i];
	if(Ai!=Aj) return Ai<Aj;
	return i<j;
}

int main()
{
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d:",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
		int n,i;
		scanf("%d",&n);
		int a[N];
		for(i=0;i<n;i++) scanf("%d",L+i),a[i]=i;
		for(i=0;i<n;i++) scanf("%d",P+i);
		sort(a,a+n,cmp);
		for(i=0;i<n;i++)
			printf(" %d",a[i]);
		printf("\n");
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
