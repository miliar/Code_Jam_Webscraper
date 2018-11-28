#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	int T;
	cin>>T;
	
	int total = 0, sum = 0;
	int min = -1;
	int N;
	int tmp;
	
	for(int t = 0; t < T; t++){
		total = 0;
		min = 10000001;
		sum = 0;
		cin >> N;
		for(int i=0; i<N; i++){
			cin>>tmp;
			if(tmp < min){
				min = tmp;
			}
			total ^= tmp;
			sum += tmp;
		}
		
		if(total != 0){
			cout<<"Case #"<< t+1 <<": NO"<<endl;
		}else{
			cout<<"Case #"<< t+1 <<": "<< sum - min<<endl;
		}
	}
	
	return 0;
}