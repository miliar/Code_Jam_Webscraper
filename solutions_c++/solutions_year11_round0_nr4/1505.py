#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]){

	ifstream fp;
	fp.open(argv[1]);
	if(fp.is_open()){
		size_t test_case;
		fp>>test_case;
		for(size_t i = 1; i <= test_case;i++){
			size_t n;
			size_t f=0;
			vector<int> v;
			vector<int> gold_v;
			v.clear();
			fp>>n;
			for(size_t j = 0 ; j < n; j++){
				int a;
				fp>>a;
				v.push_back(a);
				gold_v.push_back(a);
			}
			sort(gold_v.begin() , gold_v.end());
			for(size_t j = 0 ; j < n;j++){
				if(gold_v[j] == v[j]){
					f++;
					
				}
			}
			
			double e =(double) (n - f);
			
			cout<<fixed<<"Case #"<<i<<": "<<e<<endl;
		}
	
	}

	return 0; 
}
