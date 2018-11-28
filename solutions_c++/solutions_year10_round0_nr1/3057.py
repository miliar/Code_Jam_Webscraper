#include <iostream>
#include <string>
#include <bitset>
using namespace std;
int main (){
  freopen("A-large.in","rt",stdin);
  freopen("A.in","w",stdout);
  int c;
  cin>>c;
  int m=1;
  while(c--){
  int n,k;
  cin>>n>>k;
  string mystring;
  bitset<100> mybits=k;      
  mystring=mybits.to_string<char,char_traits<char>,allocator<char> >();
  int count=0;
  for(int i=mystring.size()-1;i>mystring.size()-1-n;i--){
          if(mystring[i]=='1')count++;
  }
  if(count==n)cout<<"Case #"<<m<<": ON"<<endl;
  else cout<<"Case #"<<m<<": OFF"<<endl;
  m++;
  }
  return 0;
}
