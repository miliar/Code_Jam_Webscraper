#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;


void main2(){
	int N = 0, L = 0, H = 0;
	scanf("%d %d %d",&N,&L,&H);
	int i = 0,j=0,num =0,flag =0;
	vector<int>frequency;
	for(i = 0; i<N;i++){
		scanf("%d",&num);
		frequency.push_back(num);
	}
	sort(frequency.begin(),frequency.end());
	int lcm = 0;
	for(i = L;i<=H; i++){
		for(j = 0, flag = 0; j<N; j++){
			if((frequency[j]%i !=0) && (i%frequency[j] != 0)){
				flag = 1;
				break;
			}
		}
		if( flag==1) continue;
		else{ lcm = i; break;}
	}
	if(flag==1) printf("NO\n");
	else printf("%d\n",lcm);
}

int main(){
	int test = 0;
	int a = 0;
	scanf("%d",&test);
	for(a= 1; a<=test;a++){
		printf("Case #%d: ",a);
		main2();
	}
	return(0);
}
