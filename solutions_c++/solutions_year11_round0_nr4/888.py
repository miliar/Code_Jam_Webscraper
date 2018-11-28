#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main(){
	int T,n;
	int i,j,k,z;
	
	j = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		
		for(i=1,z=0;i<=n;i++){
			scanf("%d",&k);
			if(k != i) z++;
		}
		printf("Case #%d: %.6lf\n",j,double(z));
		j++;
	}
	return 0;
}
	
