/*
Author: Cheng Li
Language: C++
IDE: Visual Studio C++ 2008
* 
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool isCharExist(const string& s, char c)
{
	string::size_type index=0; 
	if(s[index]=='(')
	{
		++index;
		while(s[index]!=')')
		{
			if(s[index]==c)
				return true;
			++index;
		}
		return false;
	}
	else if(s[index]==c)
		return true;
	else
		return false;
}

void removeFirst(string& s)
{
	string::size_type index=0;
	if(s[0]=='(')
	{
		s.erase(s.find_first_of('(', 0), s.find_first_of(')', 0)+1);
	}
	else
		s.erase(s.begin());
}

int main(void)
{
	string InFileName="A-large.in";
	string OutFileName="A-large.out";

	ifstream fin;
	ofstream fout;

	//open input file
	fin.open(InFileName.c_str(), ios::in);
	if(fin.fail())
	{
		std::cerr<<"Input file open error!";
	}

	//create output file
	fout.open(OutFileName.c_str(), ios::out);	
	if(fout.fail())
	{
		std::cerr<<"Output file open error!";
	}

	int caseNum=0;
	int caseCount=1;
	int L=0;
	int D=0;

	fin>>L>>D;

	fin>>caseNum;
	cout<<"L is: "<<L<<endl<<"D is: "<<D<<endl<<"N is: "<<caseNum<<endl;
	vector<string> language;

	fin.ignore(1,'\n');

	string strTemp;
	while(D > 0 && getline(fin, strTemp, '\n'))
	{
		language.push_back(strTemp);
		D--;
	}

	while(caseCount<=caseNum)//for case loop
	{
		int matchCount=0;
		string words;
		getline(fin, words, '\n');

		for(vector<string>::iterator iter= language.begin(); iter!= language.end(); ++iter)
		{
			string tempWord=words;
			for(int i=0; i<	L; ++i)
			{
				char c= (*iter)[i];
				//if *iter can be found in words
				// matchCount++;

				if(!isCharExist(tempWord, c))
				{
					break;
				}
				else
				{
					removeFirst(tempWord);
					if(tempWord=="")
						++matchCount;
				}
			}
		}
		if(caseCount==97)

			int a=caseCount;
		fout<<"Case #"<<caseCount++<<": "<<matchCount<<'\n';
	}


	//close input file& output file
	fin.close();
	fout.close();

	return 1;
}