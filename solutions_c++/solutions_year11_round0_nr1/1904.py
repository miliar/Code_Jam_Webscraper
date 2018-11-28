#include <iostream>
#include <fstream>
#include <cassert>

#define ABS(x)		((x) >=  0  ? (x) : -(x))
#define MAX(x, y) ((x) >= (y) ? (x) :  (y))

using namespace std;

void SolveNextCase(int icase, fstream &in, fstream &out){
	int N; char *bot; int *but;
	in >> N; bot = new char [N]; but = new int [N];
	for(int n = 0; n < N; n++)
		in >> bot[n] >> but[n];
	int posO = 1, posB = 1, timeO = 0, timeB = 0;
	for(int n = 0; n < N; n++){
		if			(bot[n] == 'O'){
			timeO += ABS(but[n] - posO) + 1;
			posO = but[n];
			if(timeO <= timeB) timeO = timeB + 1;
		}
		else if	(bot[n] == 'B'){
			timeB += ABS(but[n] - posB) + 1;
			posB = but[n];
			if(timeB <= timeO) timeB = timeO + 1;
		}
		else assert(0);
	}
	out << "Case #" << icase << ": " << MAX(timeO, timeB) << endl;
	delete[] bot; delete[] but;
}

int main(){
	fstream in("in.txt", fstream::in);
	fstream out("out.txt", fstream::out);
	int T; in >> T;
	for(int t = 0; t < T; t++)
		SolveNextCase(t + 1, in, out);
	return 0;
}