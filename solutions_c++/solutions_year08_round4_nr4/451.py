#include <cstdio>
#include <iostream>
#include <string>
using namespace std ;


int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out.txt", "w", stdout);
	int CASE, ks ,k, i, j, l, MAX;
	char input[1010],ttt[1010];
	int arr[10];
	scanf("%d", &CASE);
	for(ks = 1; ks <= CASE; ks++){
		MAX = 1000000000;
		scanf("%d", &k);
		scanf("%s", input);
		for(j = 0; j < k; j ++)
			arr[j] = j;
		int div = strlen(input) / k;
		do{
			for(j = 0; j < div; j ++){
				for( l = 0; l < k; l ++){
					ttt[j * k + arr[l]] = input[j * k + l] ;
				}	
			}
			int cnt = 0 ;
			int lst = -1 ;
			for(j = 0; j < strlen(input); j ++){
				if(lst != ttt[j]){
					cnt ++;
					lst = ttt[j];	
				}				
			}
			if(cnt < MAX)
				MAX = cnt ;
			
		}while(next_permutation(arr, arr + k));
		printf("Case #%d: %d\n", ks, MAX);
	}
	return 0;    
}
