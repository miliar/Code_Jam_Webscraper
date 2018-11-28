#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<fstream>
#include<bitset>
using namespace std;
bitset<1024> bst;
int n,t,a[1024];
long long unsigned zb[2];
long long unsigned xr,rj;

void povecaj(){
    int i=0;
    while( bst[i]){ bst[i]=0; ++i;}
    bst[i]=1;
}


int main(){
    ifstream fin("dsh.in");
    ofstream fout("dsh.out");
    fin>>t;
    for(int tt=0; tt<t; ++tt){
        fin>>n;
        for (int i=0; i<n; ++i){
            fin>>a[i];
        }
        rj=0;
        fout<<"Case #"<<tt+1<<": ";
        bst.reset(); zb[0]=zb[1]=0;
        for (int i=0; i<(1<<(n+1)); ++i){
                zb[0]=zb[1]=0;
                for (int j=0; j<n; ++j){
                    zb[bst[j]]^=a[j];
                }
                    //cout<<"Z "<<zb[0]<<" "<<zb[1]<<endl;
                if (zb[0]==zb[1]){
                    //cout<<"Z "<<zb[0]<<" "<<zb[1]<<endl;
                    zb[0]=zb[1]=0;
                    for (int j=0; j<n; ++j){
                        zb[bst[j]]+=a[j];
                    }
                    //cout<<"B "<<zb[0]<<" "<<zb[1]<<endl;
                    if (zb[0]&&zb[1])
                    rj=(int) max((long long unsigned) rj,max(zb[0],zb[1]));
                }
                /*for (int j=0; j<n; ++j){
                cout<<bst[j]<<" "; } cout<<endl;*/
                povecaj();
        }
        if (rj) fout<<rj<<endl;
        else
        fout<<"NO"<<endl;
    }


    return 0;
}
