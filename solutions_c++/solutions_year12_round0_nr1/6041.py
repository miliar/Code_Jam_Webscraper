// vcp.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <queue>
#include <string>
using std::map;
using std::pair;
using std::set;
using std::string;
using std::queue;
const unsigned int modn = 1000000007;
int T,N,M,S;

char* s0 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char* s1 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";


int main(void)
{
	char buf[1024];
	char map[27];

	for(int i= 0 ; s0[i];i++)
	{
		map[s0[i] - 'a'] = s1[i];	
	}
	map[0] = 'y';
	//map['o'-'a'] = 'e';
	map['z'-'a'] = 'q';
	map['q'-'a'] = 'z';

	map[26]=0;
	//printf("%s\n",map);

	freopen( "input00.txt", "r", stdin );
    freopen( "outputt.txt", "w", stdout );

	scanf( "%d\n", &T);
	for(int t= 0 ; t < T; t++)
	{
		printf("Case #%d: ",t+1);
		gets( buf);
		for(int i = 0 ; buf[i];  i++)
		{
			printf("%c",map[buf[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
/*
3
0
1
0
4
0
6
0
1
4
5
1
2
1
1
0
4
1
1
6
*/