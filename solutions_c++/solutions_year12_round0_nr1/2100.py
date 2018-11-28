//============================================================================
// Name        : GoogleQualification-A.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

char math[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

bool test_char(char ch);

int main() {
	int testcase = 0;
	char char_test[10];
	char googlerese[150];

	gets(char_test);
	for(int i = 0; char_test[i]; i++)
		testcase = (testcase * 10) + (char_test[i] - '0');

	for(int i = 0; i < testcase; i++)
	{
		gets(googlerese);
		for(int j = 0; googlerese[j]; j++)
			if(test_char(googlerese[j]))
				googlerese[j] = math[googlerese[j] - 'a'];

		cout << "Case #" << i + 1 << ": " << googlerese << "\n";
	}

	return 0;
}

bool test_char(char ch)
{
	if((ch >= 'a') && (ch <= 'z'))
		return true;
	else
		return false;
}
