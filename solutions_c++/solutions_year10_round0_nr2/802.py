#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;


int hcf(int a,int b)
{
    int r=0;
    while(b!=0)
        {
        r=a%b;
        a=b;
        b=r;
        }
    return(a);
} 


int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
   freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout); 
//    freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout); 
//    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int C;
    while (scanf ("%d",&C)!=EOF)
    {
          for (int count=1;count<=C;count++)
          {
              int n;
              cin>>n;
              vector <int> str(n);
              vector <int> num(2);
              for (int i=0;i<n;i++)
                  cin>>str[i];
              sort (str.begin(),str.end());
              for (int i=0;i<n-1;++i)
              {
                  if (i+1<n)
                  {
                     num[i]=str[i+1]-str[i];          
                  }    
              }
              int res;
              bool flag=false;
              if (n==2)
              {
                 res=num[0]-(str[0]%num[0]);
                 if (str[0]%num[0]==0)
                    flag=true;
              }
              else
              {
                  res=hcf(num[0],num[1])-str[0]%hcf(num[0],num[1]);
                  if (str[0]%hcf(num[0],num[1])==0)
                    flag=true;
              }
              if (flag)
                 res=0;
              cout<<"Case #"<<count<<": "<<res<<endl;    
          }      
    }
    return 0; 
} 



