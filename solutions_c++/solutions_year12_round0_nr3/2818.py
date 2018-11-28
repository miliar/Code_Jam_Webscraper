#include <cstdio>
#include <cstring>
#define MAXB 2000100

bool tab [MAXB];
int stack [10];

int main () {
	int TC, ndig, num, A, B, res, mult, ns;
	bool instack;
	scanf("%d", &TC);
	
	for ( int tc = 1; tc <= TC; ++tc ) {
		scanf("%d %d", &A, &B);
		
		memset( tab, 0x00, sizeof(tab) );
		num = A;
		ndig = 0;
		mult = 1;
		res = 0;
		
		while ( num > 9 ) {
			num = num / 10;
			++ndig;
			mult = mult * 10;
		}
		//printf("NDIG:%d\n", ndig);
		
		for ( int n = A; n < B; ++n ) {
			num = n;
			ns = 0;
			//printf("Start %d :", num);
			
			/*/add the initial
			if ( !tab[num] ) {
				++res;
				tab[num] = true;
			}*/
			
			for ( int k = 0; k < ndig; ++k ) {
				num = (num / 10) + ((num % 10) * mult);
				
				instack = false;
				for ( int j = 0; j < ns; ++j ) {
					if ( stack[j] == num ) {
						instack = true;
						break;
					}
				}
				
				//printf(" %d", num);
				if ( num > n && num <= B && !instack /*&& !tab[num] */) {
					++res;
					stack[ns++] = num;
					/*tab[num] = true;*/
					//printf("*");
				}
			}
			//printf("\n");
		}
		printf("Case #%d: %d\n", tc, res);
	}
	
	return 0;
}
					
