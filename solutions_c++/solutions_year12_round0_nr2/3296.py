#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(void) {
	int testCases, N,S,P, store, answer, remainder, quotient;
	char temp;
	FILE *infile= fopen("input", "r+");
	fscanf(infile, "%d",&testCases);
	fscanf(infile, "%c", &temp);
	for(int i=1; i<=testCases; ++i) {
		answer = 0;
		printf("Case #%d: ",i);
		fscanf(infile, "%d%d%d", &N,&S,&P);
		for(int j=0; j<N; ++j) {
			fscanf(infile, "%d", &store);
			remainder = store%3;
			quotient = store/3;
			if (store<29 && store>1){
				if(remainder == 0) {
					if(quotient>=P) {
						++answer;
					} else if(quotient+1==P && S>0){
						--S;
						++answer;
					}
				} else if(remainder == 1) {
					if(quotient+1>=P) {
						++answer;
					}
				} else {
					if(quotient+1>=P) {
						++answer;
					} else if(quotient+2==P && S>0){
						--S;
						++answer;
					}
				}
			} else {
				if(store == 0 && P==0) {
					++answer;
				} else if(store == 1 && P<=1) {
					++answer;
				} else if(store == 29 && P<=10) {
					++answer;
				} else if(store == 30 && P<=10) {
					++answer;
				}
					
			}
		}
		printf("%d\n", answer);
		fscanf(infile, "%c", &temp);
	}
	return 0;
}
