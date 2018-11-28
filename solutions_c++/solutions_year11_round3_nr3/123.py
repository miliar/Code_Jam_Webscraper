#include <stdio.h>
#include <map>
#include <string>
using namespace std;

int freq[100];

void run(int fall){
	printf("Case #%d: ", fall+1);
	int N,L,H;
	scanf("%d %d %d", &N, &L, &H);
	for(int i=0;i<N;i++){
		scanf("%d", &freq[i]);
	}
	for(int f=L;f<=H;f++){
		int fel=0;
		for(int i=0;i<N;i++){
			if(f%freq[i] != 0 && freq[i]%f != 0){
				fel=1;
				continue;
			}
		}
		if(!fel){
			printf("%d\n", f);
			return;
		}
	}
	printf("NO\n");
}


int main(){
	int N;
	scanf("%d", &N);
	for(int i=0;i<N;i++){
		run(i);
	}	
}