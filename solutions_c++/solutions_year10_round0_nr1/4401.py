#include<fstream>
#include<iostream>
using namespace std;
int main(){
  fstream f("snapper.in",ios::in),g("snapper.out",ios::out);
  int t,n,k,*s;
  f>>t;
  for(int c=1;c<=t;c++){
    f>>n>>k;
    s=new int[n];
    for(int i=0;i<n;i++)s[i]=0;
    for(int i=1;i<=k;i++){
      int j=0;
      while(s[j]&&j<n){s[j]=!s[j];j++;}
      if(j<n)s[j]=!s[j];
    }
    int j=0;while(s[j]&&j<n)j++;
    g<<"Case #"<<c<<": ";
    if(j==n)g<<"ON"<<endl;
    else g<<"OFF"<<endl;
  }
  return 0;
}
