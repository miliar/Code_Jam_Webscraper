#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class InputItem
{
public:
	int case_number;
	vector<string> exists;
	vector<string> creates;

	void process(FILE* fp);
};

vector<InputItem*> inputEntries;

char *TrimString(char *psz)
{
	char *s, *e;

	if(psz == NULL) return NULL;

	s = psz;
	while(*s == ' ' || *s == '\t') s++;

	for(e=s; *e != '\0'; e++);

	do *e-- = '\0'; while(*e == ' ' || *e == '\t' || *e == '\r' || *e == '\n');

	return (s>e) ? NULL : s;
}

bool readInput(const char* filename)
{
	FILE* fp;
	char buff[1024];
	char* line;
	InputItem* pItem;
	unsigned int num_entries = 0;

	int nExists;
	int nCreates;

	fp = fopen(filename, "rt");
	if(fp == NULL)
	{
		cout << "File open failed: " << filename << endl;
		return false;
	}

	line = fgets(buff, 1024, fp);
	if(line != NULL)
	{
		int iCase = 0;
		num_entries = atoi(line);
		for(unsigned int k=0; k<num_entries; k++)
		{
			line = fgets(buff, 1024, fp);
			if(line == NULL)
				break;

			sscanf(buff, "%d %d", &nExists, &nCreates);

			pItem = new InputItem();
			pItem->case_number = ++iCase;

			while(nExists-- > 0)
			{
				line = TrimString(fgets(buff, 1024, fp));
				if(line == NULL || line[0] != '/')
					goto _parseError;

				pItem->exists.push_back(&line[1]);
			}

			while(nCreates-- > 0)
			{
				line = TrimString(fgets(buff, 1024, fp));
				if(line == NULL || line[0] != '/')
					goto _parseError;

				pItem->creates.push_back(&line[1]);
			}
			
			inputEntries.push_back(pItem);
		}
	}

_parseError:

	fclose(fp);	
	return (num_entries > 0 && num_entries == inputEntries.size());
}

class Directory
{
	map<string, Directory*> children;

public:
	~Directory()
	{
		map<string, Directory*>::iterator itr = children.begin();
		for(; itr != children.end(); ++itr)
			delete itr->second;
	}

	void mkdir(char** dirs, int index, int* pCreateCount)
	{
		const char* dir = dirs[index];
		Directory* p;

		map<string, Directory*>::iterator itr = children.find(dir);
		if(itr == children.end())
		{
			*pCreateCount = *pCreateCount +1;
			p = new Directory();
			children[dir] = p;
		}
		else
		{
			p = itr->second;
		}

		if(dirs[index+1] != NULL)
			p->mkdir(dirs, index+1, pCreateCount);
	}
};

void InputItem::process(FILE* fp)
{
	//printf("Case #%d: %d, %d\n", case_number, num_snappers, click_count);

	char buff[1024];
	char *tok;
	char *tokens[200];
	int nTokens;
	Directory root;

	// pre-create
	vector<string>::iterator itr = exists.begin();
	for(; itr != exists.end(); ++itr)
	{
		strcpy(buff, itr->c_str());

		nTokens = 0;
		tok = strtok(buff, "/");
		while(tok)
		{
			tokens[nTokens++] = tok;
			tok = strtok(NULL, "/");
		}

		tokens[nTokens] = NULL;
		int ignore;
		root.mkdir(tokens, 0, &ignore);
	}

	int nCreateCount = 0;

	itr = creates.begin();
	for(; itr != creates.end(); ++itr)
	{
		strcpy(buff, itr->c_str());

		nTokens = 0;
		tok = strtok(buff, "/");
		while(tok)
		{
			tokens[nTokens++] = tok;
			tok = strtok(NULL, "/");
		}

		tokens[nTokens] = NULL;
		root.mkdir(tokens, 0, &nCreateCount);
	}

	printf("Case #%d: %d\n", case_number, nCreateCount);
	fprintf(fp, "Case #%d: %d\n", case_number, nCreateCount);
}

int main()
{
	if(readInput("v:\\A-large.in"))
	{
		FILE* fp = fopen("v:\\ex1_output2.txt", "wt");
		if(fp != NULL)
		{
			for(size_t i=0; i<inputEntries.size(); i++)
			{
				inputEntries.at(i)->process(fp);
			}

			fclose(fp);
			cout << "Done" << endl;
		}
		else
		{
			cout << "Output file open failed." << endl;
		}
	}
	else
	{
		cout << "Input parsing failed." << endl;
	}

	// TODO: delete items

	return 0;
}
