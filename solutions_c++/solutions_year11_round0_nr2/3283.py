#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>
#include <stdio.h>
#include <conio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int nTestCases;
int caseNumber;
int C;
int D;
int N;
vector<string> vc;
vector<string> vd;
string sn;

string ProcessCase()
{
	string ret;
	string list = "";
	for (int i=0; i<sn.length(); i++)
	{
		char newchar = sn[i];
		int ll = list.length();
		if (ll == 0)
		{
			list.append(1,newchar);
			continue;
		}
		bool combined = false;
		//check for combined
		for (vector<string>::iterator it = vc.begin(); it != vc.end(); it++)
		{
			string s = *it;
			char lastchar = list[ll-1];
			if (
				((s[0]==lastchar) && (s[1]==newchar))
				||
				((s[1]==lastchar) && (s[0]==newchar))
				)
			{
				//combine
				list = list.substr(0, ll-1);
				list.append(1,s[2]);
				combined = true;
				break;
			}
		}
		if (combined)
			continue;
		//check for opposed
		bool opposed = false;
		for (vector<string>::iterator it = vd.begin(); it != vd.end(); it++)
		{
			string s = *it;
			if (newchar==s[0])
				if (strchr(list.c_str(), s[1]) != NULL )
					opposed = true;
			if (opposed)
				break;
			if (newchar==s[1])
				if (strchr(list.c_str(), s[0]) != NULL )
					opposed = true;
			if (opposed)
				break;
		}
		if (opposed)
		{
			list = "";
			continue;
		}
		list.append(1, newchar);
	}

	int ll = list.length();
	ret = "";
	for (int i=0; i<ll; i++)
	{
		if (i==ll-1)
			ret.append(1,list[i]);
		else
		{
			ret.append(1,list[i]);
			ret.append(", ");
		}
	}
	ret = "[" + ret + "]";
	return ret;
}


int main()
{
	string file1;
	string file2;
	file1 = "e:\\zin.txt";
	file2 = "e:\\z2.out";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// comment this line for console output:
	freopen_s(&ps, file2.c_str(), "wt", stdout);
	scanf("%d", &nTestCases);
	for (int caseNumber=1; caseNumber<=nTestCases; caseNumber++)
	{
		vc.clear();
		vd.clear();
		char st[110];
		scanf("%d", &C);
		for (int i=0; i<C; i++)
		{
			scanf("%s", st);
			string s;
			s.assign(st);
			vc.push_back(s);
		}
		scanf("%d", &D);
		for (int i=0; i<D; i++)
		{
			scanf("%s", st);
			string s;
			s.assign(st);
			vd.push_back(s);
		}
		scanf("%d", &N);
		scanf("%s", st);
		sn.assign(st);
		string result = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		cout << result << endl;
	}
	return 0;
}
