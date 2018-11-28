#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

char m[10][10];

bool check (char c,bool p)
{
	int i,j;

	for (i=0;i<4;i++)
	{
		bool f = true;
		for (j=0;j<4;j++)
			if ((m[i][j]!=c&&m[i][j]!='T'&&m[i][j]!='.')||(!p&&m[i][j]=='.'))
			{
				f = false;
				break;
			}
		if (f)
			return f;
		f = true;
		for (j=0;j<4;j++)
			if ((m[j][i]!=c&&m[j][i]!='T'&&m[j][i]!='.')||(!p&&m[j][i]=='.'))
			{
				f = false;
				break;
			}
		if (f)
			return f;
	}

	bool f = true;
	for (i=0;i<4;i++)
		if ((m[i][i]!=c&&m[i][i]!='T'&&m[i][i]!='.')||(!p&&m[i][i]=='.'))
		{
			f = false;
			break;
		}
	if (f)
		return f;
	f = true;
	for (i=0;i<4;i++)
		if ((m[i][3-i]!=c&&m[i][3-i]!='T'&&m[i][3-i]!='.')||(!p&&m[i][3-i]=='.'))
		{
			f = false;
			break;
		}

	return f;
}

int main ()
{
	freopen ("A.in","r",stdin);
	freopen ("A.out","w",stdout);
	
	int t,o=1;
	scanf ("%d",&t);

	while (t--)
	{
		int i,j;


		for (i=0;i<4;i++)
			scanf ("%s",m[i]);/*
		for (i=0;i<4;i++)
			printf ("              %s\n",m[i]);*/

		printf ("Case #%d: ",o++);

		bool f1 = check ('X',0);
		bool f2 = check ('O',0);
		bool f3 = false;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				if (m[i][j]=='.')
					f3 = true;
		if (f1)
			printf ("X won\n");
		else if (f2)
			printf ("O won\n");
		else if (f3)
			printf ("Game has not completed\n");
		else
			printf ("Draw\n");
		/*else
		{
			bool f1 = check ('X',1);
			bool f2 = check ('O',1);
			
			if (f1||f2)
				printf ("Game has not completed\n");
			else
				printf ("Draw\n");
		}*/

		if (t)
			scanf ("\n");
	}

	return 0;
}
