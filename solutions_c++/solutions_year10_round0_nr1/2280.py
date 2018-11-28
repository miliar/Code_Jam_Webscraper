#include <iostream>

using namespace std;

int
main()
{
  int t;
  cin>>t;

  for(int i = 0; i < t; i++){
    int n,k;
    cin>>n>>k;

    int b = ((k<<(32-n))>>(32-n));
    

    cout<<"Case #"<<i+1<<": "<<(((b & (~0>>(32-n))) == (~0>>(32-n)) )?"ON":"OFF")<<endl;


  }

}
