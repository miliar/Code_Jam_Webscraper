#include<iostream>
#include<stdio.h>
#include<fstream>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>

#define LSIZE      16
#define STRSIZE    1000
#define  DSIZE     5000
using namespace std;

char  d[STRSIZE];
vector <string> a;
int L,D,N;

int findcount (int i, int pos, int ub, int lb);

int main(int argc, char* argv[])
{
    int i;
    cin>>L>>D>>N;
    
    for(i=0;i<D;i++)
    {
             cin>>d;
             a.push_back(d);
    }
    sort(a.begin(),a.end());
    
    for(i=0;i<N;i++)
    {
            cin>>d;
            cout<<"Case #"<<i+1<<": ";
            cout<<findcount(0,0,D-1,0)<<endl;
    }
    return 1;
}

int findcount (int i, int pos, int ub, int lb)
{
    int j,k,l,c=0;
    if(d[i]=='\0' && ub>=lb)
                  return ub-lb +1;
    if(d[i] =='\0')
                   return 0;
    if(d[i]=='(')
    {
                      l=i+1;
                      while(d[l]!=')')
                                      l++;
                      
                      i++;
                      while(i<l)
                      {
                               for(j=lb;j<=ub;j++)
                                                  if(a[j][pos] == d[i])
                                                               break;                  
                               if(j==ub+1)
                               {
                                           i++;
                                           continue;
                               }
                               for(k=j;k<=ub;k++)
                                              if(a[k][pos] != d[i])
                                                           break;
                               c= c + findcount(l+1,pos+1,k-1,j);
                               i++;
                      }
                      return c;
    }
    else
    {
                      for(j=lb;j<=ub;j++)
                                                  if(a[j][pos] == d[i])
                                                               break;                  
                      if(j==ub+1)
                                          return 0;
                      for(k=j;k<=ub;k++)
                                              if(a[k][pos] != d[i])
                                                           break;
                      return findcount(i+1,pos+1,k-1,j);
    }
}
