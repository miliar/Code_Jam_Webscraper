#include <cstdio>
int main(){
	int ans[] = {0, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
	int C ;
	scanf("%d" , &C) ;
	for(int c = 1 ; c <= C ; c++){
		int n ;
		scanf("%d" , &n) ;
		printf("Case #%d: %03d\n",c , ans[n]) ;
	}
}
