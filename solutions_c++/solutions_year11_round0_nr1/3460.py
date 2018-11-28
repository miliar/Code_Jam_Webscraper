#include <fstream>
#include <string>

#define MAX(a,b) ((a>b)?(a):(b))
int abs(int a) 
{
	if (a<0)
		return -a;
	return a;
}

using namespace std;

int T;

int N,M[100][2],index[2],store[2],Time;

char c;

int main(){
	ofstream outputFile;
	outputFile.open ("D:\\outputFile.txt", ofstream::out | ofstream::trunc);
	ifstream input;
	input.open("D:\\input.txt",ifstream::in);
	input >> T;
	for(int t=0;t< T;t++){
		input >> N;
		Time = index[0] = index[1] = store[0] = store[1] = 0;
		for(int i=0;i<N;i++){
			input >> c;
			input >> M[i][0];
			M[i][0]--;
			M[i][1] = (c == 'O')?0:1;
			if(M[i][1] != M[i-1][1]){
				store[M[i-1][1]] = 0;
			}
			int time_to_do = abs(index[M[i][1]] - M[i][0]) + 1;
			int real_time = MAX(time_to_do - store[M[i][1]],1);
			Time += real_time;
			store[M[i][1]] = 0;
			store[1 - M[i][1]] += real_time;
			index[M[i][1]] = M[i][0];

		}
		outputFile << "Case #"<<(t+1)<<": " << Time << endl;
	}
	input.close();
	outputFile.close();
	return 0;
}