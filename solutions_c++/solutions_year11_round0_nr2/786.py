#include <cstdio>

int id(char c) {
	
	switch(c) {
		case 'Q' : return 0;
		case 'W' : return 1;
		case 'E' : return 2;
		case 'R' : return 3;
		case 'A' : return 4;
		case 'S' : return 5;
		case 'D' : return 6;
		case 'F' : return 7;
	}
	return 8;	
}

int main() {
	char combine[9][9];
	char opposed[9][9];
	
	
	char list[101];
	int len;
	
	int t,n,c,d,i,j;
	char c1,c2,c3;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		
		for(int m = 0; m <= 8; m++)
			for( int n = 0; n <= 8; n++)
				combine[n][m] = combine[m][n] = opposed[n][m] = opposed[m][n] = 0;
		
	
		scanf("%d", &c);
		while(c--) {
			c1 = ' ';
			while(c1 == ' ')
				scanf("%c", &c1);
			scanf("%c", &c2);
			scanf("%c", &c3);
			
			combine[id(c1)][id(c2)] = combine[id(c2)][id(c1)] = c3;
		}
		
		scanf("%d", &d);
		while(d--) {
			c1 = ' ';
			while(c1 == ' ')
				scanf("%c", &c1);
			scanf("%c", &c2);			
			opposed[id(c1)][id(c2)] = opposed[id(c2)][id(c1)] = 1;
		}
		
		len = 0;
		list[0] = '.';
		
		scanf("%d", &n);
		
		
		while(n--) {
			
			c1 = ' ';
			while(c1 == ' ')
				scanf("%c", &c1);
			
			
			len++;
			list[len] = c1;
			
			if(len >= 2) {
				
				c2 = list[len-1];
				
				if(combine[id(c1)][id(c2)] != 0) {
					
					len--;
					list[len] = combine[id(c1)][id(c2)];
					
				} else {
					
					for(int k = 1; k < len; k++) 
						if (opposed[id(list[k])][id(c1)] == 1) {
							len = 0;
							
						}
							
				
				}
				
			}
			
		}
		
		printf("Case #%d: [", i);		
		if(len >= 1)
			printf("%c", list[1]);
		for(int k = 2; k <= len; k++)
			printf(", %c", list[k]);		
		printf("]\n");
		
	}
	
}
