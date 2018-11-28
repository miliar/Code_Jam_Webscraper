#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>

#include <boost/regex.hpp>

using namespace std;

int numSubseq(int tab[][25],char *str, int , char *sub, int);
int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	cin >> nTests;
	char temp[1000];
	fgets(temp, 1000, stdin);
	assert(temp[0] == '\n');
	assert(temp[1] == '\0');

	char sub[]="welcome to code jam";
	for(testId=1;testId<=nTests;testId++)
	{
		int num;
		char str[1000];

		//XXX  -- Read input --  XXX
		//cin >> str;
		fgets(str, 1000, stdin);
		assert(str[strlen(str)-1]== '\n');
		str[strlen(str)-1]='\0';
		//cout << str << endl;

		int table[strlen(str)+50][25];
		memset((char*)&table, -1, sizeof(int)*(strlen(str)+10)*25);
		//XXX  -- Process input --  XXX
		int res=numSubseq(table,str,0,sub,0);

		//XXX  -- Print output --  XXX
		printf("Case #%d: %04d\n",testId, res);
	}

	return 0;
}

int numSubseq(int tab[][25],char *str, int a, char *sub, int b)
{
	if(tab[a][b]!=-1) return tab[a][b];

	//termination criteria
	if (sub[b]=='\0')
	{
		tab[a][b]=1;
		return tab[a][b];
	}
	else if(str[a]=='\0')
	{
		tab[a][b]=0;
		return tab[a][b];
	}

	int res=0;
	//stop when sub[b] is found in str[a] onwards
	for(;str[a]!='\0'; a++)
		if(sub[b]==str[a]) break;

	if (sub[b]==str[a])
	{
		res+=numSubseq(tab,str,a+1,sub,b+1);
		res%=10000;
		res+=numSubseq(tab,str,a+1,sub,b);
		res%=10000;
	}
	
	tab[a][b]=res;
	return res;
}
