#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
using namespace std;
int rec (vector <int> zeros, vector <int> res, int i){
    if (i==res.size()){
       int a1=0;
       int b1=0;
       int real=0;
       int uns=0;
       for (int is=0; is<res.size(); is++){
           if (zeros[is]==1){
               b1=b1 ^ res[is];
               real+=res[is];
           }
           else {
                a1=a1 ^ res[is];
                uns++;
           }
       }
       if (uns==0) return -1;
       if (a1==b1) return real;
       else return -1;
    }
    else {
         zeros[i]=0;
         int t=rec(zeros, res,i+1);
         zeros[i]=1;
         int k=rec(zeros,res,i+1);
         return max(t,k);
    }
}
int main (){
   ifstream fin ("C-small-attempt0.in");
    ofstream fout ("C-small-attempt0.out");
    int tu=(5 ^6) ^3;
    //cout <<tu<<endl;
    int T;
    fin >>T;
    //cout <<T<<endl;
    for (int i=1; i<=T; i++){
        int C;
        fin >>C;
        vector <int> res (C);
        vector <int> zeros(C,0);
        for (int k=0; k<C; k++){
            fin >>res[k];
        }
        int resp=rec(zeros,res,0);
        fout <<"Case #"<<i<<": ";
        if (resp==-1) fout <<"NO"<<endl;
        else fout <<resp<<endl;
    }
  //  system ("pause");
}
