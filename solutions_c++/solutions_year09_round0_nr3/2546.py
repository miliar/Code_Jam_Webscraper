#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include<conio.h>

using namespace std;
string codejam = "welcome to code jam";

int Recurse (string &s, int cj, int pos)
{
	if (cj == codejam.length())
		return 1;

	int ans = 0;
	while((pos = s.find(codejam[cj],pos)) != -1)
	{
		pos ++;
		if(ans>9999)
		            return 1;
        else
		            ans = ans + Recurse (s, cj + 1, pos);
	}
	
	return ans % 1000;
}

int main()
{
	ifstream fin ("a.in");
	ofstream fout ("a.out");
	int N;
	string inp;
	fin >> N;
	getline (fin,inp);
	for (int i = 0; i < N; i++)
	{
		getline (fin, inp);
		int ans = Recurse (inp, 0, 0);
		char buff[10];
		sprintf (buff, "%04d", ans);
		fout << "Case #" << i+1 << ": " << buff << endl;
	}
	return 0;
}
