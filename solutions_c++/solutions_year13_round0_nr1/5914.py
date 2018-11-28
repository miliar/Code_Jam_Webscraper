#include <cstdio>
#include <string>
#include <iostream>

#define MAX 4

using namespace std;

int t; // t- number of tests

string solve(char s[MAX][MAX])
{
	string res="";
	char prev;
	int x, count, dots=0;
	for(int i = 0; i < MAX; i++)
		for(int j = 0; j < MAX; j++)
			if(s[i][j]=='.')
				dots++;
	
	for(int i = 0; i < MAX; i++)
	{
		prev=s[i][0];
		x=0;
		count=1;
		
		if(prev=='T')
		{
			prev=s[i][1];
			x++;
			count++;
		}
		
		for(int j = x+1; j < MAX; j++)
		{
			if(prev==s[i][j] || s[i][j]=='T')
				count++;
		}

		res=prev;
		if(count == 4 && prev!='.')
			return res+" won";
	}
	///////////////////////////////////////
	for(int i = 0; i < MAX; i++)
	{
		prev=s[0][i];
		x=0;
		count=1;
		
		if(prev=='T')
		{
			prev=s[1][i];
			x++;
			count++;
		}
		
		for(int j = x+1; j < MAX; j++)
		{
			if(prev==s[j][i] || s[j][i]=='T')
				count++;
		}

		res=prev;
		if(count == 4 && prev!='.')
			return res+" won";
	}
	///////////////////////////////////////
	prev=s[0][0];
	x=0;
	count = 1;
	
	if(prev=='T')
	{
		prev=s[1][1];
		x++;
		count++;
	}
	
	for(int i = 1+x; i < MAX; i++)
	{
		if(prev==s[i][i] || s[i][i]=='T')
			count++;
	}
	
	res=prev;
	if(count == 4 && prev!='.')
		return res+" won";
 	///////////////////////////////////////
	prev=s[0][3];
	x=0;
	count = 1;
	
	if(prev=='T')
	{
		prev=s[1][2];
		x++;
		count++;
	}
	
	for(int i = 2-x; i >= 0; i--)
	{
		if(prev==s[3-i][i] || s[3-i][i]=='T')
			count++;
	}
	
	res=prev;
	if(count == 4 && prev!='.')
		return res+" won";
	///////////////////////////////////////
	return dots>0 ? "Game has not completed" : "Draw";
}
int main()
{
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		char s[MAX][MAX];
		for(int j = 0; j < MAX; j++)
			scanf("%s", s[j]);
		cout << "Case #" << i << ": " << solve(s) << endl;
	}

	
	return 0;
}