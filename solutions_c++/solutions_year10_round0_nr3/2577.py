#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <assert.h>

#include <iostream>
#include <string>
#include <queue>

using namespace std;

class InputItem
{
public:
	int case_number;
	int R_times;
	int K_holds_at_once;
	int N_groups;
	deque<int> groups;

	void process(FILE* fp);
};

vector<InputItem*> inputEntries;

bool readInput(const char* filename)
{
	static const char* delim = " \t\n\r";

	FILE* fp;
	char* buff;
	char* line;
	char *tok;
	InputItem* pItem;
	unsigned int num_entries = 0;


	int buff_size = 10000000 * 10 + 1024;
	buff = (char*) malloc(buff_size);
	if(buff == NULL)
	{
		printf("Out of memory: %d", buff_size);
		return false;
	}

	fp = fopen(filename, "rt");
	if(fp == NULL)
	{
		cout << "File open failed: " << filename << endl;
		free(buff);
		return false;
	}

	int iCase = 0;
	line = fgets(buff, buff_size, fp);
	if(line != NULL)
	{
		num_entries = atoi(line);
		for(unsigned int k=0; k<num_entries; k++)
		{
			line = fgets(buff, buff_size, fp);
			if(line == NULL)
				break;

			pItem = new InputItem();
			pItem->case_number = ++iCase;

			// first line (R, k, N)
			sscanf(line, "%d %d %d", &pItem->R_times, &pItem->K_holds_at_once, &pItem->N_groups);
			if(pItem->R_times == 0 || pItem->K_holds_at_once == 0 || pItem->N_groups == 0)
			{
				delete pItem;
				break;
			}
			
			line = fgets(buff, buff_size, fp);
			if(line == NULL)
				break;

			tok = strtok(line, delim);
			while(tok)
			{
				int group_size = atoi(tok);
				if(group_size <= 0)
					break;

				pItem->groups.push_back(group_size);
				tok = strtok(NULL, delim);
			}

			if(pItem->groups.size() != pItem->N_groups)
				break;

			inputEntries.push_back(pItem);

#if 0
			printf("R=%d, k=%d, N=%d\n", pItem->R_times, pItem->K_holds_at_once, pItem->N_groups);
			for(int i=0; i<pItem->N_groups; i++)
				printf("%d ", pItem->groups.at(i));
			puts("\n--------------------------------------------");		
#endif
		}
	}

	free(buff);
	fclose(fp);
	return (num_entries > 0 && num_entries == inputEntries.size());
}

void InputItem::process(FILE* fp)
{
	__int64 money = 0;
	deque<int> coaster;
	int seats = K_holds_at_once;

	for(int r=0; r<R_times; r++)
	{
		seats = K_holds_at_once;

		while(!groups.empty())
		{
			int cur_group = groups.front();
			if(cur_group <= seats)
			{
				seats -= cur_group;
				money += cur_group;
				groups.pop_front();
				coaster.push_back(cur_group);
			}
			else
			{
				break;
			}
		}

		while(!coaster.empty())
		{
			groups.push_back(coaster.front());
			coaster.pop_front();
		}
	}

	fprintf(fp, "Case #%d: %d\n", case_number, money);
}

int main()
{
	if(readInput("v:\\ex3_input.txt"))
	{
		FILE* fp = fopen("v:\\ex3_output.txt", "wt");
		if(fp != NULL)
		{
			vector<InputItem*>::iterator itr = inputEntries.begin();
			for(; itr != inputEntries.end(); ++itr)
			{
				(*itr)->process(fp);
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
