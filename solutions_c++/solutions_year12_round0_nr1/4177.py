#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin ("in.txt");

	ofstream fout ("out.txt");
	string F = "yhesocvxduiglbkrztnwjpfmaq";
	string L1, S;
	L1 = S;
	int n;
	fin>>n;
	getline(fin, S);
	for (int i = 1; i <= n; i ++)
	{
		getline(fin, S);
		for (int i = 0; i < S.size() ; i ++)
		{
			if (S[i] != ' ')
			{
				S[i] = F[S[i]-'a'];
			}
		}
		fout<<"Case #"<<i<<": "<<S<<endl;
	}
	return 0;
}