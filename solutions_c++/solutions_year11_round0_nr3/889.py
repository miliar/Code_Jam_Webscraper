#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main(){
	int T,n;
	int i,j,k,x,y,z;;
	
	j = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		
		x = y = 0;
		z = 100000000;
		for(i=0;i<n;i++){
			scanf("%d",&k);
			x = (x^k);
			y += k;
			z = min(z,k);
		}
		
		if(x != 0) printf("Case #%d: NO\n",j);
		else printf("Case #%d: %d\n",j,y-z);
		j++;
	}
	return 0;
}
