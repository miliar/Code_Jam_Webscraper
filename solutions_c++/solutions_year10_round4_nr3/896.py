#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;
// Code Jam C
int main(){
    int t,T;
    scanf("%d",&t);
    T=t;
    while (t-->0){
        int res;
        int r;
        scanf("%d",&r);
        //printf("%d\n",r);
        int p[104][104][2];
        for (int i=0;i<100;i++)
        for (int j=0;j<100;j++) {p[i][j][1]=0; p[i][j][0]=0;}
        for (int k=0;k<r;k++){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            //printf("%d %d %d %d\n",x1,y1,x2,y2);
            for (int i=x1-1;i<x2;i++)
            for (int j=y1-1;j<y2;j++) p[j][i][0]=1;
            }
        /*for (int i=0;i<6;i++){
        for (int j=0;j<6;j++) printf("%d",p[i][j][);
        printf("\n");
        } */
        int time=0;
        bool b=false;
        while (!b){
            b=true;
            for (int i=0;i<100;i++)
            for (int j=0;j<100;j++){
                bool b1=false,b2=false;
                p[i][j][(time+1)%2]=p[i][j][time%2];
                if (i!=0){ if (p[i-1][j][time%2]==1) b1=true; else b1=false;}
                if (j!=0){ if (p[i][j-1][time%2]==1) b2=true; else b2=false;}
                if ((p[i][j][time%2]==0)&&(b1)&&(b2)) p[i][j][(time+1)%2]=1;
                if ((p[i][j][time%2]==1)&&(!b1)&&(!b2)) p[i][j][(time+1)%2]=0;
                if (p[i][j][(time+1)%2]==1) b=false;
                }
            time++;
            }
        res=time;
        printf("Case #%d: %d\n",T-t,res);
        }
    return 0;
    }
