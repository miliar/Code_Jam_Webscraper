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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct circle{
    double x,y,r;
};

double getab(circle &a, circle &b){
    return (sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))+a.r+b.r)/2.0;
}



int main(){
    int test;
    scanf("%d",&test);
    
    for(int t=1;t<=test;t++){
        printf("Case #%d: ",t);
        double res=1e100;
        circle cs[3];
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf %lf %lf",&cs[i].x,&cs[i].y,&cs[i].r);
        
        if(n==1) res=cs[0].r;
        if(n==2) res=max(cs[0].r,cs[1].r);
        if(n==3){
            res<?=max(cs[0].r,getab(cs[1],cs[2]));
            res<?=max(cs[1].r,getab(cs[0],cs[2]));
            res<?=max(cs[2].r,getab(cs[0],cs[1]));
        }
        printf("%.6lf\n",res);
    }
    return 0;
}
