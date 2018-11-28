#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;

int main( void )
{
 int T;
 cin>>T;
 for(int X=1;X<=T;++X){
  string your;
  cin >> your;
  set<char> all;
  for(int i=0;i<your.size();i++)
   all.insert(your[i]);
  int base=all.size();
  if(base==1)base=2;
  long long belong=0;
  vector<int> to(256,-1);
  int us=0;
  for(int i=0;i<your.size();i++){
   if(i==0)to[your[i]]=1;
   else if(to[your[i]]<0){to[your[i]]=us;if(us==0)us=2;else++us;}
   belong=belong*base+to[your[i]];
  }
  printf("Case #%d: %lld\n",X,belong);
 }
}
