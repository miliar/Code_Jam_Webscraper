#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

char dic[36];

char getdic(char inc)
{
	int index;
	if (islower(inc))
		index = inc - 'a' + 10;
	else
		index = inc - '0';

	return dic[index];
}

void setdic(char inc, char key)
{
	int index;
	if (islower(inc))
		index = inc - 'a' + 10;
	else
		index = inc - '0';

	dic[index] = key;
}

int main(int argc, char* argv[])
{
	FILE* is = freopen(argv[1], "r", stdin);
	FILE* os = freopen(argv[2], "w", stdout);

	int t;

	scanf("%d", &t);
	

	for (int i = 1; i<=t; i++)
	{
		memset(dic, -1, sizeof(dic));
		char oristr[62];
		memset(oristr, 0, sizeof(oristr));
		scanf("%s", oristr);
		
		int base = 2;
		int currbit = 0;

		setdic(oristr[0],'1');

		for (int k = 1; k <strlen(oristr); k++)
		{
			if (getdic(oristr[k]) == -1)
			{
				setdic(oristr[k],currbit+'0');
				if (currbit == 0) currbit = 2;
				else currbit ++;
				
			}
		}
		
		if (currbit > 0) base = currbit;
		
		char ansstr[62];
		memset(ansstr, 0, sizeof(ansstr));
		for (int m = 0; m < strlen(oristr); m++)
		{
			ansstr[m]=getdic(oristr[m]);
		}

		__int64 ans = 0;
		for (m = 0; m<strlen(ansstr)-1;m++)
		{
			ans = (ans + (ansstr[m]-'0')) * base;
		}
		ans += ansstr[m]-'0';
		printf("Case #%d: %I64d\n", i, ans);
		
	}


	fclose(is);
	fclose(os);
	return 0;
}