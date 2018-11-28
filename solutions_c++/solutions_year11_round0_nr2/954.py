#include <iostream>
#include <map>
#include <vector>
#include <fstream>

//Q, W, E, R, A, S, D, F

using namespace std;

int cti(char a)
{
	switch (a)
	{
	case 'Q':
		return 0;
		break;
	case 'W':
		return 1;
		break;
	case 'E':
		return 2;
		break;
	case 'R':
		return 3;
		break;
	case 'A':
		return 4;
		break;
	case 'S':
		return 5;
		break;
	case 'D':
		return 6;
		break;
	case 'F':
		return 7;
		break;
	}
	return 8;
}

int main()
{
	ofstream fout;
	fout.open("output.txt");
	int cases;
	cin>>cases;
	int inpi;
	char inpc[150];
	char combines[9][9];
	multimap<char,char> destroys;
	vector<char> answer;
	pair<multimap<char,char>::iterator, multimap<char,char>::iterator> ii;
    multimap<char,char>::iterator it;

	for (int h=0;h<cases;h++)
	{
		for (int i=0;i<9;i++) for (int j=0;j<9;j++) combines[i][j]=0;
		answer.clear();
		destroys.clear();
		cin >>inpi;
		for (int i=0;i<inpi;i++)
		{
			cin>>inpc;
			combines[cti(inpc[0])][cti(inpc[1])]=inpc[2];
			combines[cti(inpc[1])][cti(inpc[0])]=inpc[2];
		}
		cin >>inpi;
		for (int i=0;i<inpi;i++)
		{
			cin>>inpc;
			destroys.insert(pair<char,char>(inpc[0],inpc[1]));
			destroys.insert(pair<char,char>(inpc[1],inpc[0]));
		}
		cin>>inpi;
		cin>>inpc;
		for (int i=0;i<inpi;i++)
		{
			if (answer.size()==0) answer.push_back(inpc[i]);
			else if (combines[cti(answer[answer.size()-1])][cti(inpc[i])]!=0) 
			{
				answer[answer.size()-1]=combines[cti(answer[answer.size()-1])][cti(inpc[i])];
				continue;
			}
			else if (destroys.count(inpc[i])>0)
			{
				bool flag=false;
				ii=destroys.equal_range(inpc[i]);
				for(it = ii.first; it != ii.second; it++)
				{
					char tmp=it->second;
					for (int j=0;j<answer.size();j++)
					{
						if (answer[j]==tmp) flag=true;
					}
				}
				if (flag==true) answer.clear();
				if (flag==false) answer.push_back(inpc[i]);
			}
			else
			{
				answer.push_back(inpc[i]);
			}
		}
		fout<<"Case #"<<h+1<<": [";
		for (int i=0;i<answer.size();i++)
		{
			fout<<answer[i];
			if (i!=answer.size()-1) fout<<", ";
		}
		fout<<"]"<<endl;
	}
	fout.close();
}
