#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

#define MOD 10000

ifstream fin;
ofstream fout;

string inp;
string digits = "0123456789abcdefghijklmnopqrstuvwxyz";
bool used[36];


int getResult()
{
	for(int i = 0; i < 36; i++)
		used[i] = false;

	int base = 0;
	for(int i = 0; i < inp.size(); i++)
	{
		base++;
		for(int j = 0; j < i; j++)
			if(inp[j] == inp[i])
			{
				base--;
				break;
			}
	}
	if(base == 1)
		base = 2;
	
	string result = "1";
	used[1] = true;
	for(int i = 1; i < inp.size(); i++)
	{
		bool ok = false;
		for(int j = 0; j < i; j++)
			if(inp[i] == inp[j])
			{
				result += result[j];
				ok = true;
				break;
			}
		if(ok) 
			continue;
		for(int j = 0; j < 36; j++)
			if(!used[j])
			{
				result += digits[j];
				used[j] = true;
				break;
			}
	}
	
	int r = 0;
	for(int i = result.size()-1, p=1; i >= 0; i--,p*=base)
	{
		for(int j = 0; j < 36; j++)
			if(result[i] == digits[j])
				r += j*p;
	}
	return r;
}

int main()
{
	int N,i,j;
	fin.open("a_small.in");
	fout.open("a_small.out");
	
	fin >> N;
	for(int t = 1; t <= N; t++)
	{
		fin >> inp;
		fout << "Case #" << t << ": " << getResult() << endl;
	}
	fout.close();
	fin.close();
	return 0;
}
