
#include <iostream>
#include <fstream>
#include <bitset>

using namespace std;

int main(){
	ifstream input("input.txt");
	ofstream output("output.txt");
	size_t T;
	input >> T;
	size_t N,K;
	bool isLight;
	for(size_t i = 0; i < T;i++){
		input >> N >> K;
		isLight = true;
		for(size_t j = 0;j< N;j++){
			if(!(K & (1<<(j)))){
				isLight = false;
				break;
			}
		}
		output << "Case #"<<(i+1)<<": " << (isLight?"ON":"OFF") << "\n";
	}
	return 0;
}