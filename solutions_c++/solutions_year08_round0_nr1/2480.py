#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
 struct searcheng
 {
  char name[100];
  int token;
 }se[100];

 char q[1000][100];
 int qn,sen;

 void makenull();
 int search(char *query);

 main()
 {  int i,k,sw=0,no;
  cin>>no;
 for(k=0;k<no;k++)
 {
	sw=0;
  cin>>sen;
   for(i=0;i<sen;i++)
  cin>>se[i].name;
    cin>>qn;
  for(i=0;i<qn;i++)
   cin>>q[i];
  makenull();
  for(i=0;i<qn;i++)
   {
     if(search(q[i])==1)
      {
       makenull();
       i--;
       sw++;
      }
   }
  cout<<"Case #"<<k+1<<": "<<sw<<endl;
 }
}
 int search(char *query)
 {
  int i;
  for(i=0;i<sen;i++)
  { if(strcmp(query,se[i].name)==0)
    { se[i].token=1;
      break;
    }
  }
  for(i=0;i<sen;i++)
  { if(se[i].token!=1)
    break;
  }
  if(i==sen)
   return 1;
  else
   return 0;
 }

 void makenull()
  {
  int i;
  for(i=0;i<sen;i++)
  se[i].token=0;
  }

