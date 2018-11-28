#include <iostream>
#include <string>
using namespace std;

int main() {
	int numTests;
	cin>>numTests;
	for(int test=0;test<numTests;test++){
		cout<<"Case #"<<(test+1)<<": ";
		int numCandy;
		cin>>numCandy;
		int total=0;
		int sumTotal=0;
		int min=1000000;
		for(int i=0;i<numCandy;i++){
			int candy;
			cin>>candy;
			sumTotal+=candy;
			total=total^candy;
			if(candy<min)
				min=candy;
		}
		if(total!=0)
			cout<<"NO"<<endl;
		else{
			cout<<(sumTotal-min)<<endl;
		}
	}
}
