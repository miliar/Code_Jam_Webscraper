#include <cstdio>
int fabs(int a) {
	return a > 0 ? a : -a;
}
int main() {
	int t,n,a,lastO, lastB, blue, orange, needed,j,i,fulltimes[10001], result;
	char c;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		
			lastO = lastB = 0;
			blue = orange = 1;
			fulltimes[0] = 0;
			j = 0;
		
			scanf("%d", &n);
			for(j=1; j <= n; j++) {
				
					c = ' ';
					while(c == ' ')
						scanf("%c", &c);
				
					scanf("%d", &a);
					
					if(c == 'O') {
						
						needed = fabs(orange - a) + 1;
						
						result = fulltimes[j-1] + 1;
						if( result < fulltimes[lastO] + needed)
							result = fulltimes[lastO] + needed;
						
						
						orange = a;
						lastO = j;
					}
					
					else if(c == 'B') {
						
						
						needed = fabs(blue - a) + 1;
						
						result = fulltimes[j-1] + 1;
						if( result < fulltimes[lastB] + needed)
							result = fulltimes[lastB] + needed;
						
						blue = a;
						lastB = j;
					}
					fulltimes[j] = result;
				
				
			}
			printf("Case #%d: %d\n", i, result);
	}
	
}
