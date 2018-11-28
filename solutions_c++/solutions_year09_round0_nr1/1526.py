#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
	ifstream in("D:\\A-large.in.txt");
	ofstream out("D:\\result.txt");
	
	int L, D, N;
	in >> L >> D >> N;

	char ** arr = (char**)malloc(sizeof(char*) * D);
	for(int i = 0; i < D; i++)
	{
		arr[i] = (char*)malloc(sizeof(char) * (L + 1));
		in >> arr[i];
	}

	char *word = (char*)malloc(sizeof(char) * 1000);
	for(int i = 0; i < N; i++)
	{
		in >> word;
		int num = 0;

		for(int j = 0; j < D; j++)
		{
			char *target = arr[j];
			int len = strlen(word);
			int k = 0;
			bool find = true;
			for(int pos = 0; pos < len; pos++, k++)
			{
				if(word[pos] == '(')
				{
					bool f = false;
					for(; word[pos] != ')'; pos++)
					{
						if(word[pos] == target[k])
						{
							f = true;
						}
					}
					if(f == true)
					{
						continue;
					}
					else
					{
						find = false;
					}
				}
				else
				{
					if(word[pos] != target[k])
					{
						find = false;
					}
				}
			}
			if(find == false)
			{
				continue;
			}
			else
			{
				num++;
			}
		}

		out << "Case #" << i + 1 << ": " << num << endl;
	}

	out.flush();

	free(word);
	for(int i = 0; i < D; i++)
	{
		free(arr[i]);
	}
	free(arr);
}