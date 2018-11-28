#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

struct cases
{
public:
	vector<string> eng;
	vector<string> test;
};

int noofcases;

char * getl(FILE *fp)
{
	char *line;
	int i = 0;
        line = new char[100];
	while((line[i++] = fgetc(fp)) != '\n');
	
	line[i - 1] = '\0';
	return line;
}

struct cases * readfile(char *file)
{
	FILE *fp;
	char *line;
	struct cases *p;

        line = new char[100];
	fp = fopen(file, "r");
	line = getl(fp);
	
	noofcases = atoi(line);
	p = new struct cases[noofcases];
	
	for(int i = 0; i < noofcases; i++)
	{
		line = getl(fp);
		int noofeng = atoi(line);
	
		for(int j = 0; j < noofeng; j++)
		{
			line = getl(fp);
			p[i].eng.push_back(line);
		}	
		
		line = getl(fp);
		int noofcase = atoi(line);
	
		for(int j = 0; j < noofcase; j++)
		{
			line = getl(fp);
			p[i].test.push_back(line);
		}
	}
	return p;
}

int lru(int *count, int size, int *switchs)
{
	int c = 0;
	for(int i = 0; i < size; i++)
		if(count[i] == 0) return 1;
	(*switchs)++;
	return 0;
}

void algo(struct cases *p, char *file)
{
	FILE *fp;
	fp = fopen(file,"wt");
	for(int i = 0; i < noofcases; i++)
	{
		map <string, int> engines;	
		int count[p[i].eng.size()];
		
		for(int j = 0; j < p[i].eng.size(); count[j] = 0, j++)
			engines[p[i].eng[j]] = j;
		
		int switchs = 0, n = 0;
		while(n < p[i].test.size())
		{
			if(lru(count, p[i].eng.size(), &switchs)) {
				count[engines[p[i].test[n]]]++;	
				n++;
			}
			else {
				for(int k = 0; k < p[i].eng.size(); count[k] = 0, k++);
				count[engines[p[i].test[n - 1]]]++;	
			}
		}
		lru(count, p[i].eng.size(), &switchs);
		fprintf(fp,"Case #%d: %d\n",i+1,switchs);
	}	
	fclose(fp);
}

int main(int argc, char *argv[])
{
	struct cases *p;
	p = readfile(argv[1]);
	algo(p, argv[2]);	
}
