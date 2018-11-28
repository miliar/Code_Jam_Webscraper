#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <cstring>

using namespace std;

int main(int argc, char* argv[]){
  int T;
  cin>>T;
  int cas=1;
  while(T--){
    int N,S,p,t[100];
    cin>>N>>S>>p;
    int answer = 0;
    for(int i=0;i<N;i++){      
      cin>>t[i];
    }
    if(p>0){
      for(int i=0;i<N;i++){
        if((t[i]+2)/p >=3 || t[i]/p >=3){
          answer++;
        }
        else{
          if(S>0 && t[i]>0){
            if((t[i]+4)/p >=3){
              answer++;S--;
            }
          }
        }
      }
    }
    else{
      answer = N;
    }
    cout<<"Case #"<<cas<<": "<<answer<<endl;
    cas++;
  }
  return 0;
}
