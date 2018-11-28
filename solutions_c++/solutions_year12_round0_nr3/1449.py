#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<iostream>
#include<cmath>
#include<string>
#define MEX 2000002
using namespace std;

int store[MEX];
int hash[10]={0,0,1,3,6,10,15,21,28,36};

int getNext(int num) {

	int temp=num, c=0;
	int i=0, t=0, flag=0;
	char str[9];

	sprintf(str,"%d",num);
	c = strlen(str);

	while(temp) {
		t=temp%10;
		temp=temp/10;
		++i;
		if(t!=0) {
			break;
		}
	}
	t = (int)pow(10,i);
	c = (int)pow(10,(c-i));
	return (num/t) + (num%t)*c;
}

int main() {

	int test=0, count=1, A=0, B=0, i=0;
	int result=0, nextNum=0, comb=0;	
	
	scanf("%d",&test);
	while(count <= test) {
		scanf("%d %d",&A,&B);
		for(i=A, result=0; i<=B; ++i) {
			if(store[i]==0) {
				comb=1;
				nextNum = getNext(i);
				while(i!= nextNum) {
					if(nextNum <= B && nextNum > i) {
						store[nextNum]=1;
						++comb;							
					}
					nextNum = getNext(nextNum);
				}
				result+=hash[comb];
			}
		}
		printf("Case #%d: %d\n",count, result);
		memset(store, 0, (B+1)*sizeof(int));
		++count;
	}

	return 0;
}
