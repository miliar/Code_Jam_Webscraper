#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<iterator>
#include<algorithm>
#include<queue>
#include<stack>
#include<iomanip>
#include<cstdio>
#include<cctype>
using namespace std;

#define fe(e,C) for(__typeof((C).begin()) e=(C).begin(); e!=(C).end(); e++)
#define all(C) (C).begin(), (C).end()
#define unique(C) (C).erase(unique(all(C)), (C).end())
#define PB(el) push_back(el)


template<class T, class K> 
K CAST(T element){
    stringstream ss;
    ss<<element;
    K output;
    ss>>output;
    return output;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int test=1; test<=T; test++){
	int x1,x2,x3,y1,y2,y3,x1p,x2p,x3p,y1p,y2p,y3p;
	scanf("%d%d%d%d%d%d", &x1,&y1,&x2,&y2,&x3,&y3);
	scanf("%d%d%d%d%d%d", &x1p,&y1p,&x2p,&y2p,&x3p,&y3p);

	int A1=x1-x3-x1p+x3p,
	    A2=y1-y3-y1p+y3p,
	    B1=x2-x3-x2p+x3p,
	    B2=y2-y3-y2p+y3p,
	    C1=x3p-x3,
	    C2=y3p-y3;
	int detW=A1*B2-B1*A2,
	    dett1=C1*B2-B1*C2,
	    dett2=A1*C2-A2*C1;
	printf("Case #%d: ", test);
	if(detW==0)
	    printf("No Solution\n");
	else{
	    double t1=(double)dett1/detW,
		   t2=(double)dett2/detW,
		   X=x1*t1+x2*t2+x3*(1.0-t1-t2),
		   Y=y1*t1+y2*t2+y3*(1.0-t1-t2);
	    if(0<=t1 && t1<=1 && 0<=t2 && t2<=1)
		printf("%.6lf %.6lf\n", X, Y);
	    else
		printf("No Solution\n");
	}
    }
    return 0;
}

