#include <iostream>
#include <fstream>
#include <string>

#define MAX(a,b) ((a>b)?(a):(b))
#define ABS(a) ((a>0)?(a):(-(a)))

using namespace std;

int T;

int N,M[100][2],I[2],S[2],Time;

char c;

int main(){
	ofstream output;
	output.open ("E:\\output.txt", ofstream::out | ofstream::trunc);
	ifstream input;
	input.open("E:\\input.txt",ifstream::in);
	cout << input.is_open();
	input >> T;
	for(int t=0;t< T;t++){
		input >> N;
		Time = I[0] = I[1] = S[0] = S[1] = 0;
		for(int i=0;i<N;i++){
			input >> c;
			input >> M[i][0];
			M[i][0]--;
			M[i][1] = (c == 'O')?0:1;
			if(M[i][1] != M[i-1][1]){
				S[M[i-1][1]] = 0;
			}
			int time_to_do = ABS(I[M[i][1]] - M[i][0]) + 1;
			int real_time = MAX(time_to_do - S[M[i][1]],1);
			Time += real_time;
			S[M[i][1]] = 0;
			S[1 - M[i][1]] += real_time;
			I[M[i][1]] = M[i][0];

		}
		output << "Case #"<<(t+1)<<": " << Time << endl;
	}
	input.close();
	output.close();
	return 0;
}