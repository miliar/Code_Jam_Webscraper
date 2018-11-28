#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

const int maxn = 2000;

int test,res,m,n,c,l;
double t;
double far[maxn];
double sumfar[maxn];
double a[maxn];

void init(){
    memset(far,0,sizeof(far));
    memset(sumfar,0,sizeof(sumfar));
    int i = 1;
    for(int j = 1;j<=n;j++){
        far[j] = a[i];
        i++;
        if (i>c) i = 1;
        sumfar[j] = sumfar[j-1] + far[j];
    }
}

double cal(int u,int v){
    double res = 0;
    res += sumfar[u]*2;
    if (u<n){
        if (res>=t){
            res += far[u+1];
        } else{
            double fu = (double)t - res;
            double cango = (double)fu/2.0;
            if (cango>far[u+1]){
                res += (far[u+1])*2;
            } else{
                double temp = far[u+1];
                res = res + fu +  temp - cango;
            }
        }
        
        for(int i = u+2;i<=v;i++){
            res += (double)(far[i])*2.0;
        }
        
        if (v<n){
            if (res>=t){
                res += far[v+1];
            } else{
                double fv = (double)t - res;
                double cango = (double)fv/2.0;
                if (cango>far[v+1]){
                    res += (far[v+1])*2;
                } else{
                    double temp = far[v+1];
                    res = res + fv +  temp - cango;
                }
            }
    }
        
        for(int i = v+2;i<=n;i++){
            res += (far[i])*2;
        }
    }
    return res;
}


bool solve(){
    double tres = 10e+20;
    if (l==0){
        res = int(sumfar[n]*2.0);
        return true;
    }
    for(int i = 0;i<=n;i++){
        if (l==0){
            res = int(sumfar[n]*2.0);
        } else if (l==1){
            double temp = cal(i,n);
            tres = min(tres,temp);
        } else{
            for(int j = i+1;j<=n;j++){
                double temp = cal(i,j);
                tres = min(tres,temp);
            }
        }
    }
    res = int(tres);
    return true;
}

int main(){
    ifstream fin("b.in");
    fin>>test;
    for(int i = 1;i<=test;i++){
        fin>>l>>t>>n>>c;
        for(int j = 1;j<=c;j++){
            fin>>a[j];
        }
        init();
        solve();
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    fin.close();
    system("pause");
    return 0;
}
