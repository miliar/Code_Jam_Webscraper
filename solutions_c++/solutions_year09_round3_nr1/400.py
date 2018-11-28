

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define MAX 62
#define LEN 128

char baseChar[MAX];
bool baseFlag[LEN];

int baseCheck(const string& numStr){
	memset(baseFlag, false, sizeof(bool)*LEN);
	int j=0;
	for(size_t i=0;i<numStr.size();i++){
		if( !baseFlag[numStr[i]]){
			baseChar[j] = numStr[i];
			j++;
		}
		baseFlag[numStr[i]] = true;
	}
	char ch = baseChar[0];
	baseChar[0] = baseChar[1];
	baseChar[1] = ch;
	return j;
}

__int64 output(const string& numStr, int base){
	__int64 sum = 0;
	if(1 == base){
		for(size_t i=0;i<numStr.size();i++){
			sum *= 2;
			sum += 1;
		}
		return sum;
	}
	for(size_t i=0;i<numStr.size();i++){
		sum *= base;
		for(int j=0;j<base;j++)
			if(numStr[i] == baseChar[j]){
				sum += j;
				break;
			}
	}
	return sum;
}

int main(){
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	string numStr;
	for(int t=1;t<=T;t++){
		fin>>numStr;
		int base = baseCheck(numStr);
		fout<<"Case #"<<t<<": ";
		fout<<output(numStr, base)<<endl;
	}
	return 0;
}