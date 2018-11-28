#include <iostream>
#include <vector>
using namespace std;
int main(){
	int T;
	cin>>T;
	for (int t=0;t<T;t++){
		int N;
		cin>>N;
		unsigned int total=0;
		unsigned int min=100000000;
		unsigned int xorTotal=0;
		for (int n=0;n<N;n++){
			int cur;
			cin>>cur;

			total+=cur;

			if (cur<min){
				min=cur;
			}

			xorTotal^=cur;
		}
		cout<<"Case #"<<(t+1)<<": ";
		if (xorTotal==0){
			cout<<(total-min);
		}else{
			cout<<"NO";
		}
		cout<<"\n";
	}
}