
#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<list>
#include<algorithm>

using namespace::std;

int main(){
  
  int T;
  
  cin>>T;
  
  for(int t=0;t<T;t++){
    int N;
    
    cin>>N;
    
    vector<int> candy;
    int sum=0;
    int all=0;
    int min=10000000;
    for(int n=0;n<N;n++){
      int temp;
      
      cin>>temp;
      sum=sum^temp;
      all=all+temp;
      
      if(temp<min)
	min=temp;

      candy.push_back(temp);

    }

    if(sum!=0){
      cout<<"Case #"<<t+1<<": NO"<<endl;
    }else{
      cout<<"Case #"<<t+1<<": "<<all-min<<endl;
    }
  }

  
  return 0;
  
}
