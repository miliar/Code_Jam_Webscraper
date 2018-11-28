#include <iostream>
#include <string>
#include <fstream>
#include <tchar.h>

using namespace std;

int main(int argc, _TCHAR* argv[])
{

	string buffer;

	ifstream ifile;
	ofstream ofile;

	ifile.open("C-small-attempt4.in", ios::binary);
	ofile.open("C-small-attempt4.out", ios::binary);

	if (ifile.fail() || ofile.fail())
	{
		cout<<" 文件读取失败！" <<endl;
		return 1;
	}

	int caseTime = 0;

	if (getline(ifile,buffer))
	{
		caseTime = atoi(buffer.data());
	}

	if (caseTime == 0)
	{
		cout<<" 没有实例"<<endl;
		ifile.close();
		return 0 ;
	}

	int runTimes[50];
	int gross[50];
	int groupAmount[50];
	int groups[50][10];
	int index = 0;
	while(!ifile.eof() && (index < caseTime))
	{
		if (getline(ifile,buffer))
		{
			int pos = buffer.find(" ");
			runTimes[index] = atoi(buffer.substr(0,pos).data());
			int spos = buffer.find(" ",pos+1);
			gross[index] = atoi(buffer.substr(pos+1,spos).data());

			groupAmount[index] = atoi(buffer.substr(spos+1,buffer.size()).data());

			if (getline(ifile,buffer))
			{
				pos = 0;
				for (int i = 0; i < groupAmount[index];i++ )
				{
					spos = buffer.find(" ",pos+1);
					if (spos == -1)
					{
						groups[index][i] = atoi(buffer.substr(pos,buffer.size()).data());
						break;
					} 
					groups[index][i] = atoi(buffer.substr(pos,spos).data());
					pos = spos + 1;
				}
			}
			index++;
		}
	}

	int revenue[50];

	for (int caseIndex = 0; caseIndex < caseTime; caseIndex++)
	{
		revenue[caseIndex] = 0;
		int startIndex = 0;
		for (int runIndex = 0; runIndex < runTimes[caseIndex]; runIndex++)
		{
			int endIndex = (startIndex + 1) % groupAmount[caseIndex];

			int eachIncome = groups[caseIndex][startIndex];

			while(endIndex!=startIndex && eachIncome + groups[caseIndex][endIndex] <= gross[caseIndex])
			{
				eachIncome += groups[caseIndex][endIndex];
				endIndex = (endIndex+1) % groupAmount[caseIndex];
			}

			revenue[caseIndex] += eachIncome;

			startIndex = endIndex;

		}

	}




	for (index = 0; index < caseTime; index++)
	{
		ofile<<"Case #"<<(index+1)<<": "<<revenue[index]<<"\n";
	}

	ifile.close();
	ofile.close();

	return 0;
}


