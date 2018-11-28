// SavingTheUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include <vector>
#include <string>


void clearEngines(std::vector<std::string>& e, std::vector<bool>& s)
{
	e.clear();
	s.clear();
}

int findEngine(std::vector<std::string> e, const char* name)
{
	for(unsigned int i=0; i < e.size(); i++)
		if(!strcmp(e[i].c_str(), name))
			return i;

	return -1;
}

bool checkStatus(std::vector<bool> s)
{
	for(unsigned int i=0; i < s.size(); i++)
		if(!s[i])
			return false;

	return true;
}

void clearStatus(std::vector<bool>& s)
{
	for(unsigned int i=0; i < s.size(); i++)
		s[i] = false;
}


int main(int argc, _TCHAR* argv[])
{
FILE* fpIn;
FILE* fpOut;
char line[1024];
int N, S, Q;
std::vector<std::string> engines;
std::vector<bool> status;
int i, j;
int nSwitches;

	fpIn = fopen(argv[1], "rb");
	fpOut = fopen(argv[2], "wb");

	N = atoi(fgets(line, 1024, fpIn));

	for(i=0; i < N; i++)
	{
		S = atoi(fgets(line, 1024, fpIn));

		clearEngines(engines, status);
		nSwitches = 0;

		for(j = 0; j < S; j++)
		{
			fgets(line, 1024, fpIn);
			engines.push_back(line);
			status.push_back(false);
		}

		Q = atoi(fgets(line, 1024, fpIn));
		for(j = 0; j < Q; j++)
		{
			fgets(line, 1024, fpIn);

			// Acrescenta no  número de switches específico
			int pos = findEngine(engines, line);
			status[pos] = true;

			if(checkStatus(status))
			{
				nSwitches++;
				clearStatus(status);
			}
			status[pos] = true;
		}

		printf("%d=> %d\r\n", i+1, nSwitches);
		fprintf(fpOut, "Case #%d: %d\n", i+1, nSwitches);
	}


	fclose(fpIn);
	fclose(fpOut);

	return 0;
}

