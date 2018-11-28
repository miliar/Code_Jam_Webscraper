#include<iostream>

using namespace std;



int main()
{

  int t,n,i,j;
  int min;
  int d;
  int xr;
  int sum;

  cin>>t;
  j=0;

  while(j++<t){

    min=100000000;
    xr=0;
    sum=0;

    cin>>n;

    for(i=0;i<n;i++){
      cin>>d;
      if(d<min) min=d;
      xr ^= d;
      sum+=d;
    }

    cout<<"Case #"<<j<<": ";
    if(!xr)
      cout<<sum-min<<endl;
    else
      cout<<"NO"<<endl;
  }
  return 0;
}

