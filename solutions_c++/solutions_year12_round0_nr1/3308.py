#include<iostream>
#include<string>
#include<iostream>
using namespace std;

int main(){
  char data[26]={
    'y','h','e','s','o',//a,b,c,d,e
    'c','v','x','d','u',//f,g,h,i,j
    'i','g','l','b','k',//k,l,m,n,o
    'r','z','t','n','w',//p,*q,r,s,t
    'j','p','f','m','a',//*u,v,w,x,y
    'q'};//*z;
  //non-use;(q,u,z)->(j,q,z);

  int T;cin>>T;
  string s;getline(cin,s);
  for(int t=0;t<T;t++){
    string s;
    getline(cin,s);
    for(int i=0;i<s.size();i++){
      if(s[i]>='a' && s[i]<='z')s[i]=data[(int)(s[i]-'a')];
    }
    string g="Case #";
    int k=t+1;
    if(k<10)g+=(char)(k+'0');else{g+=(char)(k/10+'0');g+=(char)(k%10+'0');}
    g+=": ";
    cout<<g+s<<endl;
  }
  return 0;
}
