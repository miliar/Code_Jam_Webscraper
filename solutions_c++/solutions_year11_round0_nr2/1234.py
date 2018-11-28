#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

ifstream fin;
ofstream out;

vector<char> list;
int table[256][256];
int pos[256][256];
void init() {
	for(int i = 0 ; i < 256; i++)
		for(int j = 0; j < 256; j++){
			table[i][j] = 0;
			pos[i][j] = 0;
		}
	list.clear();
}

void add(char a) {
	//cout << "ADD" << a << endl;
	if(list.size() <= 0) {
		list.push_back(a);
		return;
	}
	int back = list.back();
	if(table[back][a] > 0) {
		list.pop_back();
		//cout << "COMBIME" << endl;
		return add((char)table[back][a]);
	}
	for(int i = 0; i < list.size(); i++){
		if(pos[list[i]][a] < 0){
			list.clear();
			//cout << "CLEAR" << endl;
			return;
		}
	}
	list.push_back(a);
}
void process() {
	int num;
	string info;
	fin >> num;
	for(int i = 0; i < num; i++) {
		fin >> info;
		int a = (int)info[0];
		int b = (int)info[1];
		table[a][b] = (int)info[2];
		table[b][a] = (int)info[2];
	}
	fin >> num;
	for(int i = 0; i < num; i++) {
		fin >> info;
		int a = (int)info[0];
		int b = (int)info[1];
		pos[a][b] = -1;
		pos[b][a] = -1;
	}
	fin >> num;
	fin >> info;
	for(int i = 0; i < info.size(); i++) {
		add(info[i]);
	}

}


int main(int argc,char** argv) {
	fin.open(argv[1]);
	out.open(argv[2]);

	int cnum = 0;
	fin >> cnum;

	for(int i = 0; i < cnum; i++) {
		init();
		process();
		out << "Case #" << i + 1 << ": ";
		if(list.size() <= 0) {
			out << "[]" << endl;
			continue;
		}
		bool flag = true;
		for(int j = 0; j < list.size(); j++){
			if(flag) {
				out << "[" << list[j];
				flag = false;
			} else {
				out << ", " << list[j];
			}
		}
		out << "]" << endl;
	}


	fin.close();
	out.close();
}
