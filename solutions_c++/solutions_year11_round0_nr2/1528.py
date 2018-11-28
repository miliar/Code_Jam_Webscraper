#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <cctype>
using namespace std;

string formStr(char a, char b)
{
	string str = "";
	str.push_back(a);
	str.push_back(b);
	return str;
}

string solve(int C, string strC, int D, string strD, int N, string strN)
{
	string result = "";
	
	map<string, char> compose;
	map<string, int> opposite;
	
	for(int i=0;i<strC.size();i+=3)
	{
		char a = strC[i];
		char b = strC[i+1];
		char c = strC[i+2];
		compose[formStr(a, b)] = c;
		compose[formStr(b, a)] = c;
	}
	
	for(int i=0;i<strD.size();i+=2)
	{
		char a = strD[i];
		char b = strD[i+1];
		opposite[formStr(a, b)] = 1;
		opposite[formStr(b, a)] = 1;
	}
	
	for(int i=0;i<strN.size();i++)
	{
		result.push_back(strN[i]);
		
		if(result.size() > 1)
		{
			char a = result[result.size()-2];
			char b = result[result.size()-1];
			char c = compose[formStr(a, b)];
			if(isalpha(c))
			{
				result.erase(result.end()-1);
				result.erase(result.end()-1);
				result.push_back(c);
			}
			
			for(int j=0;j<result.size()-1;j++)
			{
				a = result[j];
				b = result[result.size()-1];
				if(opposite[formStr(a, b)] > 0)
				{
					result = "";
					break;
				}
			}
		}	
	}
	
	return result;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	// {Q, W, E, R, A, S, D, F}
	
	int Test;
	cin >> Test;
	
	for(int t=1;t<=Test;t++)
	{
		int C, D, N;
		string strC, strD, strN;
		strC = "";
		strD = "";
		strN = "";
		
		cin >> C;
		if(C > 0)
		{
			string str;
			for(int i=0;i<C;i++)
			{
				cin >> str;
				strC.append(str);
			}
		}
			
		cin >> D;
		if(D > 0)
		{
			string str;
			for(int i=0;i<D;i++)
			{
				cin >> str;
				strD.append(str);
			}
		}
		
		cin >> N;
		if(N > 0)
			cin >> strN;
			
		string result = solve(C, strC, D, strD, N, strN);
		printf("Case #%d: [", t);
		for(int i=0;i<result.size();i++)
		{
			printf("%c", result[i]);
			if(i != result.size()-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
