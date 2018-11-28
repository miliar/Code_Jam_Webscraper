#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cctype>

using namespace std;

int main()
{
	FILE *f = fopen("in.txt","r");
	int tests;
	fscanf(f,"%d",&tests);
	for(int test=1; test<=tests; test++) {
		long long number;
		char new_number[100] = {0,};
		new_number[0] = '0';
		fscanf(f, "%s", new_number+1);
		int len = strlen(new_number);
		next_permutation(new_number, new_number+len);
		printf("Case #%d: %s\n", test, (new_number[0] == '0' ? new_number+1 : new_number));
	}
	fclose(f);
	return 0;
}
