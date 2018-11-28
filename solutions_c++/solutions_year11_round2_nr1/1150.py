#include <cstdio>
#include <cmath>
#include <algorithm>
int fmin(int a, int b) {
	return a < b ? a : b;
}
int fmax(int a, int b) {
	return a > b ? a : b;
}
int fabs(int a) {
	return a > 0 ? a : -a;
}
int main() {
	int i,j,k,l,n,m,a,y,z,w,res,t,numerTestu;
	char c;
	char wyn[2000][2000];
	int ile[2000];
	double r1[2000],r2[2000],r3[2000],x;
	scanf("%d", &t);
	for(numerTestu = 1 ; numerTestu <= t; numerTestu++) {
		
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			l = 0;
			r1[i] = 0;
			for(j = 0; j < n; j++) {
				scanf("%c", &c);
				while( c == '\n')
					scanf("%c", &c);
				wyn[i][j] = c;
				if(c != '.') {
					
					l++;
					r1[i] += ((c - '0')) * 1.00;
				}
				
			}
			
			
			while(c!='\n')
				scanf("%c", &c);
			
			if(l != 0)
				r1[i] /= l;
			ile[i] = l;
		}
		
		
		for(i = 0; i < n; i++) {
			
			r2[i] = 0;
			k = 0;
			for(j = 0; j < n; j++) {
				
				if(wyn[i][j] == '.') 
					continue;
				
				x = r1[j];
				x *= ile[j]*1.00;
				x -= (wyn[j][i] - '0')*1.00;
				x /= ile[j] - 1.00;
				r2[i] += x;
			}
			
			r2[i] /= (ile[i] * 1.00);
			
		}
		
		
		
		for(i = 0; i < n; i++) {
			
			r3[i] = 0;
			
			for(j = 0; j < n; j++) {
				
				if(wyn[i][j] == '.') 
					continue;
				
				r3[i] += r2[j];
			}
			
			r3[i] /= (ile[i] * 1.00);
			
		}
	
		
		
		printf("Case #%d:\n", numerTestu);
		
		for(i = 0; i < n; i++) {
			//printf("x : %lf\n", r2[i]);
			printf("%.6lf\n", 0.25*r1[i] + 0.5*r2[i] + 0.25*r3[i]);
			
		}
		
	}
	return 0;
}
