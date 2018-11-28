#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int play[100][100];
int played[100];
int won[100];
double rpi[100];
int T;

double wp(int t, int except = -1) {
	int w = won[t];
	int p = played[t];
	if (except >= 0 && play[t][except] != -1) {
		p--;
		if (play[t][except] == 1)
			w--;
	}
	//cout << "WP " <<  t << " - " << w << "/" << p << " > " <<except << endl;
	return static_cast<double>(w)/p;
}


double owp(int t) {
	//cout << "OWP " << t << endl;
	double total = 0;
	for (int i = 0; i < T; ++i) {
		if (play[i][t] != -1 && i != t) {
			total += wp(i, t);
			//std::cout << i << " -- " <<  wp(i, t) << std::endl;
		}
	}
	//cout << "played " << played[t] << endl;
	return total / played[t];
}

double oowp(int t) {
	double total = 0;
	for (int i = 0; i < T; ++i) {
		if (play[i][t] != -1 && i != t) {
			total += owp(i);
			//std::cout << i << " -- " <<  wp(i, t) << std::endl;
		}
	}
	//cout << "played " << played[t] << endl;
	return total / played[t];
	return 0;
}

void calc() {
	for (int i = 0; i < T; ++i) {
		//cout <<  i << ". " << wp(i)  << " " << owp(i) << " " << oowp(i) << endl;
		rpi[i] = 0.25 * wp(i) + 0.5 * owp(i) + 0.25 * oowp(i);

	}
}

int main(int argc, char **argv) {
	string ifilename = "rpi.in";
	string ofilename = "rpi.out";
	ifstream ifs(ifilename.c_str());
	ofstream ofs(ofilename.c_str());

	int n, t;
	ifs >> n;
	char c;

	for (int i = 0; i < n; ++i) {

		ifs >> T;
		for (int j = 0; j < T; ++j) {
			played[j] = 0;
			won[j] = 0;
			for (int k = 0; k < T; ++k) {
				ifs >> c;
				if (c == '0') {
					play[j][k] = 0;
					played[j]++;
				} else if (c == '1') {
					play[j][k] = 1;
					won[j]++;
					played[j]++;
				} else if (c == '.') {
					play[j][k] = -1;
				}
			}
		}
		calc();
		//ofs << "Case #" << (i+1) << ": " << res << endl;
		ofs << "Case #" << (i+1) << ": " << endl;
		ofs.precision(10);
		for (int j = 0; j < T; ++j) {
			ofs << rpi[j] << endl;
		}

	}



	ifs.close();
	ofs.close();
	return 0;
}
