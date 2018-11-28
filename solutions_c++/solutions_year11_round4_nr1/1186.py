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
#include <map>

#define INF (1<<30)

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;
typedef long long LL;

// first four directions + four diagonal directions + itself
int cx[]={-1,0,0,1,-1,-1,1,1,0},cy[]={0,-1,1,0,-1,1,1,-1,0};

int ingrid(int ii,int jj,int R,int C){
    if(ii < 0 || jj < 0 || ii >= R || jj >= C) return 0;
    return 1;
}
int stdout1 = 0;
int Test;

// ----------------------------------------------------------------------------------------------------------------

int N;
double X,S,R,T;

struct node{
    double dis;
    double w;
}NODE[10000];

int num;

int cmp11(node A,node B){
    if(A.w < B.w) return 1;
    else return 0;
}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); stdout1 = 1;

    scanf("%d",&Test);
    
 
    for(int t=1;t<=Test;t++){
        // begin here
        cin >> X >> S >> R >> T >> N;
        
        double dis = 0;
        double from,to;
        
        for(int i=0;i<N;i++){
            scanf("%lf %lf %lf",&from,&to,&NODE[i].w);
            NODE[i].dis = to - from;
            dis += NODE[i].dis;
        }
        X -= dis;
        
        
    
        if(X){
            NODE[N].dis = X;
            NODE[N++].w = 0;
        } 
        
        sort(NODE,NODE + N,cmp11);
        
        double ans = 0.0;
        
        
        for(int i=0;i<N;i++){
        
            double tt = min(T, NODE[i].dis / (NODE[i].w + R));
            ans += tt;
            T -= tt;
            double left = NODE[i].dis - tt * (NODE[i].w + R);
            ans += left / (NODE[i].w + S);
        }
        
        
        

        // output format
        printf("Case #%d: %lf\n",t,ans);

    }

if(!stdout1) while(1);

return 0;
}

