#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main(){
	
	int T,A,B,temp,k=1;
	cin>>T;
	while(k<=T){
		cin>>A>>B;int total=0;
		int val[1000]={0};
		for(int i=A;i<B;i++){
			if(i<10){}
			else if(i<100){
				temp=(i%10)*10+(i/10);
				if((temp>i)&&(val[temp]!=i)&&(temp<=B)){
					total++;
					val[temp]=i;
				}
			}
			else{
				temp=(i%10)*100+(i/10);
				if((temp>i)&&(val[temp]!=i)&&(temp<=B)){
					total++;
					val[temp]=i;
				}
				temp=(i%100)*10+(i/100);
				if((temp>i)&&(val[temp]!=i)&&(temp<=B)){
					total++;
					val[temp]=i;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<total<<endl;
		k++;
	}
	return 0;
}
