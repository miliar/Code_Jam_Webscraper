#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	int cnt=0;
	while(t--){
		cnt++;
		int n,i,posB=1,posO=1,timeB=0,timeO=0;
		char hall,grbg;
		int button;
		cin>>n;
//		cin>>grbg;
//		cout<<"see n"<<n<<endl;

		int mxtime=0;
		for(i=0;i<n;i++){
			cin>>hall;
			while(hall!='B' and hall!='O')
				cin>>hall;

			cin>>button;
		
			//cout<<"move "<<i+1<<" "<<hall<<" "<<button<<endl;
			if(hall=='B'){
				timeB=max(timeB+abs(button-posB),mxtime)+1;
				mxtime=timeB;
				posB=button;			
			}
			else{
				timeO=max(timeO+abs(button-posO),mxtime)+1;
				mxtime=timeO;		
				posO=button;			
				
			}
		}
		cout<<"Case #"<<cnt<<": "<<mxtime<<endl;
	}	
	return 0;
}
