#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <fstream>
using namespace std;

const int maxn = 26;
string stan = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	char myfile[maxn], infile[maxn], outfile[maxn], tmp[256];
	int i, n, siz, cas = 1;
	ifstream in;
	ofstream out;

	scanf("%s", myfile);
	strcpy(infile, myfile);
	strcpy(outfile, myfile);
	strcat(infile, ".in");
	strcat(outfile, ".out");

	in.open(infile);
	out.open(outfile);

	in >> n;
	in.getline(tmp, 256);
	while (n--)
	{
		in.getline(tmp, 256);
		siz = strlen(tmp);
		for (i = 0; i < siz; i++)
		{
			if (tmp[i] != ' ')
				tmp[i] = stan[tmp[i] - 'a'];
		}
		out << "Case #" << cas << ": " << tmp << endl;
		cas++;
	}
	
	return 0;
}