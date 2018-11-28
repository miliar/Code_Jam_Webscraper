#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cmath>
#include <string.h>

using namespace std;

ifstream fin("A-small.in");
ofstream fout("A-small.out");
char *res;
int n,k,t;
int f[3][2]={{1,0},{0,1},{1,1}};
char map[51][51];
bool flag_R,flag_B;

void init(){
    fin>>n>>k;
    int i,j,c;
    char *tmpc;
    memset(map,0,sizeof(map));
    t=-1;
    for (i=0;i<n;i++){
        fin>>tmpc;
        c=0;
        for (j=n-1;j>=0;j--){
            if (tmpc[j]!='.'){
                map[i][c]=tmpc[j];
                c++;
            }
        }
        if (c==0) t=i;
    }
    for (i=0;i<n;i++)
    fout<<map[i]<<endl;
    flag_R=false;
    flag_B=false;
}

void solve(){
    int i,j,p;
    char tmp;
    bool dot;
    for (i=t+1;i<n;i++){
        for (j=0;j<n;j++){
            if (map[i][j]==0) break;
            tmp=map[i][j];
            dot=false;
            if (i+k-1<n){ for (p=1;p<k;p++) {
                            if (map[i+p][j]!=tmp) break;
                            }
                           if (p==k) dot=true;
            }
            if (j+k-1<n) { for (p=1;p<k;p++){
                            if (map[i][j+p]!=tmp) break;
                            }
                            if (p==k) dot=true;
            }
            if (i+k-1<n && j+k-1<n) { for (p=1;p<k;p++){
                                        if (map[i+p][j+p]!=tmp) break;
                                        }
                                      if (p==k) dot=true;
            }
            if (i+k-1<n && j-k+1>=0){ for (p=1;p<k;p++){
                                        if (map[i+p][j-p]!=tmp) break;
                                        }
                                        if (p==k) dot=true;
            }
            if (dot){if (tmp=='R') flag_R=true;else flag_B=true;}
        }
        if (flag_R && flag_B) break;
    }
}




int main(){
    int N;
    fin>>N;
    int tmp=N;
    while (N!=0){
        N--;
    fin>>n>>k;
    int i,j,c;
    char *tmpc;
    memset(map,0,sizeof(map));
    t=-1;
    for (i=0;i<n;i++){
        fin>>tmpc;
        c=0;
        for (j=n-1;j>=0;j--){
            if (tmpc[j]!='.'){
                map[i][c]=tmpc[j];
                c++;
            }
        }
        if (c==0) t=i;
    }
    //for (i=0;i<n;i++) fout<<map[i]<<endl;
    flag_R=false;
    flag_B=false;
        solve();
        if (flag_R && flag_B) res="Both";
        else if (flag_R) res="Red";
        else if (flag_B) res="Blue";
        else res="Neither";
        fout<<"Case #"<<tmp-N<<": "<<res<<endl;
    }
    return 0;
}
