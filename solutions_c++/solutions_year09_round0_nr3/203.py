#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
int a[2][500];
char b[510];
char c[]="welcome to code jam";
int main(){
	int N,n,i,j,t,k,next,prev,cccc;
	scanf("%d\n",&N);
	for (n=1;n<=N;n++){
		gets(b);
		t=strlen(b);
		for (i=0;i<t;i++)
		if (b[i]=='w')
			a[0][i]=1;
		else
			a[0][i]=0;
		prev=0;
		next=1;
		for (k=1;k<19;k++){
			for (i=k;i<t;i++){
				a[next][i]=0;
				if (b[i]==c[k]){
					for (j=k-1;j<i;j++)
						a[next][i]+=a[prev][j];
					a[next][i]%=10000;
				}
			//	printf("%d ",a[next][i]);
			}
			//printf("\n");
			next=1-next;
			prev=1-prev;
		}
		cccc=0;
		for (i=18;i<t;i++)
			cccc+=a[prev][i];
		printf("Case #%d: %04d\n",n,cccc%10000);
	}
	return 0;
}
