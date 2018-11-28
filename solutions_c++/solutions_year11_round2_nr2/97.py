#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define xx first
#define yy second
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////
string testname="b-large";

void run_sol(int casenr){
	int d,c;
	scanf("%d%d",&c,&d);
	d*=2;
	Pair a[201];
	for (int i=0;i<c;i++){
		scanf("%d%d",&a[i].xx,&a[i].yy);
		a[i].xx*=2;
	}
	printf("Case #%d: ",casenr);
	long long low=-1,up=1LL<<60;
	while(low+1<up){
		long long mid=(low+up)/2;
		long long pos=-(1LL<<60);
		bool ok=true;
		for (int i=0;i<c;i++){
			for (int j=0;j<a[i].yy;j++){
				long long cur=pos+d;
				if (a[i].xx>=cur){
					cur=max(cur,a[i].xx-mid);
				}
				else{
					if (cur-a[i].xx>mid) ok=false;
				}
//				if (mid==1) printf("%d -> %I64d\n",a[i].xx,cur);
				pos=cur;
			}
		}
		if (ok) up=mid;
		else low=mid;
	}
	printf("%.2lf\n",(double)up/2.0);
}
int main(){
	freopen((testname+".in").c_str(),"r",stdin);
	freopen((testname+".out").c_str(),"w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
		run_sol(t);
	return 0;
}
