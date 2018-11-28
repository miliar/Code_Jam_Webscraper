#include <iostream>
#include <string>
#include <fstream>
using namespace std;
main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	char map[150]="                                                                 YHESOCVXDUIGLBKRZTNWJPFMAQ      yhesocvxduiglbkrztnwjpfmaq";
	int i,j,k,l;
	fin>>l;
	char in[105];
fin.getline(in,101);
	for(i=1;i<=l;i++)
	{
		fin.getline(in,101);
		fout<<"Case #"<<i<<": ";
		for(j=0;in[j]!='\0';j++)
		{
			fout<<map[in[j]];
		}
		fout<<endl;
	}
	
}