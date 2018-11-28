#include<cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>
 
using namespace std;
 
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define SZ(x) ((int) (x).size())
#define FE(i,x) for(typedef((x).begin() i=(x).begin();i!=(x).end();i++) 

typedef long long int  int64;
typedef unsigned long long int uint64;
typedef long double ldb;
typedef pair <int, int> pii;
typedef vector<int>vi;
typedef vector<string>vs;
 

 
template <class T> T sqr (T x) {return x * x;}
int main()
{
  FILE *p2=fopen("input.in","r");
  int cases;
  fscanf(p2,"%d",&cases);
  FILE *p=fopen("output2.txt","w");
  
 
  int cs=0;
  while(cases--)
  {
    int n;
    fscanf(p2,"%d",&n);
    int O[1000],B[1000];
    char seq[1000];
    int ans=0,b=0,o=0,s=0;
    while(n--)
    {
     char c;
     int  d;
     fscanf(p2," %c %d",&c,&d);
     if(c=='O')
     {
       O[o++]=d;
       seq[s++]='O';
     }
     else if(c=='B')
     {
       B[b++]=d;
       seq[s++]='B';
     }
     
    }

    int oo=0,bb=0,oldo=1,oldb=1;
    
    for(int i=0;i<s;i++)
    {
        if(seq[i]=='O')
        {
          if(O[oo]>=oldo&&oo<o)
          {
             ans=ans+O[oo]-oldo+1;
             
            
             //printf("1# %d\n",ans);
             if(B[bb]>oldb&&bb<b)
             {
               if(B[bb]-oldb<=O[oo]-oldo+1&&bb<b&&oo<o)
               {
                  oldb=B[bb];
               }
               else if(B[bb]-oldb>O[oo]-oldo+1&&bb<b&&oo<o)
               {
                  oldb+=O[oo]-oldo+1;
               }
              
             }
             else if(B[bb]<oldb&&bb<b)
             {
                if(oldb-B[bb]<=O[oo]-oldo+1&&bb<b&&oo<o)
                {
                   oldb=B[bb];
                }
                else if(oldb-B[bb]>O[oo]-oldo+1&&bb<b&&oo<o)
                {
                   oldb-=O[oo]-oldo+1;
                }
              }
              oldo=O[oo];
              oo++;
           }
           else if(O[oo]<=oldo&&oo<o)
           {
              ans=ans+oldo-O[oo]+1;
             
            
             //printf("2#\n");
             if(B[bb]>oldb&&bb<b)
             {
               if(B[bb]-oldb<=oldo-O[oo]+1&&bb<b&&oo<o)
               {
                  oldb=B[bb];
               }
               else if(B[bb]-oldb>oldo-O[oo]+1&&bb<b&&oo<o)
               {
                  oldb+=oldo-O[oo]+1;
               }
             }
             else if(B[bb]<oldb&&bb<b)
             {
                if(oldb-B[bb]<=oldo-O[oo]+1&&bb<b&&oo<o)
                {
                   oldb=B[bb];
                }
                else if(oldb-B[bb]>oldo-O[oo]+1&&bb<b&&oo<o)
                {
                   oldb-=oldo-O[oo]+1;
                }
              }
            oldo=O[oo];
            oo++;
          }//if

         }//if
         else if(seq[i]=='B')
          {
            if(B[bb]>=oldb&&bb<b)
             {
               ans=ans+B[bb]-oldb+1;
              
             
              //printf("3#\n");
              if(O[oo]>oldo&&oo<o)
              {
               if(O[oo]-oldo<=B[bb]-oldb+1&&bb<b&&oo<o)
               {
                  oldo=O[oo];
               }
               else if(O[oo]-oldo>B[bb]-oldb+1&&bb<b&&oo<o)
               {
                  oldo+=B[bb]-oldb+1;
               }
             }
             else if(O[oo]<oldo&&oo<o)
             {
                if(oldo-O[oo]<=B[bb]-oldb+1&&bb<b&&oo<o)
                {
                   oldo=O[oo];
                }
                else if(oldo-O[oo]>B[bb]-oldb+1&&bb<b&&oo<o)
                {
                   oldo-=B[bb]-oldb+1;
                }
              }
              oldb=B[bb];
              bb++;
           }
           else if(B[bb]<=oldb&&bb<b)
           {
             ans=ans+oldb-B[bb]+1;
             
             
             //printf("4#\n");
             if(O[oo]>oldo&&oo<o)
             {
               if(O[oo]-oldo<=oldb-B[bb]+1&&bb<b&&oo<o)
               {
                  oldo=O[oo];
               }
               else if(O[oo]-oldo>oldb-B[bb]+1&&bb<b&&oo<o)
               {
                  oldo+=oldb-B[bb]+1;
               }
             }
             else if(O[oo]<oldo&&oo<o)
             {
                if(oldo-O[oo]<=oldb-B[bb]+1&&bb<b&&oo<o)
                {
                   oldo=O[oo];
                }
                else if(oldo-O[oo]>oldb-B[bb]+1&&bb<b&&oo<o)
                {
                   oldo-=oldb-B[bb]+1;
                }
              }
            oldb=B[bb];
            bb++;
          }//if

         }//if
       

      //printf("%d %d %d\n",ans,oldo,oldb);

     }//for         
            

      
    fprintf(p,"Case #%d: %d\n",++cs,ans);
  }//while

     
fclose(p);  

return 0;
}
 
