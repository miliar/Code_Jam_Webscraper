/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)
int a[10000];
int cost[12][2000];
int D[12];
int n;
int P;

int fn(int p,int q,int z){
//	cout<<p<<" "<<q<<endl;
	if(q<=p)	return 0;
	int i=p;
	int ret=0;
	bool ok=true;
	for(i=p;i<=q;i++){
		if(a[i]<P)	ok=false;
		a[i]++;
	}
	if(ok)	return 0;
	
	return 1+fn(p,p+z/2-1,z/2)+fn(q-z/2+1,q,z/2);
}

int main(){
	int tst,kas=1;
	cin>>tst;
//	tst=1;
	while(tst--){
		cout<<"Case #"<<kas++<<": ";
		cin>>P;
		n=(1<<P);
		F(i,n)	cin>>a[i];
		F(i,P){
			int k=P-i-1;
			int tot=(1<<k);
			D[i]=tot;
			F(j,tot)	cin>>cost[i][j];
		}
		cout<<fn(0,n-1,n)<<endl;
	}
	return 0;
}
