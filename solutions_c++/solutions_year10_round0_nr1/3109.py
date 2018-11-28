#include <iostream>
using namespace std;

void GetCase(char* buf, int *snappernum, long *switchtime)
{
	sscanf(buf, "%d %ld", snappernum, switchtime);
}

long GetMinSwitchOnTime(int snappernum)
{
	if (snappernum == 1 || snappernum == 0)
	{
		return snappernum;
	}
	return GetMinSwitchOnTime(snappernum - 1) * 2 + 1;
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
	const int MAXCHARPERLINE = 20;
	
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
		int SnapperNumber;
		long SwitchTime;
		fgets(LineBuffer, MAXCHARPERLINE, InputFile);
		GetCase(LineBuffer, &SnapperNumber, &SwitchTime);
		long MinSwitchOnTime = GetMinSwitchOnTime(SnapperNumber);
		bool fOn = false;
		if (SwitchTime == MinSwitchOnTime)
		{
			fOn = true;
		}
		else if ((SwitchTime%(MinSwitchOnTime + 1)) == MinSwitchOnTime)
		{
			fOn = true;
		}
		cout<<"Case #"<<(i + 1)<<": ";
		if (fOn)
		{
			cout<<"ON"<<endl;
		}
		else
		{
			cout<<"OFF"<<endl;
		}
	}
	return 0;
}