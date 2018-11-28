#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>

using namespace std;

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pint;

int in(){int a; scanf("%d",&a); return a;}
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};

typedef pair<pint,int> tint;
#define one first.first
#define two first.second
#define thr second

double t;
int s,r,n,x;
tint p[1010];


int main(){
	int ts = in();
	rep(cas,ts){
		x = in(); s = in(); r = in(); t = in(); n = in();
		int rest = x;
		rep(i,n){
//			b[i] = in(); e[i] = in(); w[i] = in();
			p[i].two = in(); p[i].thr = in(); p[i].one = in();
			rest -= p[i].thr - p[i].two;
		}
//		cout << s << ' ' << r << endl;
//		cout << "rest " << rest << endl;
		sort(p,p+n);
		double total = 0.0;
		if(rest <= t*r){
			t -= (double)rest / r;
			total += (double)rest / r;
		}else{
			total += t;
			total += ((double)rest - t*r)/s;
			t = 0;
		}
//		cout << "total " << total << endl;
		rep(i,n){
			if(p[i].thr-p[i].two <= t * (p[i].one + r)){
				t -= (double)(p[i].thr-p[i].two) / (p[i].one + r);
				total += (double)(p[i].thr-p[i].two) / (p[i].one + r);
			}else{
				total += t;
				total += ((double)(p[i].thr-p[i].two)-t*(p[i].one + r)) / (p[i].one + s);
				t = 0;
			}
		}
		cout << "Case #" << cas+1 << ": ";
		printf("%.7f\n",total);
	}
	
    return 0;
}

