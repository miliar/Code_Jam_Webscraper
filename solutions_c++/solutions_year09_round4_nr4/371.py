#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;

int x[3];
int y[3];
int r[3];

double go(int i,int j){

    double X=x[i]-x[j];
    double Y=y[i]-y[j];

    double res=sqrt(X*X+Y*Y)+r[i]+r[j];
    return res;
}

main(){

    int T; scanf("%d",&T); for(int test=1;test<=T;test++){

	printf("Case #%d: ",test);

	int n; scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%d %d %d",&x[i],&y[i],&r[i]);
	}

	if(n==1) printf("%d\n",r[0]);
	if(n==2){
	    printf("%d\n",max(r[0],r[1]));
	}
	if(n==3){

	    double res=2e9;

	    res=min(res,max(go(0,1),double(r[2])));
	    res=min(res,max(go(0,2),double(r[1])));
	    res=min(res,max(go(1,2),double(r[0])));

	    printf("%.6lf\n",res/2);
	}
    }
}
