#include<iostream>
#include<fstream>
#include<string>
using namespace std;


int Solvefornum(string* letters, int L_num, string Testcase, int Length);

bool match(string letter, string Tcase, int Length);

void main()
{
		string dummy;
		fstream file_op("c:\\answers.txt", ios::out);
		fstream file_rp("c:\\problem.txt", ios::in);

		int Length;
		file_rp>>Length;

		//getting all strings
		string* letters;
		int L_num;
		file_rp>>L_num;

		//getting all testcases
		string* Testcase;
		int Times;
		file_rp>>Times;

		getline(file_rp,dummy);

		letters = new string[L_num];
		for(int cnt = 0; cnt < L_num; cnt++)
		{
			getline(file_rp,letters[cnt]);
		}

		Testcase = new string[Times];
		for(int cnt = 0; cnt < Times; cnt++)
		{
			getline(file_rp,Testcase[cnt]);
		}

		//solving the numbers.
		for(int i =0; i < Times; i++)
		{
			int round = Solvefornum(letters, L_num, Testcase[i], Length);
			file_op<<"Case #"<<(i+1)<<": "<<round<<endl;
		}
		file_rp.close();
		file_op.close();
		return;

}


	
int Solvefornum(string* letters, int L_num, string Testcase, int Length)
{
	int count = 0;
	for(int i =0; i < L_num; i++)
	{
		string temp = letters[i];
		if(match(temp,Testcase,Length))
			count++;
	}
	return count;
}

bool match(string letter, string Tcase, int Length)
{
	int pos = 0;
	int size = Tcase.size();
	for(int i = 0; i < Length; i++)
	{
		if(Tcase[pos] == '(')
		{
			bool match = false;
			while(Tcase[pos] != ')')
			{
				if(letter[i] == Tcase[pos])
					match = true;
				pos++;
			}
			if(match)
			{
				pos++;
				continue;
			}
			else
				return false;
		}
		else
		{
			if(letter[i] != Tcase[pos])
				return false;
			pos++; 
			continue;
		}
	}
	return true;
}
