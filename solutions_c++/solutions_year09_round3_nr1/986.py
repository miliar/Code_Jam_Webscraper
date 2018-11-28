#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <iostream>


using namespace std;

bool is_exist(vector<char> exist, char x){
	for(int i=0;i<exist.size();i++)
		if(exist[i] == x) return true;
	return false;
}

long long convert(string input, int base){
	map<char, int> mymap;
	vector<char> exist;
	mymap[input[0]] = 1;
	exist.push_back(input[0]);
	int value=0;
	for(int i=1;i<input.size();i++){
		if(!is_exist(exist, input[i])){
			mymap[input[i]] = value;
			exist.push_back(input[i]);
			if(value==0) value+=2;
			else value++;
		}
	}
	double max=0;
	for(int i=0;i<input.size();i++){
		if(max < mymap[input[i]]) max = mymap[input[i]];
		//cout<<mymap[input[i]]<<" ";
	}
	max++;
	long long output=0;
	double exp=0;
	for(int i=input.size()-1;i>=0;i--){
		output += mymap[input[i]]*pow(max, exp);
		exp++;
	}
	return output;
}
	
int main(){
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");
	int t;
	fin>>t;
	for(int ci=1;ci<=t;ci++){
		string instr;
		fin>>instr;
		fout<<"Case #"<<ci<<": ";
		fout<<convert(instr, 2)<<endl;
	}
}