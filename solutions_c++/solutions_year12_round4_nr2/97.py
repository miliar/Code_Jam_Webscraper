#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define AL(x) x.begin(),x.end()
#define pw(x) (1ull<<(x))
#define M 1000000007
using namespace std;
typedef pair<int,int> pt;
typedef vector<int> vt;

int n,w,h;
pair<int,int>q[1111];
double x[1111],y[1111],xx[1111],yy[1111];

double rd(long long x){
	long long r=0;
	for (int i=0;i<16;i++)r=r*10+rand()%10;
	x*=1000000;
	r%=x;
	return r/1000000.;
}


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	srand((int)time(NULL));
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n >> w >> h;
		for (int i=0;i<n;i++)cin >> q[i].F;
		for (int i=0;i<n;i++)q[i].S=i;
		sort(q,q+n);
		reverse(q,q+n);
		for (int i=0;i<n;i++){
			for(;;){
				x[i]=rd(w);
				y[i]=rd(h);
				int t=0;
				for (int j=0;j<i;j++)if (sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]))+1e-2<q[i].F+q[j].F)t=1;
				if (!t)break;
			}
		}
		for (int i=0;i<n;i++)xx[q[i].S]=x[i],yy[q[i].S]=y[i];
		cout << "Case #" << E << ":";
		for (int i=0;i<n;i++)printf(" %.3lf %.3lf",xx[i],yy[i]);
		puts("");
	}
	return 0;
}


