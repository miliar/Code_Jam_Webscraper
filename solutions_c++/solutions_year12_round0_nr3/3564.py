#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

void line(string startstr, string endstr) {
	int count = 0;
	int start = atoi(startstr.c_str());
	int end = atoi(endstr.c_str());

	int width = startstr.length();

	int shiftstart[width-1];

	for(int w=0;w<(width-1);w++) {
		string shiftstr = "";
		for(int i=0;i<width;i++) shiftstr += startstr[(i+w+1)%width];

		shiftstart[w] = atoi(shiftstr.c_str());
	}

	
	for(int i=0;i<(end-start);i++) {
		int shiftvalue[width-1];
		for(int w=0;w<(width-1);w++) {
			if(i > 0 && (start+i)%(int)pow(10,width-w-1) == 0) {
				shiftstart[w]+=1;
			}
			shiftvalue[w] = (shiftstart[w]+i*(int)pow(10,w+1))%(int)pow(10,width);
		}

		for(int w=0;w<(width-1);w++) {
			for(int w1=0;w1<(width-1);w1++) {
				if(w1 != w && shiftvalue[w1] == shiftvalue[w]) {
					shiftvalue[w1] = 0;
				}
			}
			if(shiftvalue[w]<=end && shiftvalue[w]>=(start+i) && shiftvalue[w] != (start+i)) count++;
		}
	}


	cout << count << endl;
}

int main() {
	fstream file;
	file.open("C-small-attempt0.in", fstream::in);

	int T;
	file >> T;

	for(int i=1;i<=T;i++) {
		string A, B;
		file >> A;
		file >> B;

		cout << "Case #" << i << ": ";
		line(A,B);
	}
}
