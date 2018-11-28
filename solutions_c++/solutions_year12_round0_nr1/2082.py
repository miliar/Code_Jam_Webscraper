#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;

char m[200];
void process(const char* c, const char* tr)
{
	int k = strlen(c);
	int i;
	for(i = 0; i < k; i++)
	{
		m[c[i]] = tr[i];
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tt;
	char c[10005];
	process("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	process("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	process("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	process("y qee", "a zoo");
	process("z", "q");
	cin >> tt;
	cin.getline(c, 10005);
	int ii;
	for(ii = 1; ii <= tt; ii++)
	{
		cin.getline(c, 10005);
		int k = strlen(c);
		int i;
		cout << "Case #" << ii <<": ";
		for(i = 0; i < k; i++)
		{
			cout << m[c[i]];
		}
		cout << endl;
	}
/*	int i;
	for(i = 'a'; i <= 'z'; i++)
	{
		cout << char(i);
	}
	cout << endl;
	for(i = 'a'; i <= 'z'; i++)
	{
		cout << m[i];
	}
	cout << endl;*/
	return 0;
}
