#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstdlib>
#include<string>
#include<cassert>

using namespace std;

void invoke(char base, char result[], string opposes[], int ogroups, string combines[], int cgroups, int & resultlen);
char combdo(char base, char cand, string combines[], int cgroups);
bool cleardo(char base, char result[], int &resultlen, string opposes[], int ogroups);

int main()
{
	int numcases; int cgroups; int ogroups; int spellchars; string spell; char result[100];
	cin >> numcases; int resultlen;
	int onemoreindex;
	for(int index=1; index<=numcases; index++)
	{
		cin >> cgroups;
		string *combines = new string[cgroups];
		for(int i=0; i<cgroups; i++)
			cin >> combines[i];
		cin >> ogroups;
		string *opposes = new string[ogroups];
		for(int j=0; j<ogroups; j++)
			cin >> opposes[j];
		cin >> spellchars >> spell;
		for(int k=0; k<100; k++)
			result[k] = '.';
		resultlen = 0;
		for(int invokedex=0; invokedex < spellchars; invokedex++)
			invoke(spell[invokedex], result, opposes, ogroups, combines, cgroups, resultlen);
		cout << "Case #" << index << ": [";
		if(result[0]!='.')
			cout << result[0];
		onemoreindex=1;
		while(result[onemoreindex]!='.' && onemoreindex<=100)
		{
			cout << ", " << result[onemoreindex];
			onemoreindex++;
		}
		cout << "]" << endl;
		delete[] combines; delete[] opposes;	
	}
	return 0;
}

void invoke(char base, char result[], string opposes[], int ogroups, string combines[], int cgroups, int & resultlen)
{
	if(resultlen == 0)
	{
		result[0] = base;
		resultlen++;
	}
	else if(combdo(base,result[resultlen-1], combines, cgroups)!= '.')
	{
		result[resultlen-1] = combdo(base,result[resultlen-1], combines, cgroups);
	}
	else if(cleardo(base, result, resultlen, opposes, ogroups))
	{
	}
	else
	{
		result[resultlen]=base;
		resultlen++;
	}
}

char combdo(char base, char cand, string combines[], int cgroups)
{
	for(int i=0; i<cgroups; i++)
	{
		if(combines[i][0] == base && combines[i][1] == cand)
			return combines[i][2];
		if(combines[i][0] == cand && combines[i][1] == base)
			return combines[i][2];
	}
	return '.';
}

bool cleardo(char base, char result[], int &resultlen, string opposes[], int ogroups)
{
	for(int i=resultlen-1; i>=0; i--)
	{
		for(int j=0; j<ogroups; j++)
		{
			if(opposes[j][0] == base && opposes[j][1] == result[i])
			{	
				for(int k=0; k<resultlen; k++)
					result[k] = '.';
				resultlen=0;
				return true;
			}
			if(opposes[j][0] == result[i] && opposes[j][1] == base)
			{
				for(int k=0; k<resultlen; k++)
					result[k] = '.';
				resultlen=0;
				return true;				
			}
		}
	}
	return false;
}
