#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

int toInt(const string &s){
	stringstream ss(s);
	int ret;
	ss >> ret;
	return ret;
}


int main(int argc,const char * argv[]){
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int TC;
	string line;
	getline(fin,line);
	TC=toInt(line);
	for (int tc=1;tc<=TC;tc++){
		int S,C;
		getline(fin,line);
		S=toInt(line);
		map <string,int> eng;
		for (int i=0;i<S;i++){
			string s;
			getline(fin,s);
			eng[s] = i +1;
		}
		getline(fin,line);
		C=toInt(line);
		int mem[103];
		memset(mem,0,sizeof(mem));
		for (int i=0;i<C;i++){
			string s;
			getline(fin,s);
			int j = eng[s];
			int val = 1000000000;
			for (int k = 1;k <= S;k++)
				if (k != j)
					val = min(val,mem[k] + 1);
			mem[j] = val;
		}

		int val = 1000000000;
		for (int k = 1;k <= S;k++)
			val = min(val,mem[k]);
		fout << "Case #" << tc << ": " << val << endl;
	}

}