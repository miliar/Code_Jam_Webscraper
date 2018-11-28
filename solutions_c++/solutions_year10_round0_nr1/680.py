#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <set>
#include <ctime>
#include <numeric>
#include <fstream>

using namespace std;

int main(int argc,const char * argv[]){
	istream * _if;
	ostream * _of;
	if (argc > 1)
		_if = new ifstream(argv[1]);
	else
		_if = &cin;
	if (argc > 2)
		_of = new ofstream(argv[2]);
	else
		_of = &cout;
	istream &fin = *_if;
	ostream &fout = *_of;

	int TC;
	fin >> TC;
	for (int tc=1;tc<=TC;tc++){
		int N,K;
		fin >> N >> K;
		string ans = K % (1<<N) == (1<<N) - 1 ? "ON" : "OFF";
		fout << "Case #" << tc << ": " << ans << endl;
		if (_of != &cout)
			cout << "Case #" << tc << ": " << ans << endl;
	}



	delete _if;
	delete _of;

}