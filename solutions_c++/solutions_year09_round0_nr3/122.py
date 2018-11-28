#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int n;

fstream in, out;

string wanted = "welcome to code jam";

int val[510][20];
int len;

int main() {
	in.open("prob3.in", fstream::in);
	out.open("prob3.out", fstream::out);

	in >> n;
	
	char temp[1000];
	in.getline(temp, 1000, '\n');
    for (int i = 0; i < n; i++) {

		for (int aaaa = 0; aaaa < 1000; aaaa++) {
			temp[aaaa] = '1';
		}
        in.getline(temp, 1000, '\n');
		
		for (int aaaaa = 0; aaaaa < 1000; aaaaa++) {
			if (temp[aaaaa] == '1') {
				len = aaaaa;
				aaaaa = 100000;
			}
		}

		if (wanted.at(18) == temp[len - 1]) {
			val[len - 1][18] = 1;
		} else {
			val[len - 1][18] = 0;
		}
		for (int ii = len - 2; ii >=0; ii--) {
			if (wanted.at(18) == temp[ii]) {
				val[ii][18] = (val[ii+1][18] + 1) % 10000;
			} else {
				val[ii][18] = val[ii+1][18];
			}
		}

		for (int x = 17; x >= 0; x--) {
			val[len - 1][x] = 0;
			for (int y = len - 2; y >= 0; y--) {
				if (wanted.at(x) == temp[y]) {
					val[y][x] = (val[y + 1][x] + val[y+1][x+1]) % 10000;
				} else {
					val[y][x] = val[y+1][x];
				}
			}
		}
		out << "Case #" << i + 1 << ": ";
		
		int numzeros = 0;
		if (val[0][0] < 1000) {
			numzeros++;
		}
		if (val[0][0] < 100) {
			numzeros++;
		}
		if (val[0][0] < 10) {
			numzeros++;
		}

		for (int aa = 0; aa < numzeros; aa++) {
			out << "0";
		}
		out	<< val[0][0] << endl;
    }
    
	in.close();
	out.close();

	return 0;
}
