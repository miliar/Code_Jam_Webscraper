#include<stdio.h>
#include<algorithm>
using namespace std;

#define INF 1000000000

int p[20];
int k;
char s[10000],t[10000];

int main(){

	int T,N;
	int i,j;
	int cmin;//,mx;
	char last;

	scanf("%d",&T);

	for(N=1;N<=T;N++){

		scanf("%d%s",&k,s);
		
		for(i=0;i<k;i++)
			p[i] = i;

		cmin = INF;
		do{
			for(j=0;s[j];j+=k){
				for(i=0;i<k;i++)
					t[j+i] = s[j + p[i]];
			}
			t[j] = 0;

//			printf(">> %s\n",t);

			last = t[0];
			j = 1;
			for(i=1;t[i];i++){
				if(t[i]==last);
				else{
					j++;
					last = t[i];
				}
			}

			if(j < cmin)
				cmin = j;
		}while(next_permutation(p,p+k));

		printf("Case #%d: %d\n",N,cmin);
	}

	return 0;
}