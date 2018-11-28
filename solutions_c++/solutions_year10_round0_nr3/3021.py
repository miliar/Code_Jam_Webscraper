#include <iostream>
using namespace std;

void GetCaseVar(char *buf, unsigned int *runtimenum, unsigned int *seatnum, unsigned int *groupnum)
{
	sscanf(buf, "%d %d %d", runtimenum, seatnum, groupnum);
}

unsigned int* GetGroupArray(char *buf, unsigned int groupnum)
{
	char *groupbegin, *groupend;
	char groupbuf[12];
	unsigned int* grouparray = new unsigned int[groupnum];
	unsigned int i = 0;
	for (groupbegin = groupend = buf; i < groupnum; i++)
	{
		memset(groupbuf, 0, 12);
		while ((groupend[0] != ' ') && (groupend[0] != '\n'))
		{
			groupend++;
		}
		memcpy(groupbuf, groupbegin, (groupend - groupbegin));
		sscanf(groupbuf, "%d", &grouparray[i]);
		groupend++;
		groupbegin = groupend;
	}
	return grouparray;
}

unsigned long GetIncome(unsigned int *grouparray, unsigned int seatnum, unsigned int runtimenum, unsigned int groupnum)
{
	unsigned long income = 0;
	unsigned int nextgroup = 0, count, begingroup;
	for (int i = 0; i < runtimenum; i++)
	{
		count = 0;
		begingroup = nextgroup;
		while ((count + grouparray[nextgroup]) <= seatnum)
		{
			count += grouparray[nextgroup];
			nextgroup++;
			if (nextgroup == groupnum)
			{
				nextgroup = 0;
			}
			if (nextgroup == begingroup) break;
		}
		income += count;
	}
	return income;
}

int main(int argc, char** argv)
{
	if (argc!=2)
	{
		cout<<"No input file"<<endl;
		return -1;
	}

	char* filename = argv[1];
	int CaseNumber = 0;
	char *LineBuffer = NULL;
	FILE *InputFile = NULL;
	const int MAXCHARPERLINE = 8000;

	if (!filename)
	{
		cout<<"Invalid file name"<<endl;
		return -1;
	}
	LineBuffer = new char[MAXCHARPERLINE];
	InputFile = fopen(filename, "r");
	if (!InputFile)
	{
		cout<<"Can not open file"<<endl;
		return -1;
	}

	memset(LineBuffer, 0, MAXCHARPERLINE);
	fgets(LineBuffer, MAXCHARPERLINE, InputFile);
	CaseNumber = atoi(LineBuffer);	

	for (int i = 0; i < CaseNumber; i++)
	{
		unsigned int RunTimeNum, SeatNum, GroupNum;
		memset(LineBuffer, 0, MAXCHARPERLINE);
		fgets(LineBuffer, MAXCHARPERLINE, InputFile);
		GetCaseVar(LineBuffer, &RunTimeNum, &SeatNum, &GroupNum);
		
		memset(LineBuffer, 0, MAXCHARPERLINE);
		fgets(LineBuffer, MAXCHARPERLINE, InputFile);
		unsigned int *GroupArray = GetGroupArray(LineBuffer, GroupNum);

		unsigned long Income = GetIncome(GroupArray, SeatNum, RunTimeNum, GroupNum);
		cout<<"Case #"<<(i + 1)<<": ";
		cout<<Income<<endl;
		delete[] GroupArray;
	}
	return 0;
}