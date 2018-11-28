#pragma comment(linker, "/STACK:836777216")

#define INF (int)1e9
#define EPS 1e-9
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

int t;
string code = "yhesocvxduiglbkrztnwjpfmaq";
char ch;
string s;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ", i);
		while (ch != '\n')
		{
			cin>>s;
			for (int j=0;j<s.length();j++)
				printf("%c", code[s[j]-'a']);
			printf(" ");
			scanf("%c", &ch);
		}
		ch='a';
		printf("\n");
	}
	return 0;
}