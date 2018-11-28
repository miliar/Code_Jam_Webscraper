#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main(){

	ifstream fin ("a.in", ios::in);
	ofstream fout("a.out", ios::out);
	int T;

	fin>>T;

	int n;
	for (n=0;n<T;n++){
		int N;
		fin>>N;
		int b;
		int p;
		char c;
		map<char,int> time, pos;
		time['O'] = 0;
		time['B'] = 0;
		pos['O'] = 1;
		pos['B'] = 1;
		int movetime;
		int currenttime = 0;
		for (b=0;b<N;b++){
			fin>>c>>p;
			movetime = abs(p-pos[c]);
			time[c] += movetime;
			currenttime = max(time['O'],time['B']);
			time[c] = currenttime+1;
			pos[c] = p;
		}
		fout<<"Case #"<<n+1<<": "<<max(time['O'],time['B'])<<endl;
	}

	fout.close();
	return 0;
}

