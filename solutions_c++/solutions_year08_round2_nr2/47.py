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

VVI adj;
VI visited;
int a,b,p;

int gcd(int a,int b) {return b==0?a:gcd(b,a%b);}

bool Merge(int a,int b,int p) {
	int g,x;
	g=x=gcd(a,b);
	for(int i=2;i*i<=x;++i) {
		if(x%i==0&&i>=p)return true;
		while(x%i==0)x/=i;
	}
	if(x>1&&x>=p)return true;
	return false;
}

void visit(int x) {
	visited[x]=true;
	FOR(i,a,b+1)
		if(adj[x][i]&&!visited[i])visit(i);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int N,tcase;
	for(cin>>N,tcase=1;tcase<=N;++tcase) {
		cin>>a>>b>>p;
		adj=VVI(b+1,VI(b+1));
		FOR(i,a,b+1)FOR(j,i,b+1)
			if(Merge(i,j,p))adj[i][j]=adj[j][i]=1;
		visited=VI(b+1);
		int cnt=0;
		FOR(i,a,b+1)
			if(!visited[i]) {
				cnt++;
				visit(i);
			}
		cout<<"Case #"<<tcase<<": "<<cnt<<endl;
	}
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
