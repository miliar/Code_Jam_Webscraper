
#include <iostream>
using namespace std;

int main(){

int nt,size, min,curr, sum;
int num1[20];
cin >> nt;
for(int it = 0; it<nt; it++){
	for(int i = 0; i < 20;i++){
		num1[i]=0;
	}
	min=0;
	sum=0;
	cin>>size;
	for(int i = 0; i < size;i++){
		cin >> curr;
		sum+=curr;
		if(i==0 || curr<min) min=curr;
		int j = 0;
		while(curr!=0){
			num1[j]=((curr%2)+num1[j])%2;
			curr=curr>>1;
			j++;
		}
	}
	int allzero=1;
	for(int i = 0; i < 20;i++){
		if(num1[i]== 1) allzero=0;
	}
	if(allzero==0) cout<<"Case #"<<it+1<<": NO"<<endl;
	else cout<<"Case #"<<it+1<<": "<<sum-min<<endl;
}

return 0;
}

