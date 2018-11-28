#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <stdlib.h>


#define __int64 long long
//#define MAX(a,b) ((a)>(b)?(a):(b))
//#define MAX(a,b,c) (((a)>(b))?((a)>(c)?(a):(c)):(b))
//#define MIN(a,b) ((a)<(b)?(a):(b))
//#define MIN(a,b,c) ((a)<(b)?(a)<(c)?(a):(c):(b))
int MAX(int a, int b, int c){
	if (a<b) a=b;
	if (a<c) a=c;
	return a;
}
int MIN(int a, int b, int c){
	if (a>b) a=b;
	if (a>c) a=c;
	return a;
}


int main(){
    freopen("map.in", "rt",stdin);
    freopen("map.out", "wt",stdout);
	int t;
    scanf("%d\n", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		char c; scanf("%c", &c);
		int n = 1;
		int a[100];
		a[0]=0;

		while (c<='9'&&c>='0'){
			a[n++]=c-'0';
			if (scanf("%c", &c)==EOF) break;
		}
		scanf("\n");
		n--;
			int k = n-1;
			while(a[k]>=a[k+1]) k--;
			int j = n;
			while (a[k]>=a[j]) j--;
			a[k] ^= a[j];
			a[j] ^= a[k];
			a[k] ^= a[j];
			j = n;
			k++;
			while (j>k){
				a[k] ^= a[j];
				a[j] ^= a[k];
				a[k] ^= a[j];
				j--; k++;
			}
		int i = a[0]==0?1:0;
		for (;i<=n;i++)
			printf("%i", a[i]);
		printf("\n");
	}
 }