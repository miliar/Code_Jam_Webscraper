#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <fstream>
using namespace std;

void find1()
{
	string AL = "yhesocvxduiglbkrztnwjpfmaq";

	ifstream fin("D:\\jam.in");
	ofstream fout("D:\\jam.out");

	int T;
	
	string s;
	getline(fin, s);
	T = atoi(s.c_str());

	int ncase = 1;

	while(T-- > 0)
	{
		
		getline(fin, s);

		string r = "";
		for(int i=0; i<s.length(); ++i)
		{
			if(s[i] == ' ')
				r += s[i];
			else
				r += AL[s[i]-'a'];
		}

		fout << "Case #"<< ncase++ << ": " << r << endl;
	}


}

int main()
{
find1();
}