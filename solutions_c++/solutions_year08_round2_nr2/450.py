#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long map[1000002];
int isprime(long long pt)
{
    long long i;
    for(i=2;i<pt;i++)
    {
        if(pt%i == 0)
            return false; 
       if(i*i>pt)
          break;     
    }
    return true;
    
    }

int main()
{
//  freopen("OUTPUT.FIL","w",stdout);
 int allnum,casenum;
 int find;
 long long i,j,k,n;
 long long A,B,P,set,minp,maxp,pt,tmpa,tmpb,len,tmpt;
 freopen("b.in","r",stdin);
 //fstream fin("A-large.in");
 
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>A>>B>>P;
   set = B-A+1;
   len = B-A;
   memset(map,0,(len+1)*sizeof(long long));
 //  for(i=1;i<=(len+1);i++)
 //    map[i] = i;
   minp = P;
   maxp = B;
   if(maxp>(minp+1000000))
       maxp = minp+1000000;
   for(pt=minp;pt<=maxp;pt++)
   {
     if(isprime(pt))                      
     {
       tmpa = (A-1)/pt;
       tmpb = B/pt;
       find = 1;
       for(i=(tmpa+1);i<=tmpb;i++)
       {
         if(find)
         {
            set++;
            find = 0;
         }
         j = i*pt-A;
         if(map[j]>0)
         {
            if(map[j] == pt) 
                continue; 
            tmpt = map[j];
            for(k=0;k<=len;k++)
            {
               if(map[k] == tmpt)
                   map[k] = pt;                   
            }            
         }                     
         else
            map[j] = pt; 
         set--;      
                                  
       }    
 //      if(casenum == 3)
 //      cout<<set<<endl;                                
     }
   }
   cout<<"Case #"<<casenum<<": "<<set<<endl;
  // cout<<sum<<endl;
  // printf("Case #%d: %lld\n",casenum,sum);
   
 }

}
