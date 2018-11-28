#include<string>
#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
	int arr[]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);
	int test;
	scanf("%d",&test);
	int i=0;
	char ch;
	scanf("%c",&ch);
		if(ch == '\n'){
	 printf("Case #%d: ",++i);
		}
	while(test){
		scanf("%c",&ch);
		if(ch == '\n'){
			if(--test) printf("%cCase #%d: ",ch,++i);
		}
		else if(ch==EOF)break;
		else if(ch<=122 && ch>=97)
			printf("%c",97+arr[ch-97]);
		else	
			printf("%c",ch);
	}	
}