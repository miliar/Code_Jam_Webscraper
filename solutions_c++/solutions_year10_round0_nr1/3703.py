
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cassert>
#include<fstream>
#include<iostream>
#include<algorithm>
#define fr(i,n) for(int i=0;i<n;++i)
#define For(i,a,b) for(int i=a;i<b;++i)
#define Rev(i,a,b) for(int i=a;i>=b;--i)

using namespace std;

int n;
int k;
int t;
int no;
int pw[35];

int gcd(int a, int b) {
  int t;
  while (b != 0) {
    t = b;
    b = a % b;
    a = t;
  }
  return a;
}


int main(){
    ifstream fin;
    ofstream fout;
    fin.open("in2.in");
    if(!fin){
        cout<<"\nError in opening file ";
        return 0;     
    }
    fout.open("o.in");
    if(!fout){
        cout<<"\nError in output file ";
        return 0;       
    }
    fin>>t;
    no=1;
    pw[1]=2;
    For(i,2,31){
        pw[i]=pw[i-1]*2;     
    }
    while(t--){
         fin>>n>>k;
         if(pw[n]>k+1){
              fout<<"\nCase #"<<no<<": OFF";   
         }
         else if(pw[n]==k+1){
              fout<<"\nCase #"<<no<<": ON";
         }
         else{
             int ans=gcd(k+1,pw[n]);
             if(ans==pw[n]){  
                 fout<<"\nCase #"<<no<<": ON";     
             } 
             else{
                 fout<<"\nCase #"<<no<<": OFF";
             }
         }     
         ++no;  
    }
    fin.close();
    fout.close();
}
