
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#ifdef _DEBUG
#define DBG printf
#else
#define DBG if(0) 
#endif


char combo[4];
char oppose[3];
char mystr[1024];

bool iscombo(char a, char b)
{
	if (combo[0] == a && combo[1] == b)
		return true; 
	if (combo[0] == b && combo[1] == a)
		return true; 
	return false; 
}

bool isoppose(char a, char b)
{
	if (oppose[0] == a && oppose[1] == b)
		return true; 
	if (oppose[0] == b && oppose[1] == a)
		return true; 
	return false; 
} 

void solve(char* mystr)
{
	vector<char> s ; 
	list<char> sl; 
	int i; 
	for(i = 0 ;i < strlen(mystr); ++i)
			s.push_back(mystr[i]);
			

	for(i=1; i<s.size();++i)
	{
		int k = i-1;
		while( k >0 && mystr[k] == ' ') 
			--k;
		if (iscombo(mystr[k], mystr[i]))
		{
			mystr[i] = combo[2];
			mystr[k] = ' ';
		}
		for ( k = 0; k < i; ++k)
		{
			if (isoppose(mystr[i], mystr[k]))
			{
				for(int p=0;p<=i;++p)
				{
					mystr[p] = ' ';
				}
				break;
			}
		}
			

	}

	printf("[");
	bool first=true;
	for(i=0; i<strlen(mystr);++i)
	{
		if (mystr[i] !=' ')
		{
			if (first)
			{
				first = false; 
				printf("%c", mystr[i]);
			}
			else
			{
				printf(", %c", mystr[i]);
			}
		}
	}
	printf("]");

}

void init()
{
	combo[0] = 0; 
	oppose[0] = 0;
	mystr[0] = 0;
}

int main()
{

	int ntc; 
	scanf("%d", &ntc);
	int C, D, N; 


	for(int tci = 1; tci <= ntc; ++tci)
	{
		init();
		scanf("%d", &C);
		if (C > 0)
			scanf("%s", combo);
		scanf("%d", &D);
		if (D > 0)
			scanf("%s", oppose);
		scanf("%d", &N);
		scanf("%s", mystr);
		printf("Case #%d: ", tci);
		solve(mystr);
		printf("\n");
	}
	return 0;
}