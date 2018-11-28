#include<iostream>
using namespace std;

int main(){
	int testcase,N,K;
	cin>>testcase;
	int testcasenumber=1;
	while(testcase--){
		cin>>N;
		cin>>K;
		int i,j=1;
		for(i=0;i<N;i++){
			if(K%2){
			}
			else{
				j=0;
				break;
			}
			K=K/2;
		}
		if(j)	printf("Case #%d: ON\n",testcasenumber);
		else	printf("Case #%d: OFF\n",testcasenumber);
		testcasenumber++;
	}
	return 0;
}
