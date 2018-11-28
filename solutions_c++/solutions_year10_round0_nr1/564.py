#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int T, N, K;

int main()
{
    //freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
    int i, j, t = 1;
    
    for ( scanf("%d",&T); T; T-- ) {
        scanf("%d%d",&N,&K);
        for ( j = i = 1; i <= N; i++ )
            j<<=1;
            
        printf("Case #%d: ",t++);
        if ( K%j == j - 1 )
            printf("ON\n");
        else
            printf("OFF\n");
    }
    
    //system("PAUSE");
    return 0;
}
