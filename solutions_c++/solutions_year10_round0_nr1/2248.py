#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;
int strToInt(string str){
	int num;
	istringstream is(str);
	is >> num;
	return num;
}
string intToStr(int num){
	ostringstream os;
	os << num;
	return os.str();
}

int main(){
	int T,N,K;
	string ss;
	ifstream fin("A-large.in");
	ofstream fout("A.out");
	getline(fin,ss);
	T = strToInt(ss);
	for(int t=1;t<=T;t++){
		getline(fin,ss);
		istringstream is(ss);
		is>>N>>K;
		int onK = 1<<N;
		string state = "OFF";
		if(K%onK==(onK-1))
			state = "ON";
		fout<<"Case #"<<t<<": "<<state<<endl;
	}
	return 0;
}