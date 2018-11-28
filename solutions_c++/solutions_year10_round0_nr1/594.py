#include<iostream>

using namespace std;

int main(){

  int num_cases;
  
  cin>>num_cases;
  
  for (int c=1; c<=num_cases; c++) {
    long long n,k;
    
    cin>>n>>k;
    bool on=true;
    for (int i=1; i<=n; i++) { 
  	on = on && ((k%2));
  	k/=2;
  }
  
  cout<<"Case #"<<c<<": ";
  if (on) 
  	cout<<"ON"<<endl;
  else
  	cout<<"OFF"<<endl;
  }
  return 0;
}