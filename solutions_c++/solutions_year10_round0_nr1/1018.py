#include<iostream>
#include<algorithm>
#include<string.h>
#include <vector>

using namespace std;


int main(){

  int T;
  cin >> T;

  for(int i=0; i<T; ++i){
    int N,K,B,C;
    int ans;
    B=1;

    cin >> N >> K;

    B=B<< N;
    
    ans=K%B;

    C=1;

    C=C << N;
    C=C-1;
    
   

    if( ans == C){
      cout << "Case #"<< i+1 <<": " <<"ON" << endl;   
    }else{
       cout << "Case #"<< i+1 <<": " <<"OFF" << endl;
    }
  }
}
