#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
using namespace std;
int to(char c){
  if(c==' ') return 26;
  else return c-'a';
}

int main(){
 int n; cin>>n;
 string cad;getline(cin,cad);
 for(int t=0;t<n;t++){
  getline(cin,cad);
  long long mapa[500][27][3];
  memset(mapa,0,sizeof mapa);
  
  int sz=cad.size();
  for(int i=sz-1;i>=0;i--) if(cad[i]=='m')mapa[i][to('m')][1]++;
  
  for(int i=sz-1;i>=0;i--) if(cad[i]=='a')
    for(int j=i+1;j<sz;j++) mapa[i][0][0]+=mapa[j][to('m')][1]%10000;
  
  for(int i=sz-1;i>=0;i--) if(cad[i]=='j')
    for(int j=i+1;j<sz;j++) mapa[i][to('j')][0]+=mapa[j][0][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]==' ')
    for(int j=i+1;j<sz;j++) mapa[i][to(' ')][2]+=mapa[j][to('j')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='e')
    for(int j=i+1;j<sz;j++) mapa[i][to('e')][2]+=mapa[j][to(' ')][2]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='d')
    for(int j=i+1;j<sz;j++) mapa[i][to('d')][0]+=mapa[j][to('e')][2]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='o')
    for(int j=i+1;j<sz;j++) mapa[i][to('o')][2]+=mapa[j][to('d')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='c')
    for(int j=i+1;j<sz;j++) mapa[i][to('c')][1]+=mapa[j][to('o')][2]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]==' ')
    for(int j=i+1;j<sz;j++) mapa[i][to(' ')][1]+=mapa[j][to('c')][1]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='o')
    for(int j=i+1;j<sz;j++) mapa[i][to('o')][1]+=mapa[j][to(' ')][1]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='t')
    for(int j=i+1;j<sz;j++) mapa[i][to('t')][0]+=mapa[j][to('o')][1]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]==' ')
    for(int j=i+1;j<sz;j++) mapa[i][to(' ')][0]+=mapa[j][to('t')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='e')
    for(int j=i+1;j<sz;j++) mapa[i][to('e')][1]+=mapa[j][to(' ')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='m')
    for(int j=i+1;j<sz;j++) mapa[i][to('m')][0]+=mapa[j][to('e')][1]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='o')
    for(int j=i+1;j<sz;j++) mapa[i][to('o')][0]+=mapa[j][to('m')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='c')
    for(int j=i+1;j<sz;j++) mapa[i][to('c')][0]+=mapa[j][to('o')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='l')
    for(int j=i+1;j<sz;j++) mapa[i][to('l')][0]+=mapa[j][to('c')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='e')
    for(int j=i+1;j<sz;j++) mapa[i][to('e')][0]+=mapa[j][to('l')][0]%10000;
    
  for(int i=sz-1;i>=0;i--) if(cad[i]=='w')
    for(int j=i+1;j<sz;j++) mapa[i][to('w')][0]+=mapa[j][to('e')][0]%10000;
  
  long long conta=0;
  for(int i=0;i<sz;i++) conta+=mapa[i][to('w')][0]%10000;
  
  printf("Case #%d: %04d\n",t+1,int(conta%10000));
 }
}