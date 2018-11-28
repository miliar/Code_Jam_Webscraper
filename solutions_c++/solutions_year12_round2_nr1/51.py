#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<stack>
#include<queue>
#include<deque>
#include<iostream>
using namespace std;
#define sz(X) (int)X.size()
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define ll long long
#define pii pair<int,int>
double v[210],T;
int n;
double w[210];

bool da(int p, double x){
	double V = v[p]+ x*T;
	double S = (1.0-x)*T;
	for(int i=0;i<n-1;i++){
		if(w[i] > V)
			continue;
		if(S<V-w[i])
			return true;
		S -= V-w[i];
	}
	return false;
}

int main(){
	int t;
	
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		scanf("%d",&n);
		T=0.0;
		for(int i=0;i<n;i++){
			scanf("%lf",&v[i]);
			T += v[i];
		}
		printf("Case #%d:",caso);
		for(int i=0;i<n;i++){
			int pw=0;
			for(int j=0;j<n;j++)
				if(j!=i){
					w[pw++] = v[j]; 
				}
			sort(w,w+n-1);
			double l=0,r=1.0;
			for(int it=0;it<100;it++){
				double m = 0.5*(l+r);
				if(da(i,m))r=m;
				else l=m;
			}
			printf(" %.8f",100.0*l);
		}
		printf("\n");
	}
	return 0;
}
