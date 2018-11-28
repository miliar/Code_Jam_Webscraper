// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
using namespace std;

const string code = "welcome to code jam";
char str[500];

int N,cas = 1,len,sum,lens;
int hash[35];

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k;

	len = code.length();	
freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small.out","w",stdout);
	cin >> N;
	getchar();
	while(N --)
	{
		gets(str);
		lens = strlen(str);
		memset(hash,0,sizeof(hash));
		for (i = 0; i < lens; ++ i)
			if(str[i] == code[len - 1])
				hash[i] = 1;
		for (i = len - 2; i >= 0; -- i)
		{
			for (j = 0; j < lens; ++ j)
			{
				if(str[j] == code[i])
				{
					sum = 0;
					for (k = j + 1; k < lens; ++ k)
					{
						if (str[k] == code[i + 1])
							sum = (sum + hash[k]) % 10000;
					}
					hash[j] = sum;
				}
			}
		}
		sum = 0;
		for (i = 0; i < len; ++ i)
			if(str[i] == code[0])
				sum = (sum + hash[i]) % 10000;

		printf ("Case #%d: %04d\n",cas ++,sum % 10000);
		
	}
	return 0;
}

