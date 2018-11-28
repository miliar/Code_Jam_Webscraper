#include <cstring>
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

char Trans[26]={
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r','z',
	't','n','w','j','p','f','m','a','q'
};
int main()
{

	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt0.out");
	int T;
	fin>>T;
	fin.get();
	string from;
	string to;
	for (int i=1;i<=T;i++)
	{
		getline(fin,from,'\n');
		fout<<"Case #"<<i<<": ";
		for (int j=0;j<from.size();j++)
		{
			fout<<Trans[from[j]-'a'];
		}
		if(i<T)
			fout<<endl;
	}
	
	return 0;
}

