#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <map>
#include <string>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("A-Small.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("A-Small.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	char GSet[128] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char SSet[128] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	map<char,char> GtoSmap;
	for (int i=0; i<128; i++)
	{
		GtoSmap[GSet[i]] = SSet[i];
	}
	GtoSmap['q'] = 'z';
	GtoSmap['z'] = 'q';
	//reading procedure
	string s;
	getline(inFile,s);
	case_Count = atoi(s.c_str());
	for (int i=0; i<case_Count; i++)
	{
		//输入
		getline(inFile,s);
		//操作区
		for (unsigned int j=0; j<s.length(); j++)
		{
			s[j] = GtoSmap[s[j]];
		}
		//输出
		outFile << "Case #" << i+1 << ": " << s << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}