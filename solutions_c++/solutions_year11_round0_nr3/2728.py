#include <iostream>
using namespace std;

int ar[15], maks, n;

void parse(int permute){
	int leftPat = 0, rightPat = 0;
	int leftSean = 0, rightSean = 0;
	
	for (int i = 0 ; i < n ; i ++){
		if (permute%2==0){
			leftPat ^= ar[i];
			leftSean += ar[i];
		}else{
			rightPat ^= ar[i];
			rightSean += ar[i];
		}
		permute/=2;
	}
	
	if (leftPat==rightPat){
		maks = max(maks, max(leftSean, rightSean));
	}
}

int main(){
	int t, counter;
	scanf("%d", &t);
	
	for (int k = 1 ; k <= t ; k ++){
		scanf("%d", &n);
		maks = -1;
		for (int i = 0 ; i < n ; i ++){
			scanf("%d", &ar[i]);
		}
		
		counter = 1 << n;
		
		for (int count = 1 ; count < counter-1 ; count++){
			parse(count);
		}
		
		if (maks==-1)
			printf("Case #%d: NO\n", k);
		else
			printf("Case #%d: %d\n", k, maks);
	}
	
	return 0;
}
