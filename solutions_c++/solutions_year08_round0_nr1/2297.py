// #include "iostream.h"
// #include "conio.h"

// This program reads input file from C:\\A-large-attempt0.in and generates a output file C:\\output.txt
#include "stdio.h"
#include <vector>
#include <string>

using namespace std;

//max chars in a line are 100 and a new line/return feed
#define max_chars 102

bool FindStringInArray( vector<string> &myEngines, string str);
int CalculateSwitches(vector<string> &vEngines, vector<string> &vQueries);

void main()
{
	FILE* fp = fopen("C:\\A-large-attempt0.in", "r");
	if(fp == NULL)
		printf("Unable to read file from C:\\A-large-attempt0.in");

	FILE *fpOut = fopen("C:\\output.txt", "w");
	if(fpOut == NULL)
		printf("Unable to create a output file at C:\\output.txt");

	int result = 0;
	vector<string> engines;
	vector<string> queries;
	int total_tests;
	int total_engines;
	int total_queries;

	fscanf(fp, "%d", &total_tests);

	int case_num = 0;
	while(case_num < total_tests)
	{
		//get no. of engines
		fscanf(fp, "%d", &total_engines);

		char c;
		fscanf(fp, "%c", &c);//read the new line character otherwise fgets will read newline character first
		string str;
		char arr[max_chars];
		memset(arr, 0, sizeof(arr));

		while(total_engines>0)
		{
			fgets(arr, sizeof(arr), fp);
			//str.at
			str = arr;
			int i = str.size();
			if(str[i-1] == '\n')
				str.erase(i-1);
			engines.push_back(str);
			total_engines --;
		}

		fscanf(fp, "%d", &total_queries);
		fscanf(fp, "%c", &c); //read the new line character otherwise fgets will read newline character first

		while(total_queries > 0)
		{
			fgets(arr, max_chars, fp);
			str = arr;
			int i = str.size();
			if(str[i-1] == '\n')
				str.erase(i-1);
			queries.push_back(str);
			total_queries --;
		}

		result = CalculateSwitches(engines, queries);
		printf("Case #%d: %d\n", case_num+1, result);
		fprintf(fpOut, "Case #%d: %d\n", case_num+1, result);	
		case_num++;
		result = 0;
		engines.clear();
		queries.clear();
	}

	fclose(fp);

}

int CalculateSwitches(vector<string> &vEngines, vector<string> &vQueries)
{
	int queryNum;
	bool b;
	int no_of_switches = 0;
	int totalQueries = vQueries.size();

	vector<string> myEngines = vEngines;

	for(queryNum=0; queryNum < totalQueries; queryNum++)
	{
		b = FindStringInArray(myEngines, vQueries.at(queryNum));

		if(b)//now we need to make a switch. we have avoided as long as possible.
		{
			no_of_switches++;
			queryNum--; //start from previous query
			myEngines = vEngines; //restore myEngines
		}
	}
	return no_of_switches;

}
bool FindStringInArray( vector<string> &myEngines, string str)
{
	std::vector<string>::iterator i;

	for(i = myEngines.begin(); i != myEngines.end(); ++i)
	{
		if(*i == str)
		{
			if(myEngines.size()==1)
				return 1;
			myEngines.erase(i);
			break;
		}
	}
	return 0;
}
/*
Algorithm used is - store the search engine names and queries in a vector.
Take next query. If this query is found in engine vector, then remove it from the engine vector. IF this is the last qyery to be removed from engine vector, then now we need to make a switch
otherwise repeat the above line.
*/
