#include <iostream>
#include <string>
#include <set>
using namespace std;
set<string> slow;
int L,D,N;

int policz(string& s, string pom, int p){
//cout<<p<<endl;
if (p==s.length()){
  //cout<<pom<<endl;
  if (slow.find(pom)!=slow.end())
    return 1;
  else 
    return 0;
}
else {
  if (s[p]!='('){
   if (slow.find(pom+s[p])!=slow.end())
     return policz(s,pom+s[p],p+1);
   else
     return 0;
  }
  else{
    int sum=0,k=p;
    while(s[k]!=')')
      k++;
    //cout<<k<<endl;
    p++;
    while(p<k){
      if (slow.find(pom+s[p])!=slow.end())
        sum+=policz(s,pom+s[p],k+1);
      p++;
    }
    return sum;
  }
}
}

int main(){
string s;
int i,k;
cin>>L;
cin>>D;
cin>>N;
for(i=0;i<D;i++)
  {
  cin>>s;
  for(int k=1;k<=L;k++)
    slow.insert(string(s,0,k));
  }
for(i=0;i<N;i++)
  {
  cin>>s;
  cout<<"Case #"<<i+1<<": "<<policz(s,"",0)<<endl;;
  }
}