#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>


using namespace std;


vector<string> getstrs(string str, int l)
{
	vector<string> vecstr;
	string str1;
	char chs[2];

	chs[1]='\0';

	for (int i=0;i<str.length();++i)
	{
		str1.clear();
		if (str.c_str()[i] == '(')
		{
			for (++i;i<str.length() && str.c_str()[i] != ')';++i)
			{
				chs[0] = str.c_str()[i];
				str1.append(chs);
			}
			vecstr.push_back(str1);
		}
		else
		{
			chs[0]=str.c_str()[i];
			str1.append(chs);
			vecstr.push_back(str1);
		}
	}

	if (vecstr.size() != l)
	{
		cout <<"Error getstrs size"<<vecstr.size()<<" l="<<l;
	}

	return vecstr;
}


int calculate(const set<string> &as, vector<string> strs)
{
	string str;
	int cnt=0;

	for (set<string>::const_iterator iter=as.begin(); iter!=as.end(); ++iter)
	{
		str = (*iter);

		int i=0;
		for (string::iterator it=str.begin(); it!=str.end(); ++it)
		{
			char ccc=(*it);
			if (find(strs[i].begin(), strs[i].end(), (*it)) == strs[i].end())
				break;
			++i;
		}

		if (i == str.size())
			++cnt;
	}

	return cnt;
}

int main()
{
	int nTestCases;
	int l, d, n;
	char alienstr[1024];

	set<string> alienstrs;

	FILE *in_file;
	FILE *out_file;

	if ((in_file = fopen("prob1_in.txt", "r")) == 0)
	{
		cout <<"in err\n";
	}

	if ((out_file = fopen("prob1_out.txt", "w+")) == 0)
	{
		cout <<"Out err\n";
	}

//#define in_file stdin
//#define out_file stdout

	fscanf(in_file, "%d %d %d", &l, &d, &n);

	for (int i=1;i<=d;++i)
	{
		fscanf (in_file, "%s", alienstr);

		alienstrs.insert(string(alienstr));
	}

	vector<string> strs;
	int ret;

	for (int i=1;i<=n;++i)
	{
		fscanf (in_file, "%s", alienstr);

		strs = getstrs(alienstr, l);

		ret = calculate (alienstrs, strs);

		fprintf (out_file, "Case #%d: %d\n", i, ret); 
	}

	fclose(in_file);
	fclose(out_file);

	return 0;
}