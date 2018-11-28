#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

char s[500];
int tc;
int hash[500];
int main(){
  scanf("%d\n",&tc);   
  for (int i = 1; i <= tc; i++){
      gets(s);
      memset(hash,-1,sizeof(hash));
      int ada = -1;
      for (int j = 0; s[j]; j++){
        if (j == 0){ada++;hash[s[j]-'0'] = 1; continue;} 
        if (hash[s[j]-'0'] > -1) continue;
        ada++;
        
        if (ada == 1) hash[s[j]-'0'] = 0;
        else {hash[s[j]-'0'] = ada;}
      }    
      int basis = ada+1;
      if (basis == 1) basis++;
      int lena = strlen(s);
      int pos = 0;
      unsigned long long hasil = (long long) 0;
      for (int j = lena-1; j >= 0; j--){
          unsigned long long kali = 1;
          for (int k = 1; k <= pos; k++){
              kali *= (unsigned long long) basis;    
          }
          pos++;
          hasil += ((unsigned long long) hash[s[j]-'0'] * kali);
      }
      cout<<"Case #"<<i<<": "<<hasil<<endl;

  }
}
