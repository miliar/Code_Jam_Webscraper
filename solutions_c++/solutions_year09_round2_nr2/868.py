#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
  }

int t,n,k;char T[25];
string s;

int main(int argc, char *argv[])
{
    int ol,ne;
    scanf("%d",&t);
    s=getLine();
    for(int i=1;i<=t;i++)
    {
          
     s=getLine();
     int ile=s.length();
     for(int x=0;x<s.length();x++)
     T[x]=s[x];
     ol=T[0];
     next_permutation( T,T+ile);
     ne=T[0];
     char ch=T[0]; int czy=1;
     for(int x=0;x<s.length();x++)
     if(T[0]!=T[x])czy=0;
     if(ne<ol || czy )
     {
     sort(T,T+n); 
     if(T[0]=='0')
     {
     int i=0;
     while(T[i]=='0')i++; 
   //  cout<<i;
     swap(T[i],T[0]);
   //  sort(T,T+n); 
     }
     printf("Case #%d: ",i);
     printf("%c",T[0]);
     printf("0");
     for(int i=1;i<ile;i++)
     printf("%c",T[i]);
     printf("\n");
     
     
            
     }
     else
     {
      
      
            
    printf("Case #%d: ",i);
    for(int i=0;i<ile;i++)
    printf("%c",T[i]);
    printf("\n");
    
    }
         
    }
    
    
    
    
  //  system("PAUSE");
    return 0;
}
