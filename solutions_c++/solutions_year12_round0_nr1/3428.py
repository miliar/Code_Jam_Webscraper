// Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "string"

using namespace std;

char original[]	= "abcdefghijklmnopqrstuvwxyz";
char subst2[]	= "yhesocvxduiglbkrztnwjpfmaq";
								   
char subst[]	= "ynficwlbkuomxsevzpdrjgthaq";



int _tmain(int argc, _TCHAR* argv[])
{
	if(argc < 2)
		return 1;
	int num;
	ifstream ifs(argv[1]);
	ifs >> num;

	ofstream ofs("output.txt");
	char buf[201];
	ifs.getline(buf, 200);

	for(int i = 1; i <= 30; i++)
	{
		char buf[201];		
		ifs.getline(buf, 101);
		for(unsigned j = 0; j < strlen(buf); j++)
		{
			if(buf[j] != ' ')
			{
				buf[j] = subst2[buf[j] - 'a'];
			}
		}

		ofs << "Case #" << i << ": " << buf ;
		if(i != num)
			ofs << endl;
	}

	return 0;
}

