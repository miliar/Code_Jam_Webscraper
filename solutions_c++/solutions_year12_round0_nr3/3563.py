#define MAX 20000
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include<map>
#include<cmath>

using namespace std;

int achou(int feitos[MAX][2], int total, int x, int i){
	for(int j=0;j<total;j++){
		if(((feitos)[j][0]==x&&(feitos)[j][1]==i)||((feitos)[j][1]==x&&(feitos)[j][0]==i))
			return 1;
	}
	return 0;
}

int main () {
	int t2,t=0;
	int a, b;
	int x;
	int div;
	int temp=0, tam;
	int total=0;
	int feitos[MAX][2];
	int k;
	
	int y;
	int tam2;
	cin>>t2;
	for(int h=0;h<t2;h++){
		cin>>a>>b;
		t++;
		cout<<"Case #"<<t<<": ";
		total=0;temp=0;tam=0;div=0;y=0;tam2=0;x=0;
		for(int i=a;i<=b;i++){
			
			temp=i;
			tam=-1;
			while(temp!=0){
				temp/=10;
				tam++;
			}
			div=10;
			
			k=0;
			while(div<=pow(10,tam)){
				tam2=0;
				temp=(i/div);
				tam2=0;
				while(temp!=0){
					temp/=10;
					tam2++;
				}
				x=(i/div)+(i%div)*pow(10,tam2);
				div*=10;
				//cout<<"o"<<x<<" "<<i<<"o\n";
				
				if(!(x>b||x<a||x==i||achou(feitos,total,x,i)==1))
				{
				//cout<<"-"<<x<<" "<<i<<"-";
				
				//cout<<"X"<<x<<" "<<i<<"X\n";
				feitos[total][0]=x;
				feitos[total][1]=i;
				total++;
				}
				
			}
		}
		cout<<total<<endl;
	}
	return 0;
}
