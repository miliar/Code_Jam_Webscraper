#include<iostream>

using namespace std;

int main(){
	int T,N,S,P,k=1,temp;
	cin>>T;
	while(k<=T){
		cin>>N>>S>>P;
		int total=0;
		for(int i=0;i<N;i++){
			cin>>temp;
			if(P<1)total++;
			if((temp>=(3*P-2))&&(P>=1))total++;
			else if(temp>=(3*P-4)&&(P>=2)){
				if(S>0){
					total++;
					S--;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<total<<endl;
		k++;
	}
	return 0;
}
