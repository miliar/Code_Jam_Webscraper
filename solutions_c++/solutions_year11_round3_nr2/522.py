#include <cmath>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<queue>
#include<fstream>

using namespace std;

int Distance[1000001], cir[1000001], Total[1000001];

int main(){

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int i, j, datacase, c=0, L, n, t, C, ans, Temp2, Temp;

    scanf("%d", &datacase);
    while( datacase-- )
	{
        scanf("%d%d%d%d", &L, &t, &n, &C );
        for( i=0; i<C; ++i )
            scanf("%d", &cir[i]);
        for( i=0,j=0; i<n; ++i,++j ){
            if( j==C )  j = 0;
            Distance[i] = cir[j];
        }
        Total[0] = 0;

        for( i=1; i<=n; ++i )
            Total[i] = Total[i-1] + Distance[i-1];
        ans = Total[n]*2;
		if( L == 1 )
		{
            for( i=0; i<n; ++i )
			{
                Temp = Total[i]*2;
                if( Temp < t )
				{
                    if( Temp + Distance[i]*2 <= t )   
						Temp = Temp + Distance[i]*2;
                    else                       
						Temp = t + (Distance[i]-(t-Temp)/2);
                }
                else    
					Temp += Distance[i];
                Temp += ((Total[n]-Total[i+1])*2);
                if( Temp < ans ) ans = Temp;
            }        
		}
        else if( L==2 )
		{
            for( i=0; i<n; ++i )
			{
                Temp = Total[i]*2;
                if( Temp < t )
				{
                    if( Temp + Distance[i]*2 <= t )   
						Temp = Temp + Distance[i]*2;
                    else                        
						Temp = t + (Distance[i]-(t-Temp)/2);
                }
                else    
					Temp += Distance[i];

                for( j=i+1; j<n; ++j )
				{
                    Temp2 = Temp + ((Total[j]-Total[i+1])*2);
                    if( Temp2 < t )
					{
                        if( Temp2 + Distance[j]*2 <= t )   
							Temp2 = Temp2 + Distance[j]*2;
                        else                         
							Temp2 = t + (Distance[j]-(t-Temp2)/2) ;
                    }
                    else    
						Temp2 += Distance[j];
                    Temp2 += ((Total[n]-Total[j+1])*2);
                    if( Temp2 < ans ) 
						ans = Temp2;
                }
            }
        }
        printf("Case #%d: %d\n", ++c, ans );
    }
    return 0;
}
