#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

struct Combine
{
	char com[3];
};

struct Opposition
{
	char Op[2];
};

bool checkCom(std::vector<char> & ansString,std::vector<Combine> & ComList)
{
	int tempNum = ansString.size();
	if(tempNum < 2)
		return false;
	char B = ansString[tempNum - 1];
	char A = ansString[tempNum - 2];
	for(int i = 0; i < ComList.size(); i++)
	{
		if( (A == ComList[i].com[0] && B == ComList[i].com[1]) 
			||
			(B == ComList[i].com[0] && A == ComList[i].com[1]))
		{
			ansString.pop_back();
			ansString.pop_back();
			ansString.push_back(ComList[i].com[2]);
			return true;
		}
	}
	return false;
}

void checkOppo(std::vector<char> & ansString,std::vector<Opposition> & OpList)
{
	int tempNum = ansString.size();
	if(tempNum < 2)
		return;
	char A = ansString[tempNum - 1];
	char B;
	for(int i = 0; i < tempNum - 1; i++)
	{
		B = ansString[i];
		for(int j = 0; j < OpList.size(); j++)
		{
			if((A == OpList[j].Op[0] && B == OpList[j].Op[1])
			||
			(B == OpList[j].Op[0] && A == OpList[j].Op[1]))
			{
				ansString.clear();
				return;
			}
		}
	}
	return;
}

void solve(std::vector<char> & stringVec,std::vector<Combine> & ComList, std::vector<Opposition> & OpList,std::vector<char> & ansString)
{
	ansString.clear();
	for(int i = 0; i < stringVec.size(); i++)
	{
		ansString.push_back(stringVec[i]);
		while(checkCom(ansString,ComList))
		{

		}
		checkOppo(ansString,OpList);
	}
	return;
}

int main()
{
	int T;
	int C;
	int D;
	int N;
	ifstream fin("B-large.in");
	fin>>T;
	ofstream fout("B-large.out");

	Combine tempCom;
	std::vector<Combine> ComList;

	Opposition tempOpposition;
	std::vector<Opposition> OpList;

	string tempString;
	std::vector<char> stringVec;

	std::vector<char> ansString;

	for(int i = 0; i < T; i++)
	{
		fin>>C;
		ComList.clear();
		OpList.clear();
		stringVec.clear();

		for(int j = 0; j < C; j++)
		{
			fin>>tempCom.com[0];
			fin>>tempCom.com[1];
			fin>>tempCom.com[2];
			ComList.push_back(tempCom);
		}

		fin>>D;
		for(int j = 0; j < D; j++)
		{
			fin>>tempOpposition.Op[0];
			fin>>tempOpposition.Op[1];
			OpList.push_back(tempOpposition);
		}

		fin>>N;
		fin>>tempString;
		for(int j = 0; j < N; j++)
		{
			stringVec.push_back(tempString[j]);
		}
		solve(stringVec,ComList,OpList,ansString);

		fout<<"Case #"<<i+1<<": [";
		for(int j = 0; j < ansString.size(); j++)
		{
			if(j < ansString.size() - 1)
				fout<<ansString[j]<<", ";
			else
				fout<<ansString[j];
		}
		fout<<"]\n";
	}
	return 0;
}