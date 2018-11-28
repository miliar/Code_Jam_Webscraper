//============================================================================
// Name        : gcj-1.cpp
// Author      : Thomas 'nickers' Wsuł
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int cmp(const char* a, const char* b) {
	return (*a-*b);
}

char* mk(char* n) {
	int l = strlen(n)-1;
	int ll = l + 1;

	while (l>0) {
		if (n[l]>n[l-1]) {

			//if (n[l]=='0')
			{
			int p = l-1;
			char x = n[p];

			qsort(&n[l-1], ll-l+1, sizeof(n[0]), (int(*)(const void*, const void*))cmp);

			//printf("sord: %s[%d]\n", &n[l-1], ll-l+1);
			while (n[p]<=x) p++;
			x = n[p];

			for (int i=0; i<l-1; i++) printf("%c", n[i]);
			printf("%c", x);
			//printf("<<<");
			for (int i=l-1; i<p; i++){
				printf("%c", n[i]);
			}
			printf("%s\n", &n[p+1]);
			return NULL;
/**
			printf("%s", n);
			printf("[%c]", x);
			puts(&n[l+1]);

			/*char a = n[p];
			n[p]=n[l-1];
			n[l-1]=a;*/
			}
			/*else {
				char x = n[l];
				qsort(&n[l], ll-l, sizeof(n[0]), (int(*)(const void*, const void*))cmp);
				char a = n[l];
				n[l]=n[l-1];
				n[l-1]=a;
				if (ll-l-1>0)
			}*/
			//puts(n);
			return n;
		}
		l--;
	}

	qsort(n, ll, sizeof(n[0]), (int(*)(const void*, const void*))cmp);
	//puts(n);

	int i=0;
	while (n[i]=='0') i++;

	printf("%c0", n[i]);
	n[i] = 0;
	printf("%s", n);
	puts(&n[i+1]);

	return n;
}


int main()
{
	int T;
	char n[10];

	scanf("%d", &T);

	for (int i=1; i<=T; i++) {
		scanf("%s", n);
		printf("Case #%d: ", i);
		mk(n);
	}

	return 0;
}
