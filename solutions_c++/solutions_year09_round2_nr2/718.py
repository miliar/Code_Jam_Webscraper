#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

bool cmp(int a,int b) {
//	if (a == 0) return true;
	return a < b;
}
bool lcmp(int a,int b) {
	return a > b;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int base[100];
	int base_top;
	int Case = 1;
	int i;
	int T;
	__int64 n;
	char str[100];

	scanf("%d ",&T);
	for (Case = 1; Case <= T; Case ++) {

		base_top = 0;

	//	scanf("%I64d",&n);
		scanf("%s",str);
		int len = strlen(str);
		for (i = 0; i < len; i ++) {
			base[i] = str[i]-'0';
		}
		base_top = len;
	/*	while (n) {
			base[base_top ++] = n % 10;
			n /= 10;
		}*/
	/*	for (i = 0; i < base_top / 2; i ++) {
			int t = base[i];
			base[i] = base[base_top - i - 1];
			base[base_top - i - 1] = t;
		}*/
		for (i = base_top - 1; i > 0; i --) {
			if (base[i-1] < base[i]) {
				break;
			}
		}
	/*	base[0] = 1;
		base[1] = 1;
		base[2] = 5;
		next_permutation(base,base+base_top);*/

		if (i > 0) {
		//	printf(".");
			next_permutation(base,base+base_top);
	/*		printf("Case #%d: ",Case);
			for (i = 0; i < base_top; i ++) {
				printf("%d",base[i]);
			}
			printf("\n");*/
			printf("Case #%d: ",Case);
		for (i = 0; i < base_top; i ++) {
			printf("%d",base[i]);
		}
		} else {
		/*	for (i = 0; i < base_top; i ++) {
				printf("%d",base[i]);
			}
			printf("->");*/
			sort(base,base+base_top,cmp);
			for (i = 0; i < base_top; i ++) {
				if (base[i] == 0) {} else break;
			}
			base[base_top] = base[i];
			base[i] = base[base_top - 1];
			base[base_top - 1] = 0;
			sort(base,base+base_top-1,lcmp);
		/*	for (i = base_top; i > 1; i --) {
				base[i] = base[i-1];
			}
			base[i] = 0;*/
		/*	i --;
			for (; i > 0; i --) {
				base[i] = base[i-1];
			}*/
			base_top ++;
			printf("Case #%d: ",Case);
		for (i = base_top-1; i >= 0; i --) {
			printf("%d",base[i]);
		}
		}	

		
		printf("\n");

		
	}
	return 0;
}
