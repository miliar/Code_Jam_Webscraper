#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define N 1005
#define eps (1e-9)

using namespace std;

int X,S,R,T,n,x,ts,te,tp,TC;
double t,AC;

struct path{
	int s,e,w;
	bool operator < (const path &T )const {return s<T.s;};
}P[N];

struct node{
	int s,e,w;
	node(){}
	node(int s,int e,int w):s(s),e(e),w(w){};
	bool operator < (const node & T) const {
		if (w!=T.w) return T.w<w;
		else return (e-s)<(T.e-T.s);
	}
};
priority_queue<node> Q;


int main(){
	scanf("%d",&TC);
	for (int C=1;C<=TC;C++){
		scanf("%d%d%d%d%d",&X,&S,&R,&T,&n);
		t=T;
		
		for (int i=0;i<n;i++)
			scanf("%d%d%d",&P[i].s,&P[i].e,&P[i].w);
			
		while (!Q.empty()) Q.pop();
		sort(P,P+n);
		x=0;
		AC=0.0;
		for (int i=0;i<n;i++){
			if (P[i].s!=x)
				Q.push(node(x,P[i].s,S));
			Q.push(node(P[i].s,P[i].e,P[i].w+S));
			x=P[i].e;
		}
		if (x!=X) Q.push(node(x,X,S));
		
		while (!Q.empty()){
			ts = Q.top().s;
			te = Q.top().e;
			tp = Q.top().w;
			Q.pop();
			double U = ((te-ts)*1.0)/((tp-S+R)*1.0);
			if (t>=U){
				t-=U;
				AC+=U;
			}
			else {
				AC+=(te-ts-t*(tp-S+R))*1.0/(tp*1.0)+t;
				t=0;
			}
		}

		printf("Case #%d: %.7lf\n",C,AC);
	}
	scanf("\n");
	return 0;
}
