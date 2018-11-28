#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

struct data {
	char name;
	int loca;
}R[105];
int many,on,bn;
int O[105],B[105];

void input()
{
	char A;
	int N;
	scanf("%d",&many);
	for(int i=0;i<many;i++){
		scanf(" %c%d",&A,&N);
		if(A == 'O') O[on++] = N;
		else B[bn++] = N;
		R[i].name = A;
		R[i].loca = N;
	}
}
void pro()
{
	int Many,oo,bb,onow,bnow,f;
	oo = bb = Many = 0;
	onow = bnow = 1;
	for(int i=1;i<=123456;i++){
		f = 0;
		if(onow == O[oo] && R[Many].name == 'O'){
			oo ++ ;
			Many ++ ;
			f = 1;
		}
		else if(bnow == B[bb] && R[Many].name == 'B'){
			bb ++ ;
			Many ++ ;
			f = 2;
		}
		if(onow > O[oo] && f != 1) onow -- ;
		else if(onow < O[oo] && f != 1) onow ++ ;
		if(bnow > B[bb] && f != 2) bnow -- ;
		else if(bnow < B[bb] && f != 2) bnow ++ ;
		if(Many >= many) {
			printf("%d\n",i);
			break;
		}
	}
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int T,asdf = 1;
	scanf("%d",&T);
	while(T -- ){
		on = bn = 0;
		input();
		printf("Case #%d: ",asdf);
		pro();
		asdf ++ ;
	}
	return 0;
}