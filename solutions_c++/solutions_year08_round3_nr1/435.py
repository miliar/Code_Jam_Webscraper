#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <iterator>
#include <algorithm>


using namespace std;

int main(void){
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	
	int num = 0;
	int P,K,L = 0;
	long temp = 0;
	vector<long> vec;
	long long res = 0;
	
	fin>>num;
	for(int i = 0; i < num ; i++){
		res = 0;
		vec.clear();
		
		fin>>P>>K>>L;
		
		if(P*K < L){
			// out
			fout<<"Case #"<<i+1<<": Impossible"<<endl;
		} else {
			
			for(int j = 0; j < L; j++){
				fin>>temp;
				vec.push_back(temp);
			}
			
			sort(vec.begin(),vec.end());
			
			vector<long>::reverse_iterator r_it = vec.rbegin();
			for(int k  = 0; k < L ; k++ , r_it++){
					res += (*r_it) * (k/K + 1);
			}
			
			fout<<"Case #"<<i+1<<": "<<res<<endl;
		}
	}


	return 0;
}

