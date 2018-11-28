#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <utility>
#include <climits>
#include <cfloat>

using namespace std;
#define readint(n) scanf("%d",&n);
#define readll(n) scanf("%lld",&n);
#define readf(n) scanf("%f",&n);
#define readd(n) scanf("%lf",&n);
#define readstr(s) scanf("%s",&s);
int pabs(int n){return (n>0?n:-n);}

bool what(int a,int b){
  char ar[20];
  sprintf(ar,"%d",a);
  string s1(ar);
  sprintf(ar,"%d",b);
  string s2(ar);
  if(s1.length()!=s2.length())return false;

  for(int i=0;i<s2.length();i++){
    if(s2[i]==s1[0]){
      string s11,s12,s21,s22;
      s11=s1.substr(0,s2.length()-i);
      s12=s1.substr(s2.length()-i,s1.length());

      s21=s2.substr(0,i);
      s22=s2.substr(i,s2.length());
      //cout<<s11<<"  "<<s12<<endl;
      //cout<<s21<<"  "<<s22<<endl;
      if(s11.compare(s22)==0  && s12.compare(s21)==0)return true;
    }
  }
  return false;
}

int main(){/*
  int a,b;
  while(1){
    readint(a);
    readint(b);
    if(what(a,b))cout<<"yes!!\n";
    else cout<<"no\n";
  }
  return 0;
  }
*/
  int t;
  int a,b;
  readint(t);
  for(int ii=1;ii<=t;ii++){
    readint(a);
    readint(b);
    long long int cnt=0;
    for(int i=a;i<=b;i++){
      for(int j=i;j<=b;j++){
	if(i==j)continue;
	if(what(i,j)){
	  cnt++;
	}
      }
    }
    printf("Case #%d: %lld\n",ii,cnt);
  }
  return 0;
}
