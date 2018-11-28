#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;


int main(){
	int T;
	scanf("%d", &T);
	char ch;
	scanf("%c", &ch);

	int i;
	for(i = 0; i < T; i++){
		char s[65];
		gets(s);
		int base = 0;
		bool hash[40];
		int len = strlen(s);
		int k, val;
		memset(hash, 0, 40);
		for(k = 0; k < len; k++){
			if( s[k] >= '0' && s[k] <='9'){
				val = s[k] - '0';
				if(hash[val] == 0){
					hash[val] = 1;
					base++;
				}
			}else{
				val = s[k] - 'a' + 10;
				if(hash[val] == 0){
					hash[val] = 1;
					base++;
				}
			}			
		}

		if(1 == base)
			base++;

		int num[65], code[65];
		for(k = 0; k < 65; k++){
			code[k] = -1;
		}
		num[0] = 1;
		k = 0;
		if( s[k] >= '0' && s[k] <='9'){
			val = s[k] - '0';
		}else{
			val = s[k] - 'a' + 10;
		}
		code[val] = 1;

		int next = 0;
		for(k = 1; k < len; k++){
			if( s[k] >= '0' && s[k] <='9'){
				val = s[k] - '0';
			}else{
				val = s[k] - 'a' + 10;
			}
			if(code[val] != -1){
				num[k] = code[val];
			}else{
				code[val] = next;
				num[k] = code[val];
				if(0 == next)
					next=2;
				else
					next ++;
			}
		}

		long long sum = 0;
		for(k = 0; k < len; k++){
			sum += num[k] * pow( (double)base, len - k -1);
		}
		printf("Case #%d: %lld\n", i+1, sum);
	}
	return 1;
}