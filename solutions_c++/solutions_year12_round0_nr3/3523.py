#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int foo2(int n,string A,string B){
  int res=0;
  string x="";
  while(n>0){x+=(char)(n%10+'0');n/=10;}
  reverse(x.begin(),x.end());
  for(int i=0;i<x.size();i++){
    string y="";
    y+=x.substr(i);
    y+=x.substr(0,i);
    if(x<y && y<=B){res++;}
  }
  return res;
}

int foo(string A, string B){
  if(A.size()==1)return 0;
  int C=0;int D=0;
  for(int i=0;i<A.size();i++)C=C*10+(char)(A[i]-'0');
  for(int i=0;i<B.size();i++)D=D*10+(char)(B[i]-'0');
  int res=0;
  for(int n=C;n<=D;n++){
    res+=foo2(n,A,B);
  }
  return res;
}

int main(){
  int t=0;string A;cin>>A;
  string B;
  while(cin>>A>>B){
      t++;
      int r=foo(A,B);
      string g="Case #";
      if(t==100)g+="100";
      else if(t<10)g+=(char)(t+'0');
      else{g+=(char)(t/10+'0');g+=(char)(t%10+'0');}
      g+=": ";
      cout<<g<<r<<endl;
  }
  return 0;
}
