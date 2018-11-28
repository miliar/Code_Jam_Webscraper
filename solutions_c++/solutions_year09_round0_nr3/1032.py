#include <fstream>
#include <iostream>
using namespace std;


int main(){
    ifstream in("C-large.in");
    ofstream out("C-large.out");
    string p, s;
    int n, t=0, i, j;
                  int kk;

    p=" welcome to code jam";
    in>>n;
    int cant[50];
    cant[0]=1;
    getline(in, s);
    while (t<n){
          for (i=0; i<50; i++)cant[i]=0;
          cant[0]=1;
          getline(in, s);

          for (i=0; i<s.length(); i++){
              //cout<<cant[1]<<endl;
              for (j=p.length()-1; j>0; j--){
                  if (s[i]==p[j]){cant[j]+=cant[j-1]; cant[j]=cant[j]%10000;}
                  
                  }
              }
          out<<"Case #"<<t+1<<": ";
          kk=1000;
          int res=cant[p.length()-1];
          while (res<kk && kk!=1){out<<'0'; kk/=10;}
          out<<res<<endl;
          t++;
          }
    }
