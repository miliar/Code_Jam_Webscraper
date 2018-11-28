#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
 int t,cas=1;
 cin>>t;
 while(t--) 
 {
  int w,h;
  int cont=0;
  cin>>h>>w;
  vector<string> A;
  string tmp;
  for(int j=0; j<h; j++){
   cin>>tmp;
   A.push_back(tmp);
  }

  for(int j=0; j<h; j++){
   for(int i=0; i<A[j].length(); i++)
    if(A[j][i]=='#')
     cont++;
  }
  int temp=0;
  if(cont%4!=0)
   printf("Case #%d:\nImpossible\n", cas++);
  else{
   for(int j=0; j<h; j++){
    int tk=A[j].length();
    for(int i=0; i<tk; i++)
     if(A[j][i]=='#'){
      if(i+1<tk && j+1<h && A[j][i+1]=='#' && A[j+1][i]=='#' && A[j+1][i+1]=='#')
      {
       A[j][i]='/';
       A[j][i+1]='\\';
       A[j+1][i]='\\';
       A[j+1][i+1]='/';
      }
      else
       temp=1; 
     }
   }
   if(temp)
   printf("Case #%d:\nImpossible\n", cas++);
   else{
    printf("Case #%d:\n", cas++);
    for(int j=0; j<h; j++){
     for(int i=0; i<A[j].length(); i++)
      printf("%c",A[j][i]);
     printf("\n");
    }
   }
  }   
 }
}
