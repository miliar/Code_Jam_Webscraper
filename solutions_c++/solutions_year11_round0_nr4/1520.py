#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;


int main(){
  int tc;
  cin>>tc;
  int caseno=1;
  
  while(tc--){
    int N;
    cin>>N;
    vector<int> myvector;
    for(int i=0;i<N;i++){
      int temp;
      cin>>temp;
      myvector.push_back(temp);
    }
    vector<int> myvector1(myvector);
    sort(myvector.begin(),myvector.end());
    int fixed = 0;
    for(int i=0;i<N;i++){
      if(myvector[i]==myvector1[i]) fixed++;
    }
    printf("Case #%d: %f\n",caseno,(float)N-fixed);
    //cout<<"Case #"<<caseno<<": "<<N-fixed<<endl;
    caseno++;
  }
}
