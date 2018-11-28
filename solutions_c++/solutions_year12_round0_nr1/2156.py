/*
 * main.cpp
 *
 *  Created on: 14.04.2012
 *      Author: kalhit
 */
#include <stdio.h>
#include <stdlib.h>
char s[200];
char mas[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	gets(s);
	int T = atoi(s);
	for(int j = 0; j < T; ++j)
	{
		if(j)
			printf("\n");
		gets(s);
		for(int i = 0; s[i]; ++i)
		{
			if(s[i]>='a' &&s[i] <= 'z')
				s[i] = mas[(int)s[i]-'a'];
		}
		printf("Case #%d: %s", 1+j, s);
	}

	return 0;
}
