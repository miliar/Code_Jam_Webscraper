// test.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<fstream>
using namespace std;


bool TestCaseCheck(char* TestCase,char* TestString, int L);

int main(int argc, char* argv[])
{
	ifstream fin("c:/A-large.in");

	int L=0,D=0,N=0;

	fin>>L>>D>>N;

	char **cpp = new char*[D];
	
	for(int i=0;i<D;++i)
	{
		cpp[i] = new char[L];
		fin>>cpp[i];
	}

	ofstream fout("c:/A-large.out");
	char cp[500];	
	for(int i = 0; i < N; ++i)
	{
		fin>>cp;
		
		int k = 0;

		for(int j = 0; j < D; ++j)
		{
			if(TestCaseCheck(cp,cpp[j],L))
			{
				++k;
			}
		}

		fout<<"Case #"<<i+1<<": "<<k<<endl;
	}

	for(int i = 0; i < D; ++i)
	{
		cpp[i] = 0;
		delete []cpp[i];
	}
	delete []cpp;
	
	return 0;
}

bool TestCaseCheck(char* TestCase,char* TestString,int L)
{
	int i = 0, j = 0;

	while(TestCase[i] != '\0')
	{
		if(TestCase[i] != '(')
		{
			if(TestCase[i] == TestString[j])
			{
				++j;
				if(j == L)
				{
					return true;
				}
			}
		}
		else
		{
			bool aFlag = true;

			while(TestCase[i] != ')')
			{
				if(aFlag && TestCase[i] == TestString[j])
				{
					++j;
					aFlag = false;
					if(j == L)
					{
						return true;
					}
				}
				++i;
			}
			if(aFlag)
			{
				return false;
			}
		}
		++i;
	}
		
	return false;
}