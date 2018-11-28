#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
__int64 n,k;

void init(){
	scanf("%I64d%I64d",&n,&k);
	return;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: ",i);
		if ((k%(1<<n))==((1<<n)-1)){
			puts("ON");
		} else {
			puts("OFF");
		}
	}
	return 0;
}
