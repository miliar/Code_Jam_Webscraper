#include <iostream>

using namespace std;

int answer();

const int infinity=999999999,bad=-1;

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": ";
    int a=answer();
    if(a==bad)
      cout<<"NO\n";
    else
      cout<<a<<'\n';
  }
}

int answer(){
  int candies,smallest=infinity,sum=0,xor_sum=0;
  cin>>candies;
  for(int i=0;i<candies;i++){
    int candy;
    cin>>candy;
    smallest=min(candy,smallest);
    xor_sum^=candy;
    sum+=candy;
  }
  if(xor_sum!=0)
    return bad;
  return sum-smallest;
}
