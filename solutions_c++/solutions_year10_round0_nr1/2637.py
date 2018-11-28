#include <stdio.h>
int n,m;
int main()
{
    int kase,ka=1;
    freopen("g123.out","w",stdout);
    scanf("%d", &kase);
    while( ka<=kase ){
        int  t=1,v=0,flag=1;
        scanf("%d%d", &n ,&m);
        for(int i=0 ; i<n&&flag ; i++) 
        if( m&t )        
           t *= 2;
        else flag =0;
        
        if(flag)printf("Case #%d: ON\n",ka++);
        else printf("Case #%d: OFF\n",ka++);
                    
    } 
    return 0;    
} 
/*

*/
