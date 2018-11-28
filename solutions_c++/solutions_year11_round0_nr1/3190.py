#include<stdio.h>
#define max(a,b) ((a) > (b) ? (a) : (b))
#define abs(a) ( (a) > 0 ? (a) : -(a) )

int main (void) {
	int n,t,orange,blue,casa,cont = 1,pos_o,pos_b;
	char cor[1];
	scanf("%d",&t);
	while (t--) {
		scanf("%d",&n);
		orange = blue = 0;
		pos_o = pos_b = 1;
		while (n--) {
			scanf("%s %d",cor,&casa);
			//printf("\n%d %c: ",casa,cor[0]);
			
			if ( cor[0] == 'O' ) {
				orange += abs(casa-pos_o)+1;
				orange = max(orange,blue+1);
				pos_o = casa;
			}
			
			if ( cor[0] == 'B' ) {
				blue += abs(casa-pos_b)+1;
				blue = max(orange+1,blue);
				pos_b = casa;
			}
			
			//printf("o,b = %d,%d | ",orange,blue);
		}
		
		printf("Case #%d: %d\n",cont++,max(orange,blue));
	}
	
	return 0;
}
