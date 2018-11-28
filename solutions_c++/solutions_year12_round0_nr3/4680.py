#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int main(){
	
	
	int t,i,j,k,m,n,l,b,ten,total,digit,x,a;
	cin>>t;
	
	for(i=0;i<t;i++){
		cin>>n;
		cin>>m;
		total=0;
		digit=0;
		for(j=n;j<=m;j++){
			a=j;
			b=j;
			digit=0;
			while(b>0){
				b=b/10;
				digit++;
			}
			ten=1;
			for(k=1;k<digit;k++){
				ten=ten*10;
			}
			b=j;
			int one,two,three,four;
			for(k=0;k<digit;k++){
				x=b%10;
				//if(x==0)break;
				b=b/10;
				b=b+ten*x;
				if(k==0)one=b;
				if(k==1){
					two=b;
					if(two==one)continue;
				}
				if(k==2){
					three=b;
					if(three==two || three==one)continue;
				}
				if(k==3){
					four=b;
					if(four==three || four==two || four==one)continue;
				}
				if(b>j && b<=m)total++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<total<<endl;
	}


return 0;
}
