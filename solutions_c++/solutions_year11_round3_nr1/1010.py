#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>

using namespace std;

#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) (EQ((a).real(),(b).real()) && EQ((a).imag(),(b).imag()))

typedef complex<double> P;
typedef long long ll;

const int MAX_SIZE = 10000;

int T;
int R;
int C;
vector<string> field;

bool solve(){
	for(int i = 0; i < R - 1; i++){
		for(int j = 0; j < C - 1; j++){
			if(field[i][j] == '#'){
				if(field[i+1][j] == '#' && field[i][j+1] == '#' && field[i+1][j+1] == '#'){
					field[i][j] = '/';
					field[i+1][j+1] = '/';
					field[i][j+1] = '\\';
					field[i+1][j] = '\\';
				}
			}
		}
	}
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if(field[i][j] == '#')
				return false;
		}
	}
	return true;
}

int main(){

	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	ifs >> T;
	for(int i = 0; i < T; i++){
		ifs >> R;
		ifs >> C;
		for(int i = 0; i < R; i++){
			string s;
			ifs >> s;
			field.push_back(s);
		}

		ofs << "Case #" << i+1 << ":" << endl;
		//cout << "Case #" << i+1 << ":" << endl;
		if(solve()){
			for(int i = 0; i < R; i++){
				ofs << field[i] << endl;
				//cout << field[i] << endl;
			}
		}
		else{
			ofs << "Impossible" << endl;
			//cout << "Impossible" << endl;
		}
		field.clear();
	}

	int x;
	cin >> x;

	return 0;
}