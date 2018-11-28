// c2.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <string.h>

char d[100];
int len;
int cnt;

void calcuate() {
	__int64 sum = 0;
	__int64 digit = 0;
	int sign = 1;
	for(int i=0;i<=len*2-2;i++) {
		char ch = d[i];
		if (ch>='0' && ch<='9') digit = digit*10+ch-'0';
		else if (ch==' ') ;
		else {
			sum += sign*digit;
			digit = 0;
			sign = ch=='+'?1:-1;
		}
	}
	sum += sign*digit;
	if (sum<0) sum=-sum;
	bool test = (sum ==0 || sum % 2 == 0 || sum % 3 ==0 || sum % 5 ==0 || sum % 7 == 0);
	
	// printf("%s = %d (%s)\n",d,sum,test?"ugly":"-");
	if (test) cnt++;
}

char *mask = " +-";
void put(int index) {
	if (index>=len-1) {
		calcuate();
		return;
	}
	for(int i=0;i<3;i++) {
		d[2*index+1]=mask[i];
		put(index+1);
	}
}
void work() {
	len = strlen(d);
	for(int i=len-1;i>=0;i--) {
		d[2*i]= d[i];
	}
	d[2*len]=0;
	put(0);
}
int main() {

	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		scanf("%s",d);
		cnt = 0;
		work();
		printf("Case #%d: %d\n",i,cnt);
	}
}