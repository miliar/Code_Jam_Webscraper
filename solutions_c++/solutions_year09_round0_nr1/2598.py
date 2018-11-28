#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int sov(int count, string temp);
void TestString(string s_temp);
char **data;
int **check;
	int n_token;
	int n_pattern;
	int n_testcase;

int main()
{
	
	ifstream fin("A-large.in");
	ofstream fout("output.txt");


	fin >> n_token;
	fin >> n_pattern;
	fin >> n_testcase;
	
	string s_temp;

	data = new char*[n_pattern];
	check = new int*[n_pattern];
	for(int i=0; i<n_pattern; i++)
	{
		data[i] = new char[n_token+1];
		check[i] = new int[n_token+1];
		fin >> s_temp;
		for(int j=0; j<n_token; j++)
		{
			data[i][j] = s_temp[j];
			check[i][j] = 0;
	
		}
		data[i][n_token] = '\0';
	}

	/*for(int i=0; i<n_pattern; i++)
	{
		for(int j=0; j<n_token; j++)
		{
			cout << data[i][j];
		}
		cout << endl;
	}*/
	

	for(int tt=0; tt<n_testcase; tt++)
	{
		fin >> s_temp;
		int length = s_temp.length();
		int flag = 0;    // 0이면 괄호 없을시, 1이면 괄호처리시
		int count = 0;
		int tokennumber = 0;
		for(int i=0; i<length; i++)
		{
			if(s_temp[i] == '(')
			{
				while(s_temp[i] != ')')
				{
					for(int j=0; j<n_pattern; j++)
					{
						if(data[j][tokennumber] == s_temp[i])
						{
							check[j][tokennumber] = 1;
						}
					}
					i++;
				}
				tokennumber++;
				continue;
			}
			else if(s_temp[i] != '(' || s_temp[i] != ')')
			{
				for(int j=0; j<n_pattern; j++)
				{
					if(data[j][tokennumber] == s_temp[i])
					{
						check[j][tokennumber] = 1;
					}
				}
				tokennumber++;
				continue;
			}
		}
		int sum = 0;
		int number = 0;
		for(int k=0; k<n_pattern; k++)
		{

			for(int l=0; l<n_token; l++)
			{
				sum += check[k][l];
				check[k][l] = 0;
			}	
			if(sum == n_token)
			{
				number++;
			}
			sum = 0;
		}

		fout << "Case #" << tt+1 << ": " << number << endl;
	



	}

	return 1;
}
