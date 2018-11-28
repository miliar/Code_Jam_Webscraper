#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int NMAX = 30 ;
int l , d , n ;
int front , num ;
char testchar[NMAX][15] ;
char s[1000] ;


bool match(int k)
{
     int i ;
     bool flag ;
     front = 0 ;
    for(i=0;i<l;i++)
    {
           flag = false ;
          if(s[front] == '(')
          {
               front++;
               while(s[front] != ')')
               {
                     if(testchar[k][i] == s[front]) 
                     {
                                     flag = true ;
                                     break;
                     }
                     else front++;                
               }
              if(flag == false) return false ;                  
          }
          else
          {
              if(s[front] != testchar[k][i]) return false ;  
          }
          if(flag == true)
          {
               while(s[front] != ')')  front++;        
          }                                
          front++;
    }  
    return true ;   
}


int main(void)
{
//    freopen("A-small-attempt3.in","r",stdin) ;
//    freopen("A-small-attempt3.out","w",stdout);
    int i ,j;
    scanf("%d%d%d",&l,&d,&n);
    for(i=0;i<d;i++) scanf("%s",testchar[i]) ;
    for(i=0;i<n;i++)
    {
        scanf("%s",s);
        num = 0 ;
        for(j=0;j<d;j++) 
        {
            if(match(j)) num++;
            else continue ;                 
        }
        printf("Case #%d: %d\n",i+1,num);                     
    }
//    system("pause");
    return 0 ;
}
