/*
 * fmain.cpp
 *
 *  Created on: 2009-9-3
 *      Author: sunguoyang07
 *      E-mail: matrixworker@gamil.com
 *  This is the solution for "welcome to code jam",code jam 2009.
 */

#include <iostream>
#include <fstream>
#include <string>
#include <stack>
using namespace std;

class CProblem
{
private:
	int MAXN;
	int** memory;
	string pattern,text;

public:
	CProblem()
	{
		MAXN = 512;
		memory = new int* [MAXN];
		for(int i=0;i<MAXN;i++)
		{
			memory[i]=new int[MAXN];
		}
		for(int i=0;i<MAXN;i++)
			for(int j=0;j<MAXN;j++)
				memory[i][j]=-1;
	}

	~CProblem()
	{
		for(int i=0;i<MAXN;i++)
			delete []memory[i];
		delete []memory;
	}

	void clear_cell()
	{
		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < MAXN; j++)
				memory[i][j] = -1;
	}

	int doit(unsigned int i, unsigned int j)
	{
		int& result = memory[i][j];
		if (result != -1)
		{
			return result;
		}
		else if (i == pattern.size()-1)
		{
			if(j>=text.size())
				result =0;
			else if(pattern[i]==text[j])
				result = (1+ doit(i,j+1))%10000;
			else
				result = doit(i,j+1);
		}
		else
		{
			int sum = 0;
			for(unsigned int a=j;a<text.size();a++)
				if(text[a]==pattern[i])
				{
					sum += doit(i+1,a+1);
					sum %=10000;
				}
			result = sum;
		}
		return result;
	}

	string match(string pattern, string text)
	{
		this->pattern = pattern;
		this->text = text;
		int result = doit(0, 0);
		string str;

		while (result > 0)
		{
			int mod = result % 10;
			result /=10;
			str.insert(str.begin(), '0'+mod);
		}
		while (str.size() < 4)
			str.insert(str.begin(), '0');
		return str;
	}
};

int main()
{
	ifstream fin("input.txt", ifstream::in);
	ofstream fout("output.txt", ofstream::out);
	int num, i;
	string pattern = "welcome to code jam";
	string text;
	string result;

	string num_str;
	getline(fin,num_str,'\n');
	num = atoi(num_str.c_str());

	CProblem problem;
	for(i=1;i<=num;i++)
	{
		getline(fin,text,'\n');
		result=problem.match(pattern,text);
		problem.clear_cell();
		fout<<"Case #"<<i<<": "<<result<<endl;
	}

	fin.close();
	fout.close();
	return 0;
}
