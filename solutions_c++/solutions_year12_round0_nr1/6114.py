/*
 * PbA.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: sanjeev
 */

#include <cstring>
#include <stdio.h>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int t;
	char input_s[200];
	char hash_val[] = "yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d", &t);
	cin.getline(input_s,105);

	for (int i = 1; i <= t; i++)
	{
		cin.getline(input_s,105);
//		scanf("%[^\n]s", input_s);
		int len = strlen(input_s);
		printf("Case #%d: ", i);
		for (int i = 0; i < len; i++)
		{
			if (input_s[i] == ' ')
				printf("%c", input_s[i]);
			else
				printf("%c", hash_val[input_s[i] - 'a']);
		}
		printf("\n");
	}
	return 0;
}

