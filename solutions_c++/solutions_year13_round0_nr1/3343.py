#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;

char matrix[4][4];

bool check_row(char);
bool check_column(char);
bool check_diagonal(char);

int main()
{
	int t,i,j,k=0;
	
	string str;
	getline(cin,str);
	t = atoi(str.c_str());
	bool remaining;
	while(t--)
	{
		k++;
		remaining = false;
		for(i=0;i<4;i++)
		{
			getline(cin,str);
			for(j=0;j<4;j++)
			{
				matrix[i][j] = str[j];
				if(matrix[i][j] == '.')
					remaining = true;
			}
		}
		if(t)
			getline(cin,str);
		if(check_row('X') || check_column('X') || check_diagonal('X'))
			printf("Case #%d: X won\n",k);
		else if(check_row('O') || check_column('O') || check_diagonal('O'))
			printf("Case #%d: O won\n",k);
		else if(remaining)
			printf("Case #%d: Game has not completed\n",k);
		else
			printf("Case #%d: Draw\n",k);
	}
	return 0;
}

bool check_row(char ch)
{
	int i=0,j;
	bool flag=false;
	while(!flag && (i<4))
	{
		flag = true;
		for(j=0;j<4;j++)
		{	
			if((matrix[i][j]  != ch) && (matrix[i][j] != 'T'))
				flag = false;
		}
		i++;
	}
	return flag;
}

bool check_column(char ch)
{
	int i=0,j;
	bool flag=false;
	while(!flag && (i<4))
	{
		flag = true;
		for(j=0;j<4;j++)
		{	
			if((matrix[j][i]  != ch) && (matrix[j][i] != 'T'))
				flag = false;
		}
		i++;
	}
	return flag;
}

bool check_diagonal(char ch)
{
	int i,j;
	bool flag=false;
	flag = true;
	for(j=0;j<4;j++)
	{	
		if((matrix[j][j]  != ch) && (matrix[j][j] != 'T'))
			flag = false;
	}
	if(flag)
		return flag;
	flag = true;
	for(j=0;j<4;j++)
	{	
		if((matrix[j][3-j]  != ch) && (matrix[j][3-j] != 'T'))
			flag = false;
	}
	return flag;
}
