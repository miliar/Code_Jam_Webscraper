/*
 * Author: fatboy_cw
 * Created Time:  2011/5/22 0:11:38
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxn = 105;
int ca,t,n;
char maze[maxn][maxn];
int win[maxn][maxn];
double wp[maxn],owp[maxn],oowp[maxn];

double calc_wp(int who,int ignore){
    int r1=0,r2=0;
    for(int i=0;i<n;i++){
        if(i==ignore)   continue;
        if(win[who][i]==-1) continue;
        r2++;
        if(win[who][i]==1)  r1++;
    }
    if(r1+r2==0)    return 0.0;
    return (double)r1/r2;
}

int main() {
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%s",maze[i]);
        }
        memset(win,-1,sizeof(win));
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(maze[i][j]=='1'){
                    win[i][j]=1;
                }
                else if(maze[i][j]=='0'){
                    win[i][j]=0;
                }
            }
        }
        for(int i=0;i<n;i++){
            wp[i]=calc_wp(i,-1);
        }
        for(int i=0;i<n;i++){
            vector<double> vec;
            for(int j=0;j<n;j++){
                if(win[i][j]==-1)   continue;
                vec.push_back(calc_wp(j,i));
            }
            double sum=0.0;
            for(int j=0;j<vec.size();j++){
                sum+=vec[j];
            }
            if(vec.empty()){
                owp[i]=0.0;
            }
            else{
                owp[i]=sum/vec.size();
            }
        }
        for(int i=0;i<n;i++){
            vector<double> vec;
            for(int j=0;j<n;j++){
                if(win[i][j]==-1)   continue;
                vec.push_back(owp[j]);
            }
            double sum=0.0;
            for(int j=0;j<vec.size();j++){
                sum+=vec[j];
            }
            if(vec.empty()){
                oowp[i]=0.0;
            }
            else{
                oowp[i]=sum/vec.size();
            }
        }
        printf("Case #%d:\n",++ca);
        for(int i=0;i<n;i++){
            printf("%.7lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}

