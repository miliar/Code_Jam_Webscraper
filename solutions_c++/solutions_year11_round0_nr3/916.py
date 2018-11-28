#include <iostream>
#include <list>

using namespace std;

int main(){
	int cases;
	int candies;
	cin >> cases;
	for(int i=0; i<cases; i++){
		list<long> values;
		cin >> candies;
		long patrick_sum=0;
		long sean_sum=0;
		for(int j=0; j<candies;j++){
			long value;
			cin >> value;
			values.push_back(value);
			patrick_sum ^= value;
		}
		if(patrick_sum!=0) {
			cout << "Case #" << i+1 << ": NO" <<endl;
		}
		else{
			values.sort();
			values.pop_front();
			while(!values.empty()){
				sean_sum += values.front();
				values.pop_front();
			}
			cout << "Case #" << i+1 << ": "<< sean_sum <<endl;
		}		
	}
	
	return 0;
}
