#include<cstdlib>
#include<stdio.h>
#include<math.h>

int dig(int );
int change(int, int, int);

int main(){
	int T, A, B, ans, check;

	scanf("%d ", &T);
    for(int i=0; i<T; i++){
	    scanf("%d%d", &A, &B);
	    ans=0;
		for(int j=A; j<B; j++){
		    for(int k=1; k<dig(j); k++){
			    check=0;
			    for(int l=1; l<k; l++){
				    if(change(j, dig(j), k)==change(j, dig(j), l))  check=1;
				}
				if(change(j, dig(j), k)>j&&change(j, dig(j), k)<=B&&check==0)  ans++;
			}
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
    return 0;
}

int dig(int a){
    int i=0;
	while(a>0){
	    a/=10;
	    i++;
	}
	return i;
}

int change(int number, int dig, int set){
    return number/(int)(pow(10, (double)set)+0.1)+(number%(int)(pow(10, (double)set)+0.1))*((int)(pow(10, (double)(dig-set))+0.1));
}
