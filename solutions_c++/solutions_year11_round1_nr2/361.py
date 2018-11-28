// r1p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int fit(string a, string b)
{
	if (a.length() != b.length())
		return 0;
	
	int l = a.length();
	for(int i=0;i<l;i++)
	{
		if (a[i] == '*' || b[i] == '*')
			continue;

		if (a[i] != b[i])
			return 0;
	}

	return 1;
}

int count(string word, string list, vector<string> D)
{
	string bb(word);
	for(int i=0;i<bb.length();i++)
		bb[i] = '*';

	int count = 0;
	for(int i=0;i<list.length();i++)
	{
		char g = list[i];
		bool bflag = false;

		for(int j=0;j<D.size();j++)
		{
			if (fit(D[j], bb))
			{
				for(int k=0;k<D[j].length();k++)
				{
					if (D[j][k] == g)
					{
						bflag = true;
						break;
					}
				}
				if (bflag)
					break;
			}
		}

		if (!bflag)
			continue;
		
		bool bfail = true;
		for(int j=0;j<word.length();j++)
		{
			if (word[j] == g)
			{
				bb[j] = g;
				bfail = false;
			}
		}

		// remove impossible word
		for(int j=0;j<D.size();j++)
		{
			string& str = D[j];
			if (str.length() != bb.length())
			{
				str.clear();
				continue;
			}
			for(int k=0;k<str.length();k++)
			{
				if ( (str[k] == g) & (word[k] != g))
				{
					str.clear();
					break;
				}
			}
		}

		if (bfail)
			count++;

		bool bflag2 = true;;
		for(int j=0;j<bb.length();j++)
		{
			if (bb[j] == '*')
			{
				bflag2 = false;
				break;
			}
		}

		if (bflag2)
			return count;
	}

	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

	cin >> T;
	for(int i=0;i<T;i++)
	{
		int N, M;
		cin >> N;
		cin >> M;

		vector<string> D;
		vector<string> L;

		for(int j=0;j<N;j++)
		{
			string str;
			cin >> str;
			D.push_back(str);
		}

		for(int j=0;j<M;j++)
		{
			string str;
			cin >> str;
			L.push_back(str);
		}

		printf("Case #%d:", i+1);
		for(int j=0;j<M;j++)
		{
			int Max = -1;
			int MaxIdx = 0;
			for(int k=0;k<N;k++)
			{
				int v = count(D[k], L[j], D);
				if (v > Max)
				{
					Max = v;
					MaxIdx = k;
				}
			}
			// printf(" %s", D[MaxIdx]);
			cout <<  " " << D[MaxIdx];
		}
		printf("\n");
	}


	return 0;
}

