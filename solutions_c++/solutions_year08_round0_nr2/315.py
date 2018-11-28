#include <iostream>
#include <fstream>
#include <list>
#include <string.h>
using namespace std;

typedef list<int> li;
li AD, AA, BD, BA;

int main()
{
	ifstream f("B.in");
	ofstream ff("B.out");
	int N, Ni, T, NA, NB, i;

	f >> N;

	for(Ni = 1; Ni <= N; ++Ni)
	{
		int A = 0, B = 0, t;
		char s[3], c;

		f >> T;
		f >> NA >> NB;
		s[2] = 0;
		for(i = 0; i < NA; ++i)
		{
			f >> s[0] >> s[1];
			t = atoi(s) * 60;
			f >> c >> s[0] >> s[1];
			t += atoi(s);
			AD.push_back(t);
			f >> s[0] >> s[1];
			t = atoi(s) * 60;
			f >> c >> s[0] >> s[1];
			t += atoi(s) + T;
			BA.push_back(t);
		}
		for(i = 0; i < NB; ++i)
		{
			f >> s[0] >> s[1];
			t = atoi(s) * 60;
			f >> c >> s[0] >> s[1];
			t += atoi(s);
			BD.push_back(t);
			f >> s[0] >> s[1];
			t = atoi(s) * 60;
			f >> c >> s[0] >> s[1];
			t += atoi(s) + T;
			AA.push_back(t);
		}

		AD.sort();
		AA.sort();
		BD.sort();
		BA.sort();

		while(!AD.empty())
		{
			if((!AA.empty()) && (AA.front() <= AD.front())) AA.pop_front();
			else ++A;
			AD.pop_front();
		}
		while(!AA.empty()) AA.pop_back();
		while(!BD.empty())
		{
			if((!BA.empty()) && (BA.front() <= BD.front())) BA.pop_front();
			else ++B;
			BD.pop_front();
		}
		while(!BA.empty()) BA.pop_back();

		ff << "Case #" << Ni << ": " << A << " " << B << endl;
	}

	return 0;
}