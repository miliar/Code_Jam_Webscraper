#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>
#include<map>
using namespace std;

int a,b;
int cycle(int n){
		//cout << "For the num: " << n << endl;
		int buffer[15];
		int occured[10];
		int temp = n;
		int i,j,k;
		int limit = 0;
		j = 0;
		while( temp > 0){
			buffer[j++] = temp%10;
			temp/=10;
		}
		for(i=0;i<=(j-1)/2;i++){
			temp = buffer[i];
			buffer[i] = buffer[j-i-1];
			buffer[j-i-1] = temp;
		}
		int num = 0;
		int flag = 0;
		for(i=1;i<j;i++){
			if( buffer[i] == 0) continue;
			num = 0;
			k = i;
			while( k < j )	num = num*10 + buffer[k++];
			k = 0;
			while( k < i ) num = num*10 + buffer[k++];
			//cout << "num " << num << " " << a << " " << b <<  endl;
			if( num >= a && num <=b && num>n){
				//cout << num << " " << a << " " << b << endl;
				flag = 0;
				for(int y=0; y<limit ;y++){
					if( occured[y] == num ){
				//		cout << "Exists" << endl;
						 flag = 1;break;
					}
				}
				if(!flag){
					occured[limit++] = num;		
				}
			}
		}
		//cout << "limit: " << limit << endl;
		return limit;
}


int main(){
	int i,j,k,t,n,m;
	scanf("%d",&t);
	long long int count = 0;

 	for(k=1;k<=t;k++){
		count = 0;
		scanf("%d %d",&a,&b);
		for( i=a ; i<=b ; i++){
			count += cycle(i);
		}
		printf("Case #%d: %lld\n",k,count);
	}
	return 0;
}
