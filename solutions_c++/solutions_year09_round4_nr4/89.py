#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

double X[111],Y[111],R[111];
int n;
double solve(int a,int b){
	return (hypot(X[a]-X[b],Y[a]-Y[b])+R[a]+R[b])/2.;
}
int main(){
	int tests,cas=0;
	scanf("%d",&tests);
	while(tests--){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf%lf%lf",&X[i],&Y[i],&R[i]);
		double ans;
		if(n<=2)
			ans=*max_element(R,R+n);
		else{
			ans=max(R[0],solve(1,2));
			ans=min(ans,max(R[1],solve(0,2)));
			ans=min(ans,max(R[2],solve(0,1)));
		}
		printf("Case #%d: %.10lf\n",++cas,ans);
	}
}
