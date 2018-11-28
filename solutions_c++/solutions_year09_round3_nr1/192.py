#include <iostream>
#include<iostream>
using namespace std;

int pods;
string s1;
int pom[256];

int policz(){
  int i,p;
  for(i=0;i<256;i++)
    pom[i]=0;
  p=1;
  pom[s1[0]]=1;
  for(i=1;i<s1.length();i++)
    if (pom[s1[i]]==0){
      p++;
      pom[s1[i]]=1;
    }
return p;
}

long long wynik(){
int i;
long long wyn=0, pot=1;
for(i=s1.length()-1;i>=0;i--){
  wyn+=pot*pom[s1[i]];
  pot*=pods;
}
return wyn;
}

int main(){
int i,j,n,k,p,N;
long long wyn;
cin>>N;
for(i=1;i<=N;i++){
  cin>>s1;
  pods=policz();
  if (pods==1)
    pods++;
  for(j=0;j<256;j++)
    pom[j]=-1;
  pom[s1[0]]=1;
  for(j=1;(j<s1.length())&&(s1[j]==s1[0]);j++);
  if (j==s1.length()){
    wyn=wynik();
  }
  else{
    pom[s1[j]]=0;
    k=2;
    j++;
    for(j=1;j<s1.length();j++)
      if (pom[s1[j]]==-1){
        pom[s1[j]]=k;
        k++;
      }
    wyn=wynik();
  }
  //cout<<pom['0']<<" "<<pom['1']<<endl;
  cout<<"Case #"<<i<<": "<<wyn<<endl;
}
}