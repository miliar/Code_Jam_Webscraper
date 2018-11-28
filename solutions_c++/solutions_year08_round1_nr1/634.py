#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <map>
#include <vector>

#define TAB_SIZE 2000

using namespace std;



int min(int a, int b){
	if (a < b)
		return a;
	else
		return b;
}

int main(){
//ofstream fout("A-small.out");
//ifstream f("A-small.in");
ofstream fout("A-large.out");
ifstream f("A-large.in");

int i, j, N, big, n1, n2, small;
long long res, tmp;
vector<long long> w1, w2;
const char * rest;
string line;


	//getline(f,line);
	//sscanf(line.c_str(), "%d", &N);
	f >> N;
	for (big = 1; big <= N; big++){
		//getline(f,line);
		//sscanf(line.c_str(), "%d", &n1);
		f >> n1;
		//getline(f,line);
		//rest = line.c_str();
		for (small = 0; small < n1; small++){
			//getline(f,line);
		        //sscanf(rest, "%d", &x[small]);
			//rest = rest + 4;
			f >> tmp;
			w1.push_back(tmp);
			//cout << tmp << " ";

		}
		cout << endl;
		//getline(f,line);
		//sscanf(line.c_str(), "%d", &n1);
		//getline(f,line);
		//rest = line.c_str();
		
		for (small = 0; small < n1; small++){
			//getline(f,line);
		        //scanf(rest, "%d%s", &y[small], rest);
			f >> tmp;
			//getline(f,line);
			//cout << tmp << " ";

			w2.push_back(tmp);

		}
		cout << endl;
		sort(w1.begin(), w1.end());
		sort(w2.rbegin(), w2.rend()); 

		/*for (j = 0; j < n1; j++){
			cout<< w1.at(j) << " ";
		}*/
		//cout << endl;
	
		res = 0;
		for (i = 0; i < n1; i++){
			res = res + w1.at(i) * w2.at(i);
		}
		//cout << res << endl;
		fout << "Case #" << big << ": " << res << endl;
		w1.clear();
		w2.clear();
		//getline(f, line);
	}/* for big */
	fout << flush;
	fout.close();
	f.close();


	return 0;
} /* main */
