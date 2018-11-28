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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define PB push_back
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define MP make_pair
#define PRESENT(container, element) (container.find(element) != container.end())
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define CLEAR(c,n) memset(c,n,sizeof(c))
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double PI=acos(-1.0);
const double EPS=1e-11;
const int INF=1000000000;

#define MX 1000001
LL a, b, p, t,n;
struct NODE {
	LL num;
	int grp;
};
NODE node[MX];
bool isp[MX];
int np, primes[MX];
void genprime()
{
	CLEAR(isp,true);
	isp[0]=isp[1]=false;
	for (int i=2; i*i<MX; ++i) if (isp[i]) for (int j=i*i; j<MX; j+=i) isp[j]=false;
	np=0;
	REP(i,MX) if (isp[i]) primes[np++]=i;
//	REP(i,np) cout << primes[i] << endl;// system("pause");
}
LL gcd(LL a, LL b) { return a?gcd(b%a,a):b;}
int g(int id)
{
	int res=id, tmp;
	while (node[res].grp!=res) res=node[res].grp;
	while (id!=res) tmp=node[id].grp,node[id].grp=res,id=tmp;
//	cout << id << res << endl; system("pause");
	return res;
}
int main()
{
	genprime();
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	cin>>t;
	REP(ic,t) {
		cin>>a>>b>>p; --p;
		n=b-a+1;
		REP(i,n) {
			node[i].num=a+i; node[i].grp=i;
			REP(j,np) {
				if (primes[j]>p) break;
				while (node[i].num%primes[j]==0) node[i].num/=primes[j];
				if (node[i].num<=p) node[i].num=1;
				if (primes[j]*primes[j]>node[i].num) break;
			}
//			cout << i << " " << node[i].num << endl;
		}
		bool change=true;
		while (change) {
			change=false;
			REP(i,n) REP(j,i) if (g(i)!=g(j)&&gcd(node[i].num,node[j].num)!=1) {
//				cout << i << j << g(i) << g(j) << endl;
				node[g(j)].grp=g(i),change=true;
			}
//			REP(i,n) cout << i << " " << node[i].grp << endl; system("pause");
		}
		int tot=0;
		REP(i,n) if (node[i].grp==i) ++tot;
		printf("Case #%d: %d\n", ic+1, tot);
	}
	return 0;
}
