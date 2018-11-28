#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
const int max_size=10003;

int A[max_size];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	int N,L,H;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
		scanf("%d%d%d",&N,&L,&H);
		for(int i=0;i < N; i++)
			scanf("%d",&A[i]);
		int answ;
		bool good =false, p;
		for(int i=L; i<=H && !good;i++){
			p = true;
			for(int j=0;j < N && p; j++){
				if(A[j]%i != 0 && i%A[j] != 0)
					p  = false;
			}

			if(p){
				good= true;
				answ = i;
			}
		}
		printf("Case #%d: ",t+1);
		if(good)
			printf("%d\n",answ);
		else
			printf("NO\n");
	}

	return 0;
}