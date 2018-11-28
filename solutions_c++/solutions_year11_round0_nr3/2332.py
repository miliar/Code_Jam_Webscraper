
//Problem C

#include <iostream>

using namespace std;


int n;
int candy[1000];

int main(){
	int t;
	int i,j;
	int mincandy;
	int sum;
	int xorsum;

	cin>>t;
	for (i=0;i<t;i++){
		sum=0;
		xorsum=0;
		mincandy=1000000;
		cin>>n;
		for (j=0;j<n;j++){
			cin>>candy[j];
			xorsum^=candy[j];
			sum+=candy[j];
			if (candy[j]<mincandy) mincandy=candy[j];
		}
		cout<<"Case #"<<(i+1)<<": ";
		if (xorsum!=0){
			cout<<"NO";
		} else {
			cout<<(sum-mincandy);
		}
		cout<<endl;
	}
}
