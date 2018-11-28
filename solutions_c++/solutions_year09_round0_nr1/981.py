#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool match(const string&s,const string&p)
{
 int j=0;
 for(int i=0;i<p.size();){
  if(p[i]=='('){
   i++;
   bool t=false;
   while(p[i]!=')'){
    if(s[j]==p[i])
     t=true;
    i++;
   }
   i++;
   j++;
   if(!t)
    return false;
  }
  else{
   if(p[i]!=s[j])
    return false;
   i++;
   j++;
  }
 }
 return true;
}

int main(void)
{
 int L,D,N;
 (cin>>L>>D>>N);{
  vector<string>dic(D);
  for(int i=0;i<D;i++){
   cin>>dic[i];
  }
  for(int i=0;i<N;i++){
   string str;
   cin>>str;
   int c=0;
   for(int j=0;j<D;j++){
    if(match(dic[j],str))
     c++;
   }
   printf("Case #%d: %d\n",i+1,c);
  }
 }
 return 0;
}
