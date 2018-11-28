#include<iostream>
#include<stdio.h>
using namespace std;
 char google[30]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{ char G[35][110];
  char t;
  int k=0,i=0,j=0, index,T;
 
  cin>>T;
  for(k=0;k<=T;k++)
  { for(i=0;;i++)
   {   cin.get(G[k][i]);
	   
       if(G[k][i]==10)
   break;
   }
  G[k][++i]='\n';
  }
  
  for(k=0;k<=T;k++)
  for(j=0;G[k][j]!='\n';j++)
  { if(G[k][j]==' ')
    continue;
    t=G[k][j];
    index=(t-97);
    G[k][j]=google[index];
    }
    
  for(k=0;k<T;k++)
  { cout<<"Case #"<<k+1<<": ";
  for(i=0;;i++)
  { cout<<G[k+1][i];
    if(G[k+1][i]=='\n')
    break;  
   }  
  }
 
  

  return 0;
}
