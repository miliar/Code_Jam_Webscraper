#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int main(){
  int T;
  cin>>T;
  unsigned int N;
  unsigned int K;
  int number=1;
  while(T--){
    string ans;
    cin>>N>>K;
    bool can=false;
    if(((K-((unsigned int)pow(2,N)-1))%((unsigned int)pow(2,N)))==0){
      can=true;
    }   
    if(can)ans="ON";
    else ans="OFF";
     cout<<"Case #"<<number<<": "<<ans<<endl;
     number++;
  }
  
  return 0;
}
