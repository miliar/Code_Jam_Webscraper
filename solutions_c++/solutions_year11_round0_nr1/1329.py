#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main(){
	int t,n;
	cin>>t;
	char c;
	int state=2,transtime=0,res=0,button,poso,posb;
	for(int j =1;j<=t;j++){
		cin>>n;
		res = 0;
		transtime = 0;
		state = 2;
		poso = 1;
		posb = 1;
		for(int i = 0;i<n;i++){
			cin>>c;
			if(c == 'O'){
				cin>>button;
				if(state == 0){
					res+=(fabs(button-poso)+1);
					transtime += (fabs(button-poso)+1);
					}
				else{
					if(transtime >= fabs(button - poso)){
						transtime = 1;
						res+=1;
					}
					else{
						res+=( fabs(button - poso) - transtime +1);
						transtime = fabs(button - poso) - transtime +1;
					}
				}
			poso = button;
			state = 0;
			}
			else{
				cin>>button;
				if(state == 1){
					res+=(fabs(button-posb)+1);
					transtime += (fabs(button-posb)+1);
					}
				else{
					if(transtime >= fabs(button - posb)){
						transtime = 1;
						res+=1;
					}
					else{
						res+=( fabs(button - posb) - transtime +1);
						transtime = fabs(button - posb) - transtime +1;
					}
				}
			posb = button;
			state = 1;
			}
		}
		printf("Case #%d: %d\n",j,res);
	}
	return 0;}
