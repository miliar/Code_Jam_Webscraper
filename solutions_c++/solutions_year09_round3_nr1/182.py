#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

long long answer;
long long base;
char tex[70];
int allletter[256];
int texmod[70];
int l1,lettype,i,ii,n;


int main()
{
    cin >> n;ii=1;
    while(n--)
    {
      scanf("%s",tex);
      
      l1 = strlen(tex);
      for(i=0;i<255;i++) allletter[i] = -1;
      lettype = 0;base = 1;answer = 0;
      
      
      for(i=0;i<l1;i++) 
      if(allletter[tex[i]]==-1)
      {allletter[tex[i]] = texmod[i] = lettype; lettype++;}
      else texmod[i] = allletter[tex[i]];
      
      for(i=0;i<l1;i++) {if(texmod[i] == 0) texmod[i] = 1;
      else if(texmod[i] == 1) texmod[i] = 0;}
      
      if(lettype==1) {lettype = 2;}
      
      for(i=l1-1;i>=0;i--)
      {
      answer+= base*texmod[i];
      base*= lettype;
      }
       
      
      cout << "Case #"<< ii << ": "<< answer << endl;
      ii++;
    }
}
