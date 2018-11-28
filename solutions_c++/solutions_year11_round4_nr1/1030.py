#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <ctime>

using namespace std;
struct walkway{
	int st,en,v;
	walkway(int a=0,int b=0,int c=0){
		st=a;
		en=b;
		v=c;
	}
} A[1000001];

bool mycmp(walkway a,walkway b){
	return a.v<b.v;
}

double gettime(double S,double v1,double v2,double &t){
	double res=0;
	double t1=S/v2;
	double tt=min(t,t1);
	t-=tt;
	res=tt+(S-v2*tt)/v1;
	return res;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int Q;
	scanf("%d",&Q);
	for(int test=1;test<=Q;test++){
		int X,S,R,T,N;
		scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
		int gap=0;
		for(int i=0;i<N;i++){
			int B,E,W;
			scanf("%d%d%d",&B,&E,&W);
			if(!i)gap+=B;
			else gap+=B-A[i-1].en;
			A[i]=walkway(B,E,W);
		}
		gap+=X-A[N-1].en;
		sort(A,A+N,&mycmp);
		double pos=0,t=0,v=0,rt=T;
		t+=gettime(gap,S,R,rt);
		for(int i=0;i<N;i++){
			t+=gettime(A[i].en-A[i].st,A[i].v+S,A[i].v+R,rt);
		}
		printf("Case #%d: %.9lf\n",test,t);
	}
	return 0;
}
