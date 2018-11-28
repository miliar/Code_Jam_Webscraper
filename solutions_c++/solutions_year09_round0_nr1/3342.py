
#include <string>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;


int nletters, nwords, ntestcases;
char words[25][10];
char testCases[10][251];
int flag[120];
int static counter=0;

bool check ( char s[] )
{
	if ( strlen(s) == 0 )
		return false;

	int len = strlen(s);
	for ( int i = 0 ; i <nwords; i++ )
	{
		if ( strncmp( s, words[i] , len) == 0 )
			return true;
	}
	return false;

}
void match( char str[] )
{
	if ( strlen(str) == 0 )
	{
		return;
	}

	for ( int i=0; i < nwords; i++)
	{
		if (  strncmp(str,words[i],nletters) == 0 )
		{
			counter++;
			break;
		}
	}
}

void func ( char *next, char prev[] ="-1"  )
{
	if ( strlen(next) == 0 )
	{
		if ( prev == "-1" )
			return;
		match(prev);
		return;

	}


	if (prev == "-1" )
		prev = "";


	char prev1[250];
	strcpy(prev1,prev);

	int openbracket=0, closebracket=0;

	for ( int i=0; i < strlen(next); i++ )
	{
		if ( next[i] == '(' )
			openbracket=i;

		if ( next[i] == ')' )
		{
			closebracket=i;
			break;
		}
	}

	if ( openbracket == 0 && closebracket == 0 )
	{
		char *a = strcat(prev1, next);
		match(a);
		return;
	}

	strncat(prev1, next, openbracket);

	for ( int i=0; i < (closebracket-openbracket-1); i++ )
	{
		char prev2[250];
		strcpy(prev2, prev1);

		const char *a = &next[openbracket+i+1];
		strncat ( prev2, a , 1);

		if ( check(prev2) )
			func(&next[closebracket+1],prev2);
	}

}

int main () 
{
	freopen("A-small.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);

	scanf( "%d %d %d" , &nletters, &nwords, &ntestcases );
	gets(words[0]);

	for ( int i =0 ; i < nwords ; i++ ) 
		gets(words[i]);

	for ( int i=0; i < ntestcases; i++)
		gets(testCases[i]);

	for ( int i=0 ; i<ntestcases ; i++ )
	{
		char *p = &testCases[i][0];
		func( p );
		cout << "Case #" << i+1 << ": " << counter << endl;
		counter = 0;
	}



	return 0;
}