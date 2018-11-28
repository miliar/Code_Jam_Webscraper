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

int n,test;
int pos[maxn];
int v[maxn];
int tv[maxn];
int tpos[maxn];
double result;
int d;

bool check(int i){
    int count = 0;
    memset(tpos,0,sizeof(tpos));
    for(int j = 1;j<=n;j++){
        for(int t = 1;t<=v[j];t++){
            if (count==0){
                tpos[++count] = pos[j] - i;
            } else{
                int expect = tpos[count] + d;
                if (pos[j] - d >= expect){
                    if (pos[j] - expect <=i){
                        tpos[++count] = expect;
                    } else tpos[++count] = pos[j] - i;
                    //tpos[++count] = pos[j] - d;
                } else if (abs(expect - pos[j]) <=i){
                    tpos[++count] = expect;
                } else return false;
            }
        }
    }
    for(int i = 2;i<=count;i++){
        if (tpos[count]-tpos[count-1]<d) return false;
    }
    return true;
}

void solve(){
    d = d*10;
    for(int i = 0;;i += 5){
        if (check(i)){
            result = i;
            result = result/10.0;
            break;
        }
    }
}

void init(){
    memset(pos,0,sizeof(pos));
    memset(v,0,sizeof(v));
}

int main(){
    ifstream fin("bsmall.in");
    fin>>test;
    char ch;
    for(int t = 1;t<=test;t++){
        init();
        fin>>n>>d;
        for(int i = 1;i<=n;i++){
            fin>>pos[i]>>v[i];
            pos[i] = pos[i]*10;
        }
        solve();
        cout.setf(ios::fixed);
        cout.precision(2);
        cout<<"Case #"<<t<<": "<<result<<endl;
    }
    fin.close();
   // system("pause");
    return 0;
}
