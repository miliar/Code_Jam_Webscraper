#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
//ejp mysljylc kd kxveddknmc re jsicpdrysi
//our language is impossible to understand
//
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//there are twenty six factorial possibilities
//
//de kr kd eoya kw aej tysr re ujdr lkgc jv
//so it is okay if you want to just give up
// 
//
//! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !  
//a b c d e f g h i j k l m n o p q r s t u v w x y z
//

char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
//	'a','b','c','d','e','f','g','h','i','j',
//	'k','l','m','n','o','p','q','r','s','t',
//	'u','v','w','x','y','z'

void solve(int probid)
{
	char input[128] = {0,};
	gets(input);
	int length = strlen(input);
	for(int i = 0; i<length; i++)
		if(input[i]>='a' && input[i] <= 'z')
			input[i] = mapping[input[i]-'a'];
	printf("Case #%d: %s\n", probid, input);
}

int main()
{
	int numb = 0;
	char numbs[10] = {0,};
	gets(numbs);
	numb = atoi(numbs);
	for(int i = 0; i<numb; i++)
		solve(i+1);
	return 0;
}