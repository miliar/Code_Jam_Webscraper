#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

vector<string> dics;
vector<string> patterns;
typedef vector<string>::const_iterator STR_ITER;
string filename_in("C-small-attempt0.in");
string filename_out=(filename_in+".out");
ofstream outfile(filename_out.c_str()); 
ifstream infile(filename_in.c_str());


int testcase;
char STR[]="welcome to code jam";
//char STR[]="oe";
char Line[500];


//3
//elcomew elcome to code jam
//wweellccoommee to code qps jam
//welcome to codejam
long long rst=0;
void _find_next(char* line, int index)
{
	if(index == strlen(STR)){
		rst++;return;
	}
	int len = strlen(line);
	for(int i=0; i<len; i++){
		if(STR[index] == line[i]){
			_find_next(line+i+1, index+1);
		}
	}
}

int resolve(string str)
{
	rst =0;
	strcpy(Line, str.c_str());
	//for (int i=0; i<strlen(STR); i++){
	_find_next(Line, 0);
	//}
	
	return rst%10000;
}


int main()
{
	assert(outfile && infile);
	infile >> testcase;
	string line;
	getline(infile, line);
	for(int i=1; i<=testcase; i++)
	{
		//infile >> line;
		getline(infile, line);

		//trim
		string::size_type prev_pos,pos;
		prev_pos= line.find_first_not_of(STR);
		while(prev_pos != string::npos){
			pos= line.find_first_of(STR, prev_pos);
			if (pos != string::npos){
				line.erase(prev_pos, pos-prev_pos);
			}else{
				line.erase(prev_pos);
			}
			prev_pos= line.find_first_not_of(STR);
		}
		
		int rst= resolve(line);

		char tostr[10];
		sprintf(tostr, "%04d", rst);
		outfile<<"Case #"<<i<<": "<<tostr<<"\n";
	}
	return 0;
}