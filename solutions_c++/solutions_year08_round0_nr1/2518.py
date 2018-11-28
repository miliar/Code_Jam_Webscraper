#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

const float PI = 3.1415926535897932384626433832795;

char *fgetline(char *buf, int size, FILE *stream)
{
	static char eolbuf[100];
	char *cp;
	int l;
	
	cp = fgets(buf,size,stream);
	l = strlen(buf);
	if (l > 0 && buf[l - 1] != '\n') {
		do {
		fgets(eolbuf,99,stream);
		l = strlen(eolbuf);
		} while (l > 0 && eolbuf[l - 1] != '\n');
	}
	return cp;
}

void splitString(string& sstring, string& separators, string& dstringBefore, string& dstringAfter)
{
	int n = sstring.length();
	int start, stop;

	start = sstring.find_first_not_of(separators);
	while ((start >= 0) && (start < n)) 
	{
		stop = sstring.find_first_of(separators, start);
		if ((stop < 0) || (stop > n)) stop = n;
		dstringBefore	= sstring.substr(0, start - 1);
		dstringAfter	= sstring.substr(start, stop - start);
		start = sstring.find_first_not_of(separators, stop+1);
	}
}

int searchString(vector<string> strVec, string str)
{
	int index = -1, i;
	for (i = 0; (i < (int) strVec.size() && index < 0); i++)
	{
		if (strVec[i] == str)
		{
			index = i;
		}
	}
	
	return index;
}

float sqr(float x)
{
	return x*x;
}

int main()
{
	FILE			*pOut, *pIn;
	int				N, S, Q, Y, i, j, maxIndex, maxValue, len, index;
	char			name[100], *pBuf;
	string			str;
	vector<string>	SearchEngines, Queries;
	vector<int>		sIndexes;

	pIn				= fopen ("A-large.in","r");
	pOut			= fopen ("OUT.txt","w");
	
	fscanf(pIn, "%d",&N);
	for (i = 1; i <= N; i++)
	{
		fscanf(pIn, "%d\r\n", &S);
		
		SearchEngines.clear();
		for (j = 0; j < S; j++)
		{
			pBuf = fgetline(name, 100, pIn);
			fscanf(pIn, "\r\n");
			SearchEngines.push_back(name);
		}
		
		fscanf(pIn, "%d\r\n", &Q);
		
		Queries.clear();
		for (j = 0; j < Q; j++)
		{
			pBuf = fgetline(name, 100, pIn);
			fscanf(pIn, "\r\n");
			Queries.push_back(name);
		}

		Y = 0;
		while(Queries.size())
		{
			sIndexes.clear();
			maxIndex = 0;
			maxValue = -1;
			for (j = 0; j < (int) SearchEngines.size(); j++)
			{
				index					= searchString(Queries, SearchEngines[j]);
				sIndexes.push_back(index);
				
				if (sIndexes[j] > maxValue)
				{
					maxIndex = j;
					maxValue = sIndexes[j];
				}
				
				if (sIndexes[j] < 0)
					maxValue = INT_MAX;
			}
			
			if ((maxValue > 0) && (maxValue != INT_MAX))
			{
				printf("string found %d\n", maxValue);
				Queries.erase(Queries.begin(), Queries.begin() + maxValue);
				Y++;
			}
			else
			{
				Queries.clear();
			}
		}
		
		fprintf(pOut, "Case #%d: %d\n", i, Y);
	}
		
	return 0;
}
