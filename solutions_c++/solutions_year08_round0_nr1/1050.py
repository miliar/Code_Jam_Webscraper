// Saving the earth.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include < iostream>
#include <string>
#include <vector>
using namespace std;


#include <math.h>



inline void removeSpace(ifstream& in)
{
	char temp[2];
	in.getline(temp, 2);
}



void  getHead(char* head, int index)
{
	size_t start = 0;

	char temp[10];
	_itoa_s(index, temp, 10);

	start = 6;
	head[start] = '\0';
	strcat(&(head[start]), temp);
	start += strlen(temp);
	strcat(&(head[start]), ": ");
}





int find(int start, int end, const string* enginNames, const string& enginName )
{
	for(int ii = start; ii <= end; ii++)
		if(strcmp(enginNames[ii].c_str(), enginName.c_str()) == 0)
			return ii;
	
	return -1;

}

int _tmain(int argc, _TCHAR* argv[])
{
	size_t N = 0;
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	char out_head[100] = "Case #";
	char out_data[100];
	in>>N;
	removeSpace(in);

	string enginName[100];
	string query[1000];
	for (size_t  caseIndex = 0; caseIndex < N; caseIndex++)  //start the test
	{
		size_t enginNumbers = 0;
		size_t queryNumbers = 0;
		in>> enginNumbers;
		removeSpace(in);
		for(size_t jj = 0; jj < enginNumbers; jj++) // read engins' names
		{		
			getline(in, enginName[jj]);
		}

		in>>queryNumbers;
		removeSpace(in);
		for(size_t jj = 0; jj < queryNumbers; jj++) // read query
		{
			getline(in, query[jj]);
		}
		

		size_t queryIndex = 0;
		vector<int> candidata;
		for(size_t ii =0; ii < enginNumbers; ii++)
			candidata.push_back(ii);

		int switcher = 0;
		while(queryIndex < queryNumbers)  //start to search
		{
			int index = find(0, enginNumbers-1,enginName, query[queryIndex]);
			if(index != -1)
			{
				if(candidata.size() == 1 && candidata[0] == index) // we have to do a switch
				{
					switcher ++;
					candidata.clear();
					for(int ii =0; ii < enginNumbers; ii++)
						candidata.push_back(ii);

				}
				else // do not have to
				{
					queryIndex++;
					// remove, the last one is the bestOne
					for(vector<int>::iterator f = candidata.begin(); f != candidata.end(); f++)
					{
						if(*f == index)
						{
							candidata.erase(f);
							break;
						}
					}
				}
			}
		}  // while

		getHead(out_head, caseIndex+1);
		itoa(switcher, out_data, 10);
		out.write(out_head, strlen(out_head));
		out.write(out_data, strlen(out_data));
		if(caseIndex != N-1)
			out.write("\n",1);

	}



	out.close();
	return 0;
}

