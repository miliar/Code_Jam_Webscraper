#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <vector>

using namespace std;

class InputItem
{
public:
	int case_number;
	int num_snappers;
	int click_count;

	void process(FILE* fp);
};

vector<InputItem*> inputEntries;

bool readInput(const char* filename)
{
	FILE* fp;
	char buff[1024];
	char* line;
	InputItem* pItem;
	unsigned int num_entries = 0;


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

			pItem = new InputItem();
			pItem->case_number = ++iCase;

			sscanf(buff, "%d %d", &pItem->num_snappers, &pItem->click_count);

			inputEntries.push_back(pItem);
		}
	}

	fclose(fp);	
	return (num_entries > 0 && num_entries == inputEntries.size());
}

void InputItem::process(FILE* fp)
{
	//printf("Case #%d: %d, %d\n", case_number, num_snappers, click_count);

	int cbReq = sizeof(char) * (num_snappers + 2);
	char* snps = (char*) malloc(cbReq);
	memset(snps, 0, cbReq);

	snps[0] = 1;

	for(int clk=0; clk<click_count; clk++)
	{
		int power_length = 1;
		while(snps[power_length])
			power_length++;

		if(power_length > num_snappers)
		{
			memset(&snps[1], 0, num_snappers);
			continue;
		}

		//assert(snps[power_length] == 0);
		snps[power_length] = 1;

		while(power_length-- > 1)
		{
			snps[power_length] = !snps[power_length];
		}

/*
		printf("Click %03d: ", clk+1);
		for(int i=1; i<=num_snappers; i++)
			printf("[%d]", snps[i]);
		printf("\n");
*/
	}

	int on_count = 0;
	for(int i=1; i<=num_snappers; i++)
		on_count += snps[i];
	const char* result = (on_count == num_snappers) ? "ON" : "OFF";

	printf("Case #%d: %s\n", case_number, result);
	fprintf(fp, "Case #%d: %s\n", case_number, result);

	free(snps);
}

int main()
{
	if(readInput("v:\\A-large.in"))
	{
		FILE* fp = fopen("v:\\ex1_output2.txt", "wt");
		if(fp != NULL)
		{
			for(int i=0; i<inputEntries.size(); i++)
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
