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

int main(int argc, char *argv[]) {
//processing...
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int L, P, C;
		scanf("%d %d %d", &L, &P, &C);
		unsigned int i=1;
		while(true){
			L*=C;
			if(L>=P){
				break;
			}
			++i;
		}
		bool f;
		f = i && !(i & (i - 1));
		unsigned r=0;
		while (i >>= 1) // unroll for more speed...
		{
  			r++;
		}
		if(f){
			printf("Case #%d: %u\n", t, r);
		} else{
			printf("Case #%d: %u\n", t, r+1);
		}
	
	}
}







