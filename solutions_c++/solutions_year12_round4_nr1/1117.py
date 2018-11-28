
//A Moolla (6 May 2012)

#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <list>

using namespace std;

//T is the number of trials
//N is the # of vines

int t,n,d;
int centre[10000];
int len[10000];
int move[10000];
int temp;
int main ()
{
    freopen("A-large.in","r",stdin);   
    freopen("A-large.out","w",stdout);
    
    scanf ("%d",&t);
    for (int trial=1;trial<=t;trial++)
    {
     cout<<"Case #"<<trial<<": ";
     scanf ("%d",&n);
     for (int i=0;i<n;++i)
     {
         scanf("%d %d",&centre[i],&len[i]);
     }
     scanf("%d",&d);
     
     //Sort
     for (int i=0;i<n;++i)
     {
         for (int j=i+1;j<n;++j)
         {
             if (centre[i]>centre[j])
             {
                             temp = centre[i];
                             centre[i] = centre[j];
                             centre[j] = temp;
                             temp = len[i];
                             len[i] = len[j];
                             len[j] = temp;             
             }    
         }    
     }
     if (centre[0]>len[0])
        cout<<"NO\n";
     else
     {     
           int last = 0;
           bool love = false;
           move[0] = centre[0];
           for (int i=0;i<n;++i)
           {
               //cout<<i<<" "<<centre[i]<<" "<<move[i]<<"\n";
               
               if (last<i)
                  break;
               for (int j=last+1;j<n;j++)
               {
                   if (centre[j] <= move[i]+centre[i])
                   {
                                  last = j;
                                  move[j] = centre[j] - centre[i];  
                                  if (move[j]>len[j])
                                     move[j] = len[j];
                   }    
                   
               }
               if (d<=move[i]+centre[i])
               {
               
                      love = true;
                      break;                         
               }    
           }
           if (love)
              cout<<"YES\n";
           else
              cout<<"NO\n";
     }
                      
    }
    return 0;    
}

