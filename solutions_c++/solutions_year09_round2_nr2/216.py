#include<stdio.h>
#include<algorithm>
using namespace std;

#define MAX 100

char s[MAX];

int main(){

	int T,N;
	int i,n;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%s",s);
		n = strlen(s);

		printf("Case #%d: ",N);
		if(next_permutation(s,s+n)==0){
			sort(s,s+n);
			for(i=0;i<n;i++)if(s[i]!='0')
				break;
			if(i==n){
				printf("%s1\n",s);
				continue;
			}
			swap(s[0],s[i]);
			printf("%c0%s\n",s[0],s+1);
		}
		else
			printf("%s\n",s);


	}

	return 0;
}