#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int n, j, t;
	char v[1000];
	
	scanf("%d",&n);
	
	for(int i=0; i<n; i++){
		scanf("%s",&v);

		printf("Case #%d: ",i+1);
		if(next_permutation( v, v + strlen(v)))
			printf("%s\n",v);
		else{
			t = strlen(v);
			for( j = 0; j < t && v[j] == '0'; j++);
			printf("%c",v[j]);
			for(int k = 0; k <= j; k++)
				printf("0");
			if(j+1<strlen(v))	
				printf("%s",&v[j+1]);
			printf("\n");
		}
	} 
}
