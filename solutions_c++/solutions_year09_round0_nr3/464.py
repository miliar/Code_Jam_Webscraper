#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char wstr[20] = "welcome to code jam";
int len, sol;
int sumd[19];
char dat[510];
int main(){
	sol = 0;
	int T, tt, len, i, j, k;
	gets(dat);
	T = atoi(dat);
	for(tt=1;tt<=T;tt++){
		gets(dat);
		len = strlen(dat);
		for(i=0;i<19;i++){
			sumd[i] = 0;
		}
		for(i=0;i<len;i++){
			for(j=18;j>=0;j--){
				if(dat[i] == wstr[j]){
					if(j == 0) sumd[j] ++;
					else{
						sumd[j] += sumd[j-1];
					}
					sumd[j] %= 10000;
				}
			}
		}
		sol = sumd[18]%10000;
		printf("Case #%d: %04d\n",tt, sol);
	}
	return 0;
}