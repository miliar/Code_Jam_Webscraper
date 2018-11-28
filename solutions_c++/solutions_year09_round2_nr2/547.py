#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int hash[12];
int tp[12];

int main()
{

	int t;

	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);
	scanf("%d" , &t);
	int cas = 0;
	while (t --){
		int n;
		cas ++;
		memset(hash , 0 , sizeof(hash));
		scanf("%d" , &n);
		int mm = n;
		while (mm){
			hash[mm % 10] ++;
			mm /= 10;
		}
		int i;
		for (i = n + 1 ; ; i ++){
			int tmp = i;
			memset(tp , 0 , sizeof(tp));
			while (tmp){
				tp[tmp % 10] ++;
				tmp /= 10;
			}
			int j;
			for (j = 1 ; j <= 9 ; j ++)
				if (tp[j] != hash[j])break;
			if (j == 10)break;
		}
		printf("Case #%d: %d\n" , cas , i);
	}
	
	

	return 19890907;
}