#include <iostream>
#include <fstream>
using namespace std;

int cor(char x){
    if (x=='Q') return 0;
    else if(x=='W')    return 1;
    else if(x=='E')    return 2;
    else if(x=='R')    return 3;
    else if(x=='A')    return 4;
    else if(x=='S')    return 5;
    else if(x=='D')    return 6;
    else if(x=='F')    return 7;
    return -1;
}

int main(){
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    char invo[102];
    char fus[10][10];
    int res[10][10];
    int cases=0;
    int a,b,c,d;
    int ctr=0;
    char x,y,z;
    fin>>cases;
    for(int i=1;i<=cases;i++){
            cout<<cases<<endl;
            for(int m=0;m<9;m++){
                    for(int l=0;l<9;l++){
                            fus[m][l]=0;res[m][l]=0;}}
            fin>>a;
            for(;a>0;a--){ 
                          fin>>x>>y>>z;
                          d=cor(x);
                          b=cor(y);
                          c=cor(z);
                          if (d<0){     fus[b][c]=x;fus[c][b]=x;}
                          else if(b<0){ fus[d][c]=y;fus[c][d]=y;}
                          else if(c<0){ fus[d][b]=z;fus[b][d]=z;}
            }
            fin>>a;
            for(;a>0;a--){
                          fin>>x>>y;
                          d=cor(x);
                          b=cor(y);
                          res[d][b]=1;
                          res[b][d]=1;
            }
            fin>>a;
            int dex=0;
            for(int j=0;j<a;j++){
                          fin>>x;
                          ctr=0;
                          if(dex==0){
                                   invo[0]=x;
                                   dex++;
                          } else {
                                 invo[dex]=x;
                                 dex++;
                                 b=cor(invo[dex-2]);
                                 c=cor(x);
                                 if((b>=0)&&(fus[b][c]>0)){

                                                 invo[dex-2]=fus[b][c];
                                                 dex--;
                                                 ctr=1;
                                 } else {
                                                 for(int k=0;k<dex;k++){
                                                         b=cor(invo[k]);
                                                         if(b>=0){
                                                             if(res[b][c]>0){
                                                                             dex=0;
                                                                             ctr=1;
                                                             }
                                                         }
                                                 }
                                 }
                          }   
            }
            int m=0;
            fout<<"Case #"<<i<<": [";
            for(m=0;m<dex-1;m++){
                    fout<<invo[m]<<", "; }
            if(m==(dex-1))
                          fout<<invo[m];
            fout<<"]";
            fout<<endl;    
    }
    return 0;
}
