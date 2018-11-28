#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>

//AAAAAAA

using namespace std;

int T;

struct Case
{
};

vector<string> cases;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in);
    
    ifs >> T;

	string tmp;
	for(int i=0;i<T;++i){
		ifs >> tmp;
		cases.push_back(tmp);
	}

	return 0;
}

unsigned long long solve(string str){

	vector<int> count(255);
	vector<int> val(255,-1);

	int base=0;
	int len = str.size();
	for(int i = 0; i < len; ++i){
		if(count[str[i]]==0){
			base++;
		}
		count[str[i]]++;
	}

	if(base==1)base=2;

	unsigned long long num=0;
	unsigned long long nowbase=1;
	for(int i = 0; i < len-1; ++i){nowbase*=base;}
	int sym=0;

	for(int i = 0; i < len; ++i){
		if(val[str[i]]==-1){
			val[str[i]]=sym;
			if(sym==0){val[str[i]]=1;}
			if(sym==1){val[str[i]]=0;}
			sym++;
		}
		num+=val[str[i]]*nowbase;
		nowbase/=base;
	}

	return num;
}


#define INFILE "A-large.in"

int main(){
	input_read(INFILE);
	ofstream o(INFILE ".out");

	int n = 0;

//#define o cout
	for(vector<string>::iterator i = cases.begin(), e = cases.end(); i != e; ++i){
		o << "Case #" << ++n << ": " << solve(*i) << endl;
	}
	
}
