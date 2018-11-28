#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>


using namespace std;

#define MAXS 100
#define MAXQ 1000

string engines[MAXS];
string queries[MAXQ];
int S,Q;

int funk(int dist, int last)
{
    int j,k,d;
    d=0;
    
    for(j=0;j<S;j++)
    {
     for(k=dist;k<Q && engines[j].compare(queries[k]);k++);
     if(k>=Q && j!=last)
     {
          return 0;
     }
     else if(k>d && j!=last)
     {
      d = k;
      last = j;
     }    
    }

    if (Q-d<S)
    {
       return 1;
    
    }
    else
    {
      return funk(d,last)+1;
    }
}

int main(void)
{
 int N,i,j,k,Y,maior;
 string s;
 
 scanf("%d\n",&N);
  
 for(i=0; i<N; i++)
 {
  scanf("%d\n",&S);
  
  for(j=0;j<S;j++)
  {
   getline(cin, engines[j]);
  }
  
  scanf("%d\n",&Q);
 
  for(k=0;k<Q;k++)
  {
   getline( cin, queries[k]);
  } 
 
  Y = funk(0,-1);
  cout<<"Case #"<<i+1<<": "<<Y<<endl; 
 } 
 
 return 0;
}
