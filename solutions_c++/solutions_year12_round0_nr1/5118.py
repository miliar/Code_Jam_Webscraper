#include <iostream>
#include <fstream>
#include <string>
using namespace std;
char map[] =
	{'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o',
	'm', 'x', 's', 'e', 'v', 'z' ,'p' ,'d', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
int indexOf(char c)
{
	for(int i = 0 ; i < 26; i++)
	{
		if(map[i] == c)
			return i;
	}
}
int main()
{
	ifstream fin("A-Small-attempt0.in");
	ofstream fout("A-Small-attempt0.out");

	int n;
	fin >> n;
	string s;
	getline(fin, s);
	for(int i = 0; i < n; i++)
	{
		getline(fin, s);
		fout << "Case #" << i+1 << ": ";
		for(int j = 0; j<s.length(); j++)
		{
			if (s[j] != ' ')
				fout << (char)(indexOf(s[j]) + 'a'); //map[ s[j] - 'a' ];
			else fout << ' ';
		}
		fout << endl;
	}
	return 0;
}