#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int L, D, N;
string dict[5000];

int calculate(string test)
{
	int index = 0;
	bool mat[5000][15] = {false};
	int count = 0;

	for(int i = 0; i < L; i++)
	{
		if(test[index] == '(')
		{
			index++;
			while(test[index] != ')')
			{
				for(int j = 0; j < D; j++)
				{
					if(dict[j][i] == test[index])
					{
						mat[j][i] = true;
					}
				}
				index++;
			}			
			index++;
		}
				
		else
		{
			for(int j = 0; j < D; j++)
			{
				if(dict[j][i] == test[index])
				{
					mat[j][i] = true;
				}
			}
			index++;
		}
	}
	
	for(int i = 0; i < D; i++)
	{
		int flag = true;
		
		for(int j = 0; j < L; j++)
		{
			if(!mat[i][j])
			{
				flag = false;
				break;	
			}
		}
		if(flag)
		{
			count++;
		}
	}
	return count;
}

int main()
{
	ifstream fin;
	ofstream fout;
	
	fin.open("A-large.in");
	fout.open("A-large.out");
	
	fin>>L>>D>>N;
	
	for(int i = 0; i < D; i++)
	{
		fin>>dict[i];
	}
	
	for(int i = 0; i < N; i++)
	{
		string test;
		
		int count = 0;		
		fin>>test;
		
		count = calculate(test);
		
		fout<<"Case #"<<i + 1<<":"<<" "<<count<<endl;
	}
	
	cout<<"Done"<<endl;	
}

			
							
	
	
