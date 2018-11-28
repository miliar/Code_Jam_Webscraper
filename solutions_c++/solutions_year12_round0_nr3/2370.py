#include<vector>
#include<iostream>
#include<cmath>
using namespace std;
typedef long long int LL;
LL countdig(LL num){
	LL dig=0;
	while(num!=0){
		dig++;
		num/=10;
	}
	return dig;
}
LL shift(LL num,LL digit,LL places){
	LL newnum=0;
	if(num%(LL)pow(10,places)==0) return num;
	for(LL i=0;i<places;i++){
		LL last=num%10;
		newnum=last*pow(10,digit-1)+num/10;
		num=newnum;
	}
	//cout<<newnum<<endl;
	return newnum;
}
bool issaved(vector <LL> &saved,LL num){
	for(int i=0;i<saved.size();i++){
		if(saved[i]==num) return true;
	}
	return false;
}
int main(){
	LL t;
	cin>>t;
	for(LL i=1;i<=t;i++){
		LL a,b;
		LL count=0;
		cin>>a>>b;
		LL dig=countdig(a);
		for(LL j=a;j<=b;j++){
		vector <LL> saved;
			for(LL k=1;k<=dig;k++){
				LL shiftednum=shift(j,dig,k);
				if(dig==countdig(shiftednum)&&shiftednum<=b&&shiftednum>j&&!issaved(saved,shiftednum)){
					count++;
					saved.push_back(shiftednum);	
				}
			}	
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
