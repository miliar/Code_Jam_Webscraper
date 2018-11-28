#include <iostream>
#include <string>
#include <fstream>
using namespace std;
string Structure = "yhesocvxduiglbkrztnwjpfmaq";
void googlerese(string &stringRef)
{
	for(string::iterator iter = stringRef.begin(); iter != stringRef.end(); ++iter)
	{
		char ch = *iter;
		if(ch != ' ')
		*iter = Structure[ch - 97];
	}
}
int main()
{
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	unsigned int testcases, current_test = 1;
	fin>>testcases;
	string inputString;
	getline(fin,inputString);
	while(testcases-- > 0)
	{
		//cin.clear();cin.sync();
		fin.clear();
		getline(fin,inputString);
		googlerese(inputString);
		fout<<"Case #"<<current_test++<<": "<<inputString<<endl;
	}
	fout.close();
	return 0;
}
