#include<fstream>
#include<iostream>
using namespace std;
int main(){
  fstream f("park.in",ios::in),g("park.out",ios::out);
  long r,k,*gr;int n,t;
  f>>t;
  for(int c=1;c<=t;c++){
    f>>r>>k>>n;
    gr=new long[n];
    for(int i=0;i<n;i++)f>>gr[i];
    int p=0;long st=0;
    while(r--){
      long s=0;int m=0;
      while(s+gr[p]<=k&&m<n){
	s+=gr[p++];
	p=p%n;
	m++;
      }
      st+=s;
    }
    g<<"Case #"<<c<<": "<<st<<endl;
  }
  return 0;
}
