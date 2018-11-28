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
double sq(double a){
	return a*a;
}
double Dist(double a,double b,double c,double d){
	return sqrt(sq(a-c)+sq(b-d));
}
int main(){
	int t,n;
	cin>>t;
	int cas=1;
	while(t--){
		cout<<"Case #"<<cas++<<": ";
		cin>>n;
		vector<double> x(n),y(n),r(n);
		F(i,n)	cin>>x[i]>>y[i]>>r[i];
		VI w(n);
		F(i,n)	w[i]=i;
		double ans;
		int k=1;
		do{
			double v=0;
			if(n==1)	v=r[0];
			if(n==2){
				v=max(r[0],r[1]);
			}
			if(n==3){
				v=Dist(x[w[0]],y[w[0]],x[w[1]],y[w[1]])+r[w[0]]+r[w[1]];
				v/=2.;
				v=max(v,r[w[2]]);
			}
			if(k)	ans=v;
			else{
				ans=min(ans,v);
			}
			k=0;
		}while(next_permutation(ALL(w)));
		cout<<setiosflags(ios::fixed)<<setprecision(8)<<ans<<endl;
	}
	return 0;
}
