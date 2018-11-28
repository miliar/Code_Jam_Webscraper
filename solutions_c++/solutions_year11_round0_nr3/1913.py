#include <iostream>
#include <fstream>
#include <cassert>

#define MIN(x, y) ((x) < (y) ? (x) : (y))

using namespace std;

void SolveCase(int casen, fstream &in, fstream &out){
	int N, *C;
	in >> N; C = new int [N];
	for(int n = 0; n < N; n++) in >> C[n];
	int sum = 0, xorsum = 0, min = C[0];
	for(int n = 0; n < N; n++){
		min = MIN(min, C[n]);
		xorsum ^= C[n];
		sum += C[n];
	}
	out << "Case #" << casen << ": ";
	if(xorsum != 0) out << "NO";
	else out << sum - min;
	out << endl;
	delete[] C;
}

int main(){
	fstream in("in.txt", fstream::in);
	fstream out("out.txt", fstream::out);
	int T; in >> T;
	for(int t = 0; t < T; t++)
		SolveCase(t + 1, in, out);
	return 0;
}
