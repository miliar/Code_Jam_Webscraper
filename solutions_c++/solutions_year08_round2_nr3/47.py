#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

VI tree;

int GetK(int k,int nd=0,int a=0,int b=-1) {
	if(b<0)b=(1<<20)-2;
//	cerr<<"GetK("<<k<<", "<<nd<<", "<<a<<", "<<b<<")"<<endl;
	if(tree[nd]==0)return a+k;
	else {
		int m=(a+b)/2;//[a,m],[m+1,b]
		if(k>=(m-a+1)-tree[nd+nd+1])
			return GetK(k-(m-a+1)+tree[nd+nd+1],nd+nd+2,m+1,b);
		else return GetK(k,nd+nd+1,a,m);
	}
}
void Mark(int k,int nd=0,int a=0,int b=-1) {
	if(b<0)b=(1<<20)-2;
	tree[nd]++;
	if(a<b) {
		int m=(a+b)/2;//[a,m],[m+1,b]
		if(k<=m)Mark(k,nd+nd+1,a,m);
		else Mark(k,nd+nd+2,m+1,b);
	}
}
int GetSum(int k,int nd=0,int a=0,int b=-1) {
	if(b<0)b=(1<<20)-2;
	if(b<=k)return b-a+1-tree[nd];
	if(a>k)return 0;
	if(tree[nd]==0)return k-a+1;
	else {
		int m=(a+b)/2;//[a,m],[m+1,b]
		return GetSum(k,nd+nd+1,a,m)+GetSum(k,nd+nd+2,m+1,b);
	}
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int N,tcase;
	for(cin>>N,tcase=1;tcase<=N;++tcase) {
		int k,n;
		cin>>k>>n;
		VI d(n);
		REP(i,n)cin>>d[i];
		VI deck(k);
		tree=VI((1<<21)+5);
		int pos=0;
		REP(i,k) {
			pos=GetK((GetSum(pos-1)+i)%(k-i));
			//cerr<<i<<" -> "<<pos<<endl;
			deck[pos]=i+1;
			Mark(pos);
		}
		
		cout<<"Case #"<<tcase<<":";
		REP(i,n)cout<<" "<<deck[d[i]-1];
		cout<<endl;
	}
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
