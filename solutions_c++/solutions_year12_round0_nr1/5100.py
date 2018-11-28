#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <string>
using namespace std;


int main(int argc, char* argv[])
{	char *input="A-small-attempt.IN";
	char *output="Output.txt";
	int abc [128];
	abc[97]=121;	abc[98]=104;	abc[99]=101;	abc[100]=115;	abc[101]=111;	abc[102]=99;	abc[103]=118;
	abc[105]=100;	abc[106]=117;	abc[107]=105;	abc[108]=103;	abc[109]=108;	abc[110]=98;	abc[111]=107;
	abc[112]=114;	abc[113]=122;	abc[114]=116;	abc[115]=110;	abc[116]=119;	abc[117]=106;	abc[118]=112;
	abc[119]=102;	abc[120]=109;	abc[121]=97;
	
	abc[104]=120;	abc[122]=113;	
	int int_ch;
    int i=0, j=0; 
	string line; 
	ifstream fin; 
    ofstream fout;
	vector<string> data; 
	fin.open(input);
	fout.open(output);
	while(getline(fin, line)){
	if (i>=1) data.push_back(line);
	i++;
	}	
	for (i=0; i<data.size(); i++)
		for (j=0; j<data[i].length(); j++)
			{int_ch=(int)(data[i][j]);
			 if (int_ch>=97 && int_ch<=122) data[i][j]=abc[int_ch]; 
			}

	for (i=0; i<data.size(); i++)
		fout<<"Case #"<<i+1<<": "<<data[i]<<"\n";
	
	 fin.close();
	fout.close();
	data.clear();
	return 0;

}
