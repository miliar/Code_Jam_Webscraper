#include <fstream>
#include <iostream>
#include <map>


using namespace std;

int L, D, N, length;

char** dictt;

int table[15][26];

char line[1024];

char s[1024];

ifstream fin;

ofstream fout;


//map<const char*, int, ltstr> dict;

int num;

int scan;

void check()
{
	int i, l = 0, j, in = 0, flag;

	//memset(table, 0, sizeof(int) * 15 * 26);

	for(i = 0; i < 15; i ++)
	{
		for(j = 0; j < 26; j ++)
			table[i][j] = 0;
	}

	for(i = 0; i < length; i ++)
	{
		if(line[i] == ')')
		{
			in = 0;
			l ++;
		}
		else if(line[i] == '(')
		{
			in = 1;
		}
		else if(!in)
		{
			table[l][line[i] - 97] = 1;
			l ++;
		}
		else
		{
			table[l][line[i] - 97] = 1;
		}
	}

	/*for(i = 0; i < L; i ++)
	{
		for(j = 0; j < 26; j ++)
			cout << table[i][j] << " ";
		cout << endl;
	}*/

	for(i = 0; i < D; i ++)
	{
		flag = 1;
		for(j = 0; j < L && flag; j ++)
		{
			if(!table[j][dictt[i][j] - 97])
			{
				//cout << dictt[i][j] << " " << i << " " << j << endl;
				flag = 0;
			}
		}
		if(flag)
			num ++;
	}
}

bool checklen()
{
	int i, n = 0, in = 0;
	i = 0;
	while(i < length)
	{
		if(line[i] == '(')
		{
			in = 1;
			n ++;
		}
		else if(line[i] == ')')
		{
			in = 0;
		}
		else if(!in)
		{
			n ++;
		}
		
		i ++;
	}

	//cout << "l: " << n << endl;
	if(n != L)
		return 0;

	return 1;
}

void solve()
{
	int i, j;

	dictt = new char*[D];
	for(i = 0; i < D; i ++)
	{
		dictt[i] = new char[L + 1];		
		fin.getline(line, 1024);
		memcpy(dictt[i], line, sizeof(char) * L);
		dictt[i][L] = 0;

		//cout << dictt[i] << endl;

		//dict[dictt[i]] = 1;
	}


	for(i = 0; i < N; i ++)
	{
		num = 0;
		scan  = 0;
		fin.getline(line, 1024);

		length = strlen(line);
		//cout << length << " line: " << line << endl;

		if(checklen())
		{
			check();
		}	

		cout << "Case #" << i + 1 << ": " << num << endl;

		fout << "Case #" << i + 1 << ": " << num << endl;
	}	
	
	for(i = 0; i < D; i ++)
	{
		delete[] dictt[i];		
	}
	delete[] dictt;
}

int main()
{
	fin.open("A-large.in");
	fout.open("A-large.out");

	fin >> L >> D >> N;

	//cout << "L: " << L << "D: " << D << "N: " << N << endl;
	fin.getline(line, 1024);

	solve();

	fin.close();
	fout.close();
	
	return 0;
}
