#include <iostream>
#include <stdio.h>

using namespace std ;

bool Parse(int n,int p)
{
     int n2 = p-1 ;
     if(n2 < 0)
           n2 = 0 ;
     int n3 = p-1 ;
     if(n3 < 0)
           n3 = 0 ;
     if((p+n2+n3) <= n)
                    return true ;
     return false ;
}

bool SurpriseParse(int n,int p)
{
     int n2 = p-2 ;
     if(n2 < 0)
           n2 = 0 ;
     int n3 = p-2 ;
     if(n3 < 0)
           n3 = 0 ;
     if((p+n2+n3) <= n)
                    return true ;
     return false ;
}     
int main()
{
    int t ;
    scanf("%d",&t) ;
    int ctr = 1 ;
    while(t--) {
               int n,s,p ;
               scanf("%d%d%d",&n,&s,&p) ;
               int A[n] ;
               for(int i=0;i < n;i++)
                       scanf("%d",&A[i]) ;
               int ans = 0 ;
               for(int i=0;i < n;i++){
                       if(Parse(A[i],p))
                            ans += 1 ;
                       else if(s > 0){
                            if(SurpriseParse(A[i],p)){
                                ans += 1 ;
                                s-- ;
                            }
                       }
               }
               cout << "Case #" << ctr++ << ": " << ans << endl ;
    }
    //system("pause") ;
    return 0 ;
}
