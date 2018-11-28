#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int noofcases;

struct cases
{
public:
	int turn;
	int A_no;
	int B_no;
	vector<int> A_Dep;
	vector<int> A_Arr;
	vector<int> B_Dep;
	vector<int> B_Arr;
};

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
	char *pch;

        line = new char[100];
	fp = fopen(file, "r");
	line = getl(fp);
	
	noofcases = atoi(line);
	p = new struct cases[noofcases];
	
	for(int i = 0; i < noofcases; i++)
	{
		line = getl(fp);
		p[i].turn = atoi(line);

		line = getl(fp);
		pch = strtok(line," ");
		p[i].A_no = atoi(pch);	
		pch = strtok(NULL," ");	
		p[i].B_no = atoi(pch);
		for(int j = 0; j < p[i].A_no; j++)
		{
			line = getl(fp);
			pch = strtok (line," :");
			p[i].A_Dep.push_back(atoi(pch) * 60);
	          	pch = strtok (NULL," :");
	          	p[i].A_Dep[j] += atoi(pch);
			pch = strtok (NULL," :");
			p[i].A_Arr.push_back(atoi(pch) * 60); 
	          	pch = strtok (NULL," :");
			p[i].A_Arr[j] += atoi(pch);	          	
		}	
		
		for(int j = 0; j < p[i].B_no; j++)
		{
			line = getl(fp);
			pch = strtok (line," :");
			p[i].B_Dep.push_back(atoi(pch) * 60);
	          	pch = strtok (NULL," :");
			p[i].B_Dep[j] += atoi(pch);
			pch = strtok (NULL," :");
			p[i].B_Arr.push_back(atoi(pch) * 60);
	          	pch = strtok (NULL," :");
			p[i].B_Arr[j] += atoi(pch);	          	
		}	
	}
	return p;
}

void algo(struct cases *p, char *file)
{
FILE *fp;
fp = fopen(file, "wt");
	for(int i = 0; i < noofcases; i++)
	{
		int a[p[i].A_no];
		int b[p[i].B_no];
		for(int j = 0; j < p[i].A_no; j++) a[j] = 0;
		for(int j = 0; j < p[i].B_no; j++) b[j] = 0;		
		for(int j = 0; j < p[i].A_no; j++)
		{
			int min = 24 * 60 + 100;
			int ind = -1;
			for(int k = 0; k < p[i].B_no; k++)
			{
				if(b[k] != 1 && (p[i].A_Arr[j] + p[i].turn) <= p[i].B_Dep[k] && p[i].B_Dep[k] < min)
				{
					ind = k;
					min = p[i].B_Dep[k];
				}
			}
			if(ind != -1) b[ind] = 1;
		}
		
		for(int j = 0; j < p[i].B_no; j++)
		{
			int min = 24 * 60 + 100;
			int ind = -1;
			for(int k = 0; k < p[i].A_no; k++)
			{
				if(a[k] != 1 && (p[i].B_Arr[j] + p[i].turn) <= p[i].A_Dep[k] && p[i].A_Dep[k] < min)
				{
					ind = k;
					min = p[i].A_Dep[k];
				}
			}
			if(ind != -1) a[ind] = 1;
		}
		
		int count = 0;
		for(int j = 0; j < p[i].A_no; j++)
			if(a[j] == 0) count++;
		
		fprintf(fp,"Case #%d: %d", i + 1, count);
		count = 0;
		for(int j = 0; j < p[i].B_no; j++)
			if(b[j] == 0) count++;
		fprintf(fp," %d\n", count);
	}
fclose(fp);
}

int main(int argc, char *argv[])
{
	struct cases *p;
	p = readfile(argv[1]);
	algo(p, argv[2]);
}
