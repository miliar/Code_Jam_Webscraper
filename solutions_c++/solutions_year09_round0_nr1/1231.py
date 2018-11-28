#include <iostream>
#include <cstdio>
using namespace std;

int D,L,N;
int i,ii,iii,ans;
bool test;
bool ct[15][26];
char data[5000][15];
char tempbgt[100];
char temp;


int main(){

    cin >> L;
    cin >> D;
    cin >> N;

    for(i=0;i<D;i++)
     scanf("%s",data[i]);
    
    for(i=0;i<N;i++)
    {
     ans = 0;
     for(ii=0;ii<L;ii++)
     {
      for(iii=0;iii<26;iii++) ct[ii][iii] = false;
      
      cin >> temp;
      
      if(temp!='(') ct[ii][temp-'a'] = true;
      else
      {
          cin >> temp;
          while(temp!=')')
          {
          ct[ii][temp-'a'] = true;
          cin >> temp;
          }
      }
      
     }
     gets(tempbgt);
     
     for(ii=0;ii<D;ii++)
     {
      test = true;
      for(iii=0;iii<L;iii++) if(!ct[iii][data[ii][iii]-'a']) test = false;
      
      if(test) ans++;
     
     }
     
     printf("Case #%d: %d\n",i+1,ans);
     
    }
    

}
