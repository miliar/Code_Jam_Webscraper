/*
    ID : ping128
    LANG : C++
*/
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>

#define INF (1<<30)

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;


// first four directions + four diagonal directions + itself
int cx[]={-1,0,0,1,-1,-1,1,1,0},cy[]={0,-1,1,0,-1,1,1,-1,0};

int stdout1 = 0;

int Test;

typedef pair<double,int>PPP;

PPP in[205];

double D;
int C;

double max(double x){
    if(x<0) return -x;
    return x;
}

int check(double time){
    double now;
    
 //   if(time<1.2){ printf("D %lf\n",time); }
    for(int i=0;i<C;i++){
        int j=0;
        if(i==0){ now=in[i].first-time; j=1; }
    //    if(time<1.2){ printf("D %lf",now);while(1); }
    
        for(;j<in[i].second;j++){
            if(now+D>in[i].first+time) return 0;
            else now=max(in[i].first-time,now+D);
        }
    }
  //  if(time<1.2){ printf("AAA");while(1); }
    return 1;
}

int main(){

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout); stdout1 = 1;

    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        // begin here
        scanf("%d %lf",&C,&D);
        for(int i=0;i<C;i++){
            scanf("%lf %d",&in[i].first,&in[i].second);
        }
        
        
        
        sort(in,in+C);
        
 //       for(int i=0;i<C;i++) printf("%lf %d\n",in[i].first,in[i].second);
        
        double left=0.0,right=10000000000000.0;
        double mid;
        
        while(right-left>0.0000000001){
            mid=(left+right)/2;
            if(check(mid)==0) left=mid;
            else if(check(mid)) right=mid;
    //        printf("--sdfsdf %lf %lf %lf %d\n",left,mid,right,check(mid));
       
        }



        // output format
        printf("Case #%d: %lf\n",t,left);

    }

if(!stdout1) while(1);

return 0;
}
