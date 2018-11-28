#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;
char number[100], str[100];

int main(){

	//freopen("pb.in","r",stdin);
	freopen("B-large.in","r",stdin);

	int turn, T;
	scanf("%d",&T);
	for(turn=0;turn<T;++turn){
		int N, i = 99;
		scanf("%s",str);
		memset(number,0,sizeof(number));
		int len = strlen(str);
		int base = 100-len;
		for(i=0;i<len;++i)	number[base + i] = str[i]-'0';
		next_permutation( number, number+100 );
		bool flag = true;
		printf("Case #%d: ",1+turn);
		for(i=0;i<100;++i){
			if( flag ){
				if( number[i]==0 )	continue;
				printf("%d",number[i]);
				flag = false;
			}
			else{
				printf("%d",number[i]);
			}
		}
		putchar('\n');
	}
	return 0;
}
