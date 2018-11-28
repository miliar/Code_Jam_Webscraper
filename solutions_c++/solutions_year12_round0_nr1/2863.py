//============================================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
//#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>


using namespace std;

char org[] = "abcdefghijklmnopqrstuvwxyz";
char trans[] = "!!!!!!!!!!!!!!!!!!!!!!!!!!";
char known[] = "abcdefghijklmnopqrstuvwxyz";

char str[4][100] = {
		"y qee",
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
char ans[4][100] = {
		"a zoo",
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
};

int main(int argc, char** argv)
{

	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	//construct dictionary
	int i,j;
	for(j=0; j<4; j++)
	{
		for(i=0; i<strlen(str[j]); i++)
		{
			if(str[j][i] == ' ')
				continue;

			if(trans[str[j][i]-'a'] != '!' && (trans[str[j][i]-'a'] != ans[j][i]))
			{
				cout << "Something Wrong!!" << endl;
				cout << "trans: " << trans[str[j][i]-'a'] << ", ans: " << ans[j][i] << endl;
			}

			trans[str[j][i]-'a'] = ans[j][i];
			known[ans[j][i]-'a'] = '-';
		}
	}

	cout << org << endl;
	cout << trans << endl;
	cout << known << endl;

	//manually assign from previous result
	trans['z'-'a'] = 'q';
	cout << trans << endl;

//	return 0;

	char result[120];
	char origin[120];

	int nCase;

	string strOrg;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;
	string tempStr;
	getline(infile, tempStr);	//flush first \n

	for(int iCase=0; iCase<nCase; iCase++)
	{
		outfile << "Case #" << iCase+1 << ": ";

		memset(result, 0, 120);
		int pos = 0;

		char c = 0;
		int inter = 0;

		getline(infile, strOrg);

		strcpy(origin, strOrg.c_str());

		for(i=0; i<strlen(origin); i++)
		{
			c = origin[i];

			if(c == ' ')
				result[pos++] = ' ';
			else
				result[pos++] = trans[c-'a'];
		}

		outfile << result << endl;
	}

	outfile << endl;

	return 0;

}
