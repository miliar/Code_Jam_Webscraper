#include<fstream>
#include<string>
#include<vector>
#include<iostream>
using namespace std;


char checkWin(vector<vector<char>>& v);
int main(){

	ifstream fin;
	ofstream fout;
	int casenum, tisize(4);
	fin.open("input.txt");
	fout.open("output.txt");
	vector<vector<char>> v;
	
	vector<char> temp,state;
	fin>>casenum;
	
	for(int cn=0; cn<casenum;cn++)
	{
		char c;
		for(int i=0;i<tisize;i++)
		{
				for(int j=0; j<tisize; j++)
				{
			
					fin>>c;
					temp.push_back(c);
				}
		
				v.push_back(temp);
				temp.clear();

		}		
		state.push_back(checkWin(v));

		
	
	v.clear();
	
	
	}


	for(int i=1; i<=casenum;i++)
	{
		fout<<"Case #"<<i<<": ";
		switch (state[i-1])
		{
		case 'X':
			fout<<"X won";
			break;
		case 'O':
			fout<<"O won";
			break;
		case 'N':
			fout<<"Game has not completed";
			break;
		case 'D':
			fout<<"Draw";

			default:
				break;
		}

		fout<<endl;
	}

	

}

char checkWin(vector<vector<char>>& v)
{
	vector<int> count;
	int temp(0);
	bool isdot =false;
	for(int i=0; i<4;i++)
		count.push_back(temp);
	for(int i=0; i<v.size(); i++)
	{
		for(int j=0; j<v[i].size();j++)
		{
			switch (v[i][j])
			{
				case 'X':
					count[0]++;
					break;
				case 'O':
					count[1]++;
					break;
				case 'T':
					count[2]++;
					break;
				case '.':
					count[3]++;
					break;
				default:
					break;
			}

		}
		if(count[3]>0)
			isdot =true;
		else if(count[0]+count[2] ==v.size())
			return 'X';
		else if(count[1]+count[2]==v.size())
			return 'O';
		for(int j=0; j<count.size(); j++)
			count[j]=0;
	}
	//row
for(int i=0; i<v.size(); i++)
	{
		for(int j=0; j<v[i].size();j++)
		{
			switch (v[j][i])
			{
				case 'X':
					count[0]++;
					break;
				case 'O':
					count[1]++;
					break;
				case 'T':
					count[2]++;
					break;
				case '.':
					count[3]++;
					break;
				default:
					break;
			}

		}
		if(count[3]>0)
			isdot =true;
		else if(count[0]+count[2] ==v.size())
			return 'X';
		else if(count[1]+count[2]==v.size())
			return 'O';
		for(int j=0; j<count.size(); j++)
			count[j]=0;
	}
//dia
for(int i=0;i<v.size();i++)
{
	int edge=v.size()-1;
	switch (v[i][edge-i])
	{
		case 'X':
			count[0]++;
			break;
		case 'O':
			count[1]++;
			break;
		case 'T':
			count[2]++;
			break;
		case '.':
			count[3]++;
			break;
		default:
			break;
	}
}
if(count[3]>0)
	isdot =true;
else if(count[0]+count[2] ==v.size())
	return 'X';
else if(count[1]+count[2]==v.size())
	return 'O';
for(int j=0; j<count.size(); j++)
	count[j]=0;
for(int i=0;i<v.size();i++)
{
	int edge=v.size()-1;
	switch (v[i][i])
	{
		case 'X':
			count[0]++;
			break;
		case 'O':
			count[1]++;
			break;
		case 'T':
			count[2]++;
			break;
		case '.':
			count[3]++;
			break;
		default:
			break;
	}
}
if(count[3]>0)
	isdot =true;
else if(count[0]+count[2] ==v.size())
	return 'X';
else if(count[1]+count[2]==v.size())
	return 'O';
for(int j=0; j<count.size(); j++)
	count[j]=0;
if(isdot)
	return 'N';
else
	return 'D';

}



