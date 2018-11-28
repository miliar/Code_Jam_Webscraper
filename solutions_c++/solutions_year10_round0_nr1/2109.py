#include <stdio.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

inline FILE *checked_fopen( const char *file_name,
                            const char *mode_str, int exit_code=1 )
{
   FILE *file;

   if( (file=fopen(file_name, mode_str))==NULL )
   {
      printf( "Can't open file %s in %s mode",
                          file_name, mode_str );
   }

   return file;
}

int main(int argc, char *argv[]) {
//processing...
	int T, N, K;
	scanf("%d", &T);
	for(int i=1; i<=T; ++i){
		scanf("%d %d", &N, &K);
		if(K == 0){
			printf("Case #%d: OFF\n", i);
		} else{
			K+=1;
			int mask = 1 << N;
			mask-=1;
			if( (K & mask) == 0 ){
				printf("Case #%d: ON\n", i);	
			} else{
				printf("Case #%d: OFF\n", i);
			}
		}
	}
}







