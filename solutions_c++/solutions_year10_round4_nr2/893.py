#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cmath>
#include <string.h>

using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");

int M[1050];
bool p[1050];
int price;
int n,N;
int ans;
void init(){
    int i,j;
    fin>>n;
    int tmp_n=1<<n;
    //fout<<tmp_n<<endl;
    for (i=0;i<tmp_n;i++)
    fin>>M[i];
    for (i=0;i<tmp_n-1;i++)
    fin>>price;
    memset(p,false,sizeof(p));
    ans=0;
   // cout<<ans<<endl;
}

void solve(){
    int i,j,k,tmp_n,nn;
    bool flag,flag2;
    nn=1<<n;
    for (i=n;i>=1;i--){
        tmp_n=1<<i;
        flag2=true;
        //cout<<"tmp_n:"<<tmp_n<<endl;
        for (j=0;j<nn/tmp_n;j++){
            flag=false;
            int jj=j*tmp_n;
            while (jj<(j+1)*tmp_n) {
                if (M[jj]<n) {flag=true;flag2=false;break;}
                jj++;
            }
            if (flag) {ans+=price;for (k=j*tmp_n;k<(j+1)*tmp_n;k++) M[k]++;}
            //cout<<ans<<endl;
        }
        if (flag2) break;
    }
}

int main(){
    fin>>N;
    int tmp=N;
    while (N!=0){
        N--;
        init();
        solve();
        //cout<<tmp-N<<endl;
        fout<<"Case #"<<tmp-N<<": "<<ans<<endl;
    }
    return 0;
}
