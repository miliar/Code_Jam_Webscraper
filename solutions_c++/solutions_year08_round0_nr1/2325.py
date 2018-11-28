#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int findstr(string target, int start, string list[], int len);
string Switch(int start, string q[], string s[], int lenS, int lenQ, string curr);

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int N;
	int S;
	int Q;
	int i = 0;
	int j;
	int switches;
	
	string* engines;
	string* queries;

	string currEng;

	fin>>N;

	while(i < N)
	{
		switches = 0;

		fin>>S;
		engines = new string[S];
		getline(fin,engines[0]);
		for(j = 0; j < S; j++)
			getline(fin,engines[j]);

		fin>>Q;
		if(Q == 0)
			goto print;
		queries = new string[Q];
		getline(fin,queries[0]);
		for(j = 0; j < Q; j++)
			getline(fin,queries[j]);

		currEng = Switch(0,queries,engines,S,Q,"");
		for(j = 1; j < Q; j++)
		{
			if(queries[j] == currEng)
			{
				switches++;
				currEng = Switch(j,queries,engines,S,Q,currEng);
			}
		}

		delete []queries;
print:
		if(i < N-1)
			fout<<"Case #"<<i+1<<": "<<switches<<endl;
		else
			fout<<"Case #"<<i+1<<": "<<switches;

		delete []engines;

		i++;
	}

	fin.close();
	fout.close();

	return 0;
}

string Switch(int start, string q[], string s[], int lenS, int lenQ, string curr)
{
	int index = -2;
	int temp;
	int i;
	for(i = 0; i < lenS; i++)
	{
		temp = findstr(s[i],start,q,lenQ);
		if(temp == -1)
			return s[i];
		else if(temp > index && q[temp] != curr)
			index = temp;
	}

	return q[index];
}

int findstr(string target, int start, string list[], int len)
{
	int i = start;
	int index = -1;
	while(i != len)
	{
		if(list[i] == target)
		{
			index = i;
			break;
		}
		i++;
	}

	return index;
}