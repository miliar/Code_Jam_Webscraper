#include<stdio.h>
#include<memory.h>
const int MAXN = 1000+1;
bool bIsInit[ MAXN ];
int iPeople[ MAXN ];
int iHead[ MAXN ];
int nPeopleGroup[ MAXN ];
#define bruteforce

int main()
{
    int t,ncase;
    t = ncase = 0;
	freopen( "C-large.in", "r", stdin);
	freopen( "C-large1.out", "w", stdout);
    scanf( "%d", &t );
    while( t-- )
    {
        ncase++;
        int r,k,n;
        scanf("%d %d %d", &r,&k,&n);
        for( int i=0;i<n;i++ )
            scanf("%d", &nPeopleGroup[i] );
        memset( iPeople, 0, sizeof(iPeople) );
        memset( bIsInit, 0, sizeof(bIsInit) );
        int p1,p2;
        p1=0;
        p2=0;
        while( !bIsInit[p2] )
        {
            bIsInit[p2] = true;
            iHead[p1] = p2;
			int i;
            for( i = p2 ; iPeople[p1] + nPeopleGroup[i] <= k ; i=(i+1)%n )
			{
				iPeople[ p1 ] += nPeopleGroup[ i ];
				if( i == (p2-1+n)%n )
				{
					i = p2;
					break;
				}
			}
            p2 = i;
            p1++;
        }        
		
        int cycle = p2;
		for( int i = 0 ; i < p1 ; i++ )
		{
            if( cycle == iHead[i] )
            {
                cycle = i;
                break;
            }
		}
        int res = 0;
        if( r <= cycle )
        {
            for( int i = 0 ; i < r ; i++ )
                res += iPeople[i];
        }
        else
        {
            int s1=0;
            int s2=0;
			r -= cycle;
            for( int i = 0 ; i < cycle; i++ )
                s1 += iPeople[i];
            for( int i = cycle ; i < p1 ; i++ )
                s2 += iPeople[i];
            int nc = p1 - cycle ;
            res = s1 + r / nc * s2;
            for( int i = 0 ; i < r % nc ; i++ )
                res += iPeople[i + cycle];
        }
        printf("Case #%d: %d\n", ncase, res);

    }
    return 0;
}
