#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream fin;
ofstream fout;

int calc(const string & s, int k, int * num)
{
	int pos = 0;
	int n = s.length();
	string news = s;
	while (pos < n)
	{
		for (int i = 0; i < k; ++ i) news [pos + i] = s[pos + num[i]];
		pos += k;
	}
	int res = 1;
	for (int i = 1; i < n; ++ i)
	{
		if (news [i] != news[i - 1]) ++ res;
	}
	return res;
}

int main (int argc, char * argv [])
{

	if (argc  == 1)
	{
		fin.open("input.txt");
		fout.open("output.txt");
	}
	else
	{
		fin.open(argv[1]);
		fout.open(argv[2]);
	}

	int tests = 0;
	fin >> tests;

	while (tests -- > 0)
	{
		int k ;
		string s;
		int n ;

		fin >> k >> s;
		int num[10];
		for (int i = 0; i < k; ++ i) {
			num [i] = i;
		}

		int res = s.length();
		do 
		{
			int curr = calc(s, k, num);
			res = min (res, curr);
		}
		while (next_permutation(num, num + k));

		static int caseNum = 0;
		fout << "Case #" <<  (++ caseNum) << ": " << res << endl;
	}

	return 0;
}