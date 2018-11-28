#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;
//input
//3 5 4
//abc
//bca
//dac
//dbc
//cba
//(ab)(bc)(ca)
//abc
//(abc)(abc)(abc)
//(zyx)bc

int len=15;
int numDic=5000;
int numPat =500;

vector<string> dics;
vector<string> patterns;
typedef vector<string>::const_iterator STR_ITER;
ofstream outfile("out_file"); 
ifstream infile("A-large.in");

int solve(const string& pattern)
{
	int rst=0;

	vector<string> parts;
	string::size_type pos=1, prev_pos=0;
	while(prev_pos < pattern.length()){
		if(pattern[prev_pos] == '('){
			prev_pos++;
			pos = pattern.find(')',pos);
			parts.push_back(pattern.substr(prev_pos,pos-prev_pos));
			prev_pos = pos +1;	pos = prev_pos +1;
		}else{
			parts.push_back(pattern.substr(prev_pos,pos-prev_pos));
			prev_pos = pos; pos = prev_pos +1;
		}
	}
	STR_ITER itr_word;

	for(itr_word =dics.begin(); itr_word !=dics.end(); itr_word++){
		int i;
		for (i=0; i<len; i++){
			if(parts[i].find((*itr_word)[i]) != string::npos)
				continue;
			else
				break;
		}
		if(i==len)
			rst++;
	}

	return rst;
}

void init()
{
	assert(outfile && infile);

	infile >> len;	infile >> numDic;	infile >> numPat;

	string word;
	int num = numDic;
	while(num--){
		infile >> word;
		dics.push_back(word);
	}
	num = numPat;
	while(num--){
		infile >> word;
		patterns.push_back(word);
	}
}

int main()
{
	init();
	
	//Case #1: 2
	int num=1;
	STR_ITER itr;
	for(itr= patterns.begin(); itr != patterns.end(); itr++)
	{
		int rst= solve(*itr);
		outfile<<"Case #"<<num++<<": "<<rst<<"\n";
	}
	return 0;
}