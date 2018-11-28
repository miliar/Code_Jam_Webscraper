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

int test,res,m,n;
char b[maxn][maxn];

bool check(int i,int j){
    if (b[i][j+1] == '#' &&
        b[i+1][j] == '#' &&
        b[i+1][j+1] == '#'){
        return true;
    } else return false;
}


bool solve(){
    for(int i = 1;i<m;i++){
        for(int j = 1;j<=n;j++){
            if (b[i][j] == '#'){
                if (check(i,j)){
                    b[i][j] = '/';
                    b[i][j+1] = '\\';
                    b[i+1][j] = '\\';
                    b[i+1][j+1] = '/';
                }
            }
        }
    }
    for(int i = 1;i<=m;i++){
        for(int j = 1;j<=n;j++){
            if (b[i][j] == '#') return false;
        }
    }
    return true;
}

int main(){
    ifstream fin("alarge.in");
    fin>>test;
    for(int t = 1;t<=test;t++){
        fin>>m>>n;
        for(int i = 1;i<=m;i++){
            for(int j = 1;j<=n;j++){
                fin>>b[i][j];
            }
        }
        if (solve()){
            cout<<"Case #"<<t<<":"<<endl;
            for(int i = 1;i<=m;i++){
                for(int j = 1;j<=n;j++){
                    cout<<b[i][j];
                }
                cout<<endl;
            }
        } else{
            cout<<"Case #"<<t<<":"<<endl;
            cout<<"Impossible"<<endl;
        }
    }
    fin.close();
    return 0;
}
