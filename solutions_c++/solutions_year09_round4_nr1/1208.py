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
	char str[1000];
	__int64 a[100];
		
    scanf("%d\n", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		int n; scanf("%d\n", &n);
		for (int i = 0; i < n; i++){
			a[i]=0;
			for (int j = 0; j < n; j++){
				char c;
				scanf("%c", &c);
				if (c=='1'){
					a[i] = (__int64)1 << j;
					
				}
				
			}
			fgets(str, 1000, stdin);
		}
		int f = 0;
		int k = 0;
		for (int i = 0; i < n; i++){
			__int64 r = 1<<i;
			for (int j = k; j < n; j++){
				if (a[j] <= r){
					if (i != j){
						__int64 t = a[j];
						for (int p=i; p<=j; p++){
							__int64 t1 = a[p];
							a[p] = t;
							t = t1;
						}
						f += j-i;
					}
					break;
				}
			}
			k++;
		}

		printf("%d\n", f);
	}
 }