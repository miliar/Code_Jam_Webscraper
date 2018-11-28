#include <stdio.h>
#include <math.h>
int main () {
        int t;
        scanf ( "%d", &t );
        while ( t-- ) {
                int a, b;
                scanf ( "%d %d", &a, &b );
                int i, j, k,l,m,n,o,z[100],p,in=0;
                int sum = 0;
                char y[5];              
                for ( i = a; i <= b; i++ ) {
                        j = i;
                        n = i;
                        l=0;
                        m=i;
                        while ( j != 0 ) {
                                k = j%10;
                                j = j / 10;
                                y[l]=k+48;
                                l++;
                        }
                        l--;
                        o = l; 
                        in = 0;
                        while(l>0){
                        m = (m - ( y[l] - 48 ) * pow ( 10, o ))*10 + y[l] - 48;
                        z[in++]=m;
                        if(m<=b&&m>n){
                        for ( p = 0;p<in-1;p++){
                                if(m==z[p])
                                break;
}
                        if(p==in-1)
                        sum++;
}
                        //printf ( "%d   %d\n", m,n);
                        
                //      printf ( "%d   %d\n", m,n);
                        l--;
                        }
        }
                printf ( "\n%d\n", sum);
        }
        return 0;
}