#include <iostream>
#include <fstream>
#include <string>

#define MAX(a,b) ((a>b)?(a):(b))
#define ABS(a) ((a>0)?(a):(-(a)))

using namespace std;

int T;

int N,M[100][2],I[2],S[2],Result;

char c;

int main(){
	ofstream output;
	output.open ("E:\\output.txt", ofstream::out | ofstream::trunc);
	ifstream input;
	input.open("E:\\input.txt",ifstream::in);
	input >> T;
	for(int t=0;t< T;t++){
		input >> N;
		int min = INT_MAX,temp,sum = 0,xor = 0;
		for(int i=0;i<N;i++){
			input >> temp;
			xor ^= temp;
			sum += temp;
			if(min > temp){
				min = temp;
			}
		}
		sum -= min;
		if(xor == 0){
			output << "Case #"<<(t+1)<<": " << sum << endl;
		}else{
			output << "Case #"<<(t+1)<<": " << "NO" << endl;
		}
	}
	input.close();
	output.close();
	return 0;
}