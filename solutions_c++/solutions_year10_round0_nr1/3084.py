#include<iostream>
#include<fstream>
using namespace std;


int main() {

  int t;
  cin>>t;

  std::fstream FS( "output", std::ios::out );
  if( FS.fail() ) return 1;

  long n,k;
  for(int o=0; o<t; o++) {
    cin>>n>>k;


    bool flag  = true;
    for(int i=0; i<n; i++) {
      //cout<<(k&(1<<i))<<" "<<(1<<i)<<endl;
      if( !(k&(1<<i)) )
	flag = false;
    }

    //cout<<c<<" "<<k<<endl;
    if(flag) {
      FS<<"Case #"<<o+1<<": ON"<<endl;
    }else{
      FS<<"Case #"<<o+1<<": OFF"<<endl;

    }
  }

}
