#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

typedef unsigned long long uint64;

int main(){
	int cases = 0;
	cin>>cases;
	for(int i = 0; i < cases; i++){
		uint64 totalEuros = 0, R = 0, k = 0, N = 0;
		cin>>R>>k>>N;
		vector<uint64> groups;
		for(int j = 0; j < N; j++){
			uint64 size = 0;
			cin>>size;
			groups.push_back(size);
		}
		for(int p = 0; p < R; p++){
			vector<uint64> temp = groups;
			uint64 capacity = 0;
			int counter = 0;
			while(true && counter < groups.size()){
				counter++;
				capacity = capacity + groups[0];
				if(capacity > k)	break;
				vector<uint64>::iterator vit = groups.begin();
				uint64 firstValue = *vit;
				totalEuros = totalEuros + *vit;
				groups.erase(vit);
				if(groups.size() != 0){					
					groups.push_back(firstValue);
				}
				else{
					groups = temp;
					break;
				}
			}
		}
		cout<<"Case #"<<i + 1<<": "<<totalEuros<<endl;
	}	
	return 0;
}
