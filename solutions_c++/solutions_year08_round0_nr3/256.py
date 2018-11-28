#include <iostream>
#include "test_case.h"
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
	ifstream fin;
	fin.open("C-large.in");
	if(!fin){
		cout<<"open input failed"<<endl;
		return -1;
	}
	ofstream fout;
	fout.open("output.txt");
	if(!fout){
		cout<<"open output failed"<<endl;
		return -1;
	}

	int tn = 0;
	fin>>tn; 
	test_case** tc = new test_case* [tn];
	for(int i = 0; i < tn; i++){
		tc[i] = new test_case(fin);
		fout<<"Case #"<<i+1<<": ";
		fout.setf(fout.showpoint);
		fout.precision(6);
		fout.setf(ios::fixed); 
		fout<<tc[i]->hit_pb()<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}