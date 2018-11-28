// p6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>


using namespace std;

long getnum(string source, string find)
{
	if (find.empty()) return 0;
	int retVal = 0;
	char firstChar = find[0];
	int pos = 0;
	if (find.length() == 1) {
	while ((pos = source.find_first_of(firstChar,pos)) != string::npos)
	{
		++retVal;
		++pos;
	}
	return retVal;
	}

	
	while ((pos = source.find_first_of(firstChar,pos)) != string::npos)
	{

		retVal = (retVal + getnum(source.substr(pos+1),find.substr(1)));
		//printf("%d ",pos);
		++pos;
	}
	return (retVal);
}


int main(int argc, char* argv[])
{
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	int numCases;
	char temp[2000];
	fin >> numCases;
	vector <string> cases;
	fin.getline(temp,2000);
	//cases.push_back(temp);
	for (int i=0;i<numCases;++i)
	{
		fin.getline(temp,2000);
		cases.push_back(temp);
		char temp[250];
		sprintf(temp,"%4d",10000+getnum(cases[i],"welcome to code jam"));
		fprintf(f2,"Case #%d: %s\n",i+1,temp+1);
	}
	return 0;
}



