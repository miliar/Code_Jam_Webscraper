#include <stdio.h>
#include <algorithm>
using namespace std;
int L,D,N ;
int Case ;
bool str[27][2000] ;
char w[6000][20] ;
char s[20000] ;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("cc.out","w",stdout) ;
    int i ;
    int deep ;
    while(3 == scanf("%d %d %d",&L,&D,&N))
    {
        Case = 1 ;
        for(i = 0 ; i < D ; i ++)
        {
            scanf("%s",w[i]) ;   
        }    
        for(i = 0 ; i < N ; i ++)
        {
           memset(str,0,sizeof(str)) ;   
           scanf("%s",s) ;
           int j = 0 ;
           deep = 0 ;
           while(s[j] != '\0')
           {
              if(s[j] == '(')
              {
                      
                 while(s[j] != ')')
                 {
                    if(s[j] >= 'a' && s[j] <= 'z')        
                    str[s[j]-'a'][deep] = 1 ;
                    j ++ ;        
                 }  
                 deep ++ ;   
              }     
              else
              {
                  if(s[j] >= 'a' && s[j] <= 'z')
                  {
                   str[s[j]-'a'][deep] = 1;
                   deep ++ ;
                  }
                  j ++ ;
              }
           }  
           int ans = 0 ;
           for(j = 0 ; j < D ; j ++)
           {
              int k = 0 ;
              while(w[j][k] != '\0')
              {
                 if(str[w[j][k]-'a'][k] == 1){}
                 else break ;
                 k ++ ;        
              }   
              if(w[j][k] == '\0')
              {
                 ans ++ ;     
              }
           } 
           printf("Case #%d: %d\n",Case++,ans);
        }
    }
    return 0 ;
} 
