#define MD(x) if (1) {x;}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
void MyAssert(int p){ while (!p) printf("error\n"); };
#define O1(S,A,n) MD(cout<<S<<":";for (int i=0; i<n; i++)cout<<A[i]<<" ";cout<<endl;)
#define O2(S,A,n) MD(cout<<S<<"\n";for (int i=0; i<n; i++){for (int j=0; j<n; j++)cout<<A[i][j]<<" ";cout<<endl;})
using namespace std;



double solve(double x1, double y1, double r1, double x2 ,double y2, double r2){
	return (sqrt( (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) ) + r1 + r2)/2;
}



int main(){
	int tc;
	scanf("%d",&tc);
	for (int ti=1; ti<=tc; ti++){
		printf("Case #%d: ",ti);
		// TODO
		double X[3],Y[3],R[3];
		int n;
		scanf("%d",&n);
		for (int i=0; i<n; i++)
			scanf("%lf%lf%lf",&X[i],&Y[i],&R[i]);
		double ans = 1e9;
		if (n==1){
			ans = R[0];
		}
		else if (n==2){
			double p1 = solve(X[0],Y[0],R[0],X[1],Y[1],R[1]);
			p1 = max(p1, R[2]);
			ans = p1;
			ans = min( ans, max(R[0],R[1]) );
		}
		else{
			double p1 = solve(X[0],Y[0],R[0],X[1],Y[1],R[1]);
			p1 = max(p1, R[2]);
			double p2 = solve(X[0],Y[0],R[0],X[2],Y[2],R[2]);
			p2 = max(p2, R[1]);
			double p3 = solve(X[2],Y[2],R[2],X[1],Y[1],R[1]);
			p3 = max(p3, R[0]);
			ans = min( min(p1,p2) , p3);
		}
		printf("%.10lf\n",ans);
	}

	return 0;
}
