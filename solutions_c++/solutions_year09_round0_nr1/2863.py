#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>


#define LEN  16
#define MAX_LETT 26
#define MAX_DIC_SIZE 5000
#define MAX_TEST_SIZE 500
#define MAX_INPUT_LEN (28 * LEN)

using namespace std;

bool match(char* line, int L, int word[LEN][MAX_LETT] )
{
	bool found = true;

	for (int i = 0; i < L; i++)
	{
		if (word[i][ line[i] - 'a' ] == 0)
		{
			found =false;
			break;
		}
	}
	return found;
}

int countMatch(char dic[MAX_DIC_SIZE][LEN], int D, int L, int word[LEN][MAX_LETT])
{
	int cnt = 0;
	for (int i = 0; i < D; i++)
	{
		if (match(dic[i], L, word))
		{
			cnt ++;
		}
	}
	return cnt;
}

void readLine(char line[MAX_INPUT_LEN], int word[LEN][MAX_LETT])
{
	int letId = 0;
	int inp = 0;
	for (int i = 0; i < strlen(line); i++)
	{
		if (line[i] == ')')
		{
			inp = 0;
			letId ++;
		}
		else if (line[i] == '(')
		{
			inp = 1;
		}
		else
		{
	
			word[letId][line[i] - 'a'] = 1;
			if(0 == inp)
			{
				letId ++;
			}
		}
	}		
}

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("out.txt");

	char dic[MAX_DIC_SIZE][LEN];
	memset(dic, 0, MAX_DIC_SIZE * LEN * sizeof(char));

	int L = 0;
	int D = 0;
	int N = 0;

	fin >> L >> D >> N;

	for (int i = 0; i < D; i++)
	{
		fin >> dic[i];
	}
	
	int cnt[MAX_TEST_SIZE];
	memset(cnt, 0, sizeof(int) * MAX_TEST_SIZE);

	
	char testline[MAX_INPUT_LEN];

	int word[LEN][MAX_LETT];

	for (int i = 0; i < N; i++)
	{
		fin >> testline;
		memset(word, 0, sizeof(int) * LEN * MAX_LETT);

		readLine( testline, word);

		int cnt = countMatch(dic, D, L, word);

		fout << "Case #" << i+1 << ": " << cnt << endl;


	}



	


	
}