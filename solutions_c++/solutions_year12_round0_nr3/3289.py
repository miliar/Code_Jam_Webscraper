#include<cstdio>
#include<string>
#include<iostream>
#include<sstream>
using namespace std;
int main(){
  int T;
  scanf("%d",&T);
  for(int z=1;z<=T;z++){
    int i;
    int c=0;
    string a,b;
    cin>>a;
    cin>>b;
    int na,nb;
    stringstream ta,tb;
    ta<<a;ta>>na;
    tb<<b;tb>>nb;
    for(i=na;i<nb;i++){
      string t;
      ta.clear();
      ta<<i;ta>>t;
      string st="";
      st += t;
      st += t;
      for(int k=0;k<t.length();k++){
       int x;
       string sa;
       for(int j=k;j<k+t.length();j++){
          sa+=st[j];
        }
        ta.clear();
        int y;
        ta<<sa;ta>>y;
        if(i<y&&y<=nb&&sa[0]!='0'){
          if(y!=x)
            c++;
          x=y;
        }
      }
    }
  printf("Case #%d: %d\n",z,c);
  }
	return 0;
}
