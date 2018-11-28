//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<double>          VD;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef	pair<double,PII>        EL;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define Ai64(a)                  (a).begin(), (a).end()
#define RAi64(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

VVI g;
VB used;
VI ans;
int n;

i64 dist(i64 x, i64 y, i64 x1, i64 y1){
	return (x-x1)*(x-x1)+(y-y1)*(y-y1);
}

void solve() {
    int n;
		cin>>n;
		i64 w,l;
		cin>>w>>l;
		i64 r[20];
		FOR(i,0,n){
			cin>>r[i];
		}
		i64 x[20],y[20];
		while (1){
			bool p=1;
			FOR(i,0,n){
				i64 z=rand();
				x[i]=(z*31i64+z*127i64+z*z+z*z*z)%w+rand()%2;
				z=rand();
				y[i]=(z*7i64+z*z+z*z*z+z*37i64)%l+rand()%2;
			}
			FOR(i,0,n)
				FOR(j,0,i)
				if (dist(x[i],y[i],x[j],y[j])<(r[i]+r[j])*(r[i]+r[j]))
				{
					p=0;
					break;
				}
			if (p)
				break;
		}
		FOR(i,0,n)
			cout<<" "<<x[i]<<" "<<y[i];
		cout<<endl;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int A_TESTS;
	cin >> A_TESTS;
	FOR(SYS_TEST,0,A_TESTS) {

		printf("Case #%d:",SYS_TEST+1);

		solve();
	}
	return 0;
}