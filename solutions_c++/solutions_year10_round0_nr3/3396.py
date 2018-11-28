#include "stdio.h"

int main()
{
FILE *in_ptr, *out_ptr;
unsigned int i, t;

in_ptr = fopen( "C-small-attempt3.in", "r+" );
out_ptr = fopen( "C-small.out", "w+" );

unsigned int T, R, k, N;
unsigned int g[1000];

long long total;
unsigned int gr_index, gr_start_index, p_cnt;

fscanf( in_ptr, "%d", &T );

for( t=1; t<=T; t++ )
 {
	fscanf( in_ptr, "%d", &R );
	fscanf( in_ptr, "%d", &k );
	fscanf( in_ptr, "%d", &N );

	for( i=0; i<N; i++ )
		fscanf( in_ptr, "%d", &g[i] );

      total = 0LL;
      gr_index = 0L;
      for (i = 0; i < R; ++i) {
         p_cnt = 0L;
         gr_start_index = gr_index;
         while ((p_cnt + g[gr_index]) <= k) {
            p_cnt += g[gr_index];
            if (++gr_index == N) {
               gr_index = 0;
            }
            
            if (gr_index == gr_start_index) {
               break;
            }
         }
         
         total += p_cnt;
      }



	fprintf( out_ptr, "Case #%d: %u\n", t, total );

 }

}




