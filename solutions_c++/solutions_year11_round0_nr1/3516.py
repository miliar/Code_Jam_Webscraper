#include <cstdlib>
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	int i, j, k;
	ifstream inputfile("data.in");
	ofstream outputfile("data.out");
	int casesCount;
	int N;
	int O, B, time;
	int Otime, Btime;
	char Robot;
	inputfile >> casesCount;
	for(i = 0; i < casesCount; i++) {
		inputfile >> N;
		O = B = 1;
		time = 0;
		Otime = Btime = 0;
		for(j = 0; j < N; j++) {
			inputfile >> Robot;
			inputfile >> k;
			if(Robot == 'O') {
				time += ((abs(k - O) - (time - Otime))>0)?(abs(k - O)  - (time - Otime)) + 1:1;
				Otime = time;
				O = k;
			} else if(Robot == 'B') {
				time += ((abs(k - B) - (time - Btime))>0)?(abs(k - B) - (time - Btime)) + 1:1;
				Btime = time;
				B = k;
			}
		}
		outputfile << "Case #" << i+1 << ": " << time << endl;
	}
	inputfile.close();
	outputfile.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}