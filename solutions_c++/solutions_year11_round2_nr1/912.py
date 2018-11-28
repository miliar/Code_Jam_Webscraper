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

const int maxn = 1000;

int test,n;
int win[maxn];
int lose[maxn];
int opp[maxn];
double owp[maxn];
char b[maxn][maxn];
double result = 0;

double getWP(int i){
    double w = win[i];
    double l = lose[i];
    return w/(w+l);
}

double getOWP(int i){
    double res = 0;
    for(int j = 1;j<=n;j++){
       if (b[i][j] != '.'){
           double w = win[j];
           double l = lose[j];
           if (win[j] + lose[j] == 1) continue;
                if (b[i][j]=='1'){
                    res = res + w/(w+l-1);
                } else if (b[i][j] == '0') {
                    res = res + (w-1)/(w+l-1);
                }
            }
    }
    double num = win[i] + lose[i];
    if (win[i] + lose[i] ==0) return 0;
    return res/num;
}

double getOOWP(int i){
    double res = 0;
    for(int j = 1;j<=n;j++){
        if (b[i][j] != '.'){
            res += owp[j];
        }
    }
    double num = win[i] + lose[i];
    if (win[i] + lose[i] == 0) return 0;
    return res/num;
}

void init(){
    memset(win,0,sizeof(win));
    memset(lose,0,sizeof(lose));
    memset(owp,0,sizeof(owp));
    result = 0;
}

void solve(){
    for(int i = 1;i<=n;i++){
        owp[i] = getOWP(i);
        //cout<<owp[i]<<endl;
    }
    cout.precision(8);
    cout.setf(ios::fixed);
    for(int i = 1;i<=n;i++){
        cout<<0.25*getWP(i) + 0.5*owp[i] + 0.25*getOOWP(i)<<endl;
    }
}

int main(){
    ifstream fin("alarge.in");
    fin>>test;
    char ch;
    for(int t = 1;t<=test;t++){
        init();
        fin>>n;
        for(int i = 1;i<=n;i++){
            for(int j = 1;j<=n;j++){
                fin>>b[i][j];
                if (b[i][j]=='1'){
                    win[i]++;
                    opp[i]++;
                    opp[j]++;
                } else if (b[i][j]=='0'){
                    lose[i]++;      
                }
            }
        }
        cout<<"Case #"<<t<<":"<<endl;
        solve();
    }
    fin.close();
    return 0;
}
