#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	int T, C, D, N;
	char buff[1024];
	char list[1024];
	int list_c;
	
	const int nbe = 8;
	char be[nbe] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
	char rbe[256];
	for(int i=0; i<256; i++)
		rbe[i] = -1;
	for(int i=0; i<nbe; i++)
		rbe[ be[i] ] = i;
	
	
	char reptab[nbe][nbe];
	bool cleartab[nbe][nbe];
	int extab[nbe];
	
	scanf("%d", &T);
				
	for(int ti=0; ti<T; ti++) {
		for(int j=0; j<nbe; j++) {
			for(int k=0; k<nbe; k++) {
				reptab[j][k] = 0;
				cleartab[j][k] = false;
			}
			extab[j] = 0;
		}
										
		scanf("%d", &C);
		
		for(int j=0; j<C; j++) {
			scanf("%s", buff);
			char b1 = rbe[ buff[0] ];
			char b2 = rbe[ buff[1] ];
			char x = buff[2];
			
			reptab[b1][b2] = x;
			reptab[b2][b1] = x;
		}
		
		
		scanf("%d", &D);		
		for(int j=0; j<D; j++) {
			scanf("%s", buff);
			char b1 = rbe[ buff[0] ];
			char b2 = rbe[ buff[1] ];
			
			cleartab[b1][b2] = true;
			cleartab[b2][b1] = true;
		}
		
		scanf("%d", &N);
		scanf("%s", buff);
		list_c = 0;
		
		for(int j=0; j<N; j++) {
					
			char b = rbe [ buff[j] ];
			
			if (list_c > 0) {
				char pb = rbe [ list[list_c-1] ];
				
				if (pb >= 0) {
					if (reptab[b][pb] > 0) {
						extab[pb]--;
						list[list_c-1] = reptab[b][pb];
						continue;
					}	
				}		
			}
					
			bool is_clear = false;	
			for(int k=0; k<nbe; k++) {
				if (extab[k]>0) {					
					if (cleartab[b][k]) {
						is_clear = true;
						break;
					}
				}
			}
			
			if (is_clear) {
					list_c = 0;
					for(int m=0; m<nbe; m++)
						extab[m] = 0;
			} else {
				extab[b]++;
				list[list_c] = be[b];
				list_c++;															
			}
					
		} 
								
		printf("Case #%d: [", ti+1);
		for(int j=0; j<list_c; j++) {
			if (j>0)
				printf(", ");
			printf("%c",list[j]);	
		}
		printf("]\n");
		
	}
	
	return 0;
}

