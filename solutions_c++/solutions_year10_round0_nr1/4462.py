#include<stdio.h>
#include<stdlib.h>


struct snap{
       bool power;
       bool on;
       }a[100];
       
       void reset(int n)
       {
            int i;
            for(i=0;i<n;i++)
            {
                            a[i].power=false;
                            a[i].on=false;
            }
            a[0].power=true;
            }
            
            int main()
            {
                
                freopen("A-small-attempt2.in", "r",stdin);
                freopen ("A-small-attempt2.out", "w",stdout);
                int T;
                scanf("%d",&T);
                int cases = 0;
	    while ( T-- ) {
	        int n;
	        int k;
	        scanf ("%d %d", &n, &k);
	 
	        reset (n);
	 
	        for ( int i = 0; i < k; i++ ) {
	            for ( int j = 0; j < n; j++ ) {
	                if ( a [j].power )
	                    a [j].on = a [j].on ? false : true;
	            }
	            for ( int j = 0; j < n; j++ ) {
	                if ( a [j].power && a [j].on )
	                    a [j + 1].power = true;
	                else
                    a [j + 1].power = false;
	            }
	        }
	 
	        if ( a [n - 1].power && a [n - 1].on )
	            printf("Case #%d: ON\n", ++cases);
	        else
	            printf("Case #%d: OFF\n", ++cases);
	    }
	    return 0;
	}
