// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

const int MAX = 1000000;

int f[MAX+10];

bool isWin(int a, int b)
{
	if (a>b){
		int t= a; a=b; b=t;
	}
	if (a==0)
		return true;
	else
	if (a==1)
		return (b!=1);
	else
	if (b>f[a]) return true; else return false;
}

bool check(int a, int b)
{
	b = b-a;
	return !isWin(b, a);
}

void prepare()
{
	int i, test;

	f[2] = 3;
	for (i=3; i<=MAX; i++){
		test = f[i-1]+2;
		if (test>MAX)
			f[i] = MAX;
		else
		{
			if (!check(i, test))
				f[i] = test;
			else
				f[i] = test-1;
		}
		
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w", stdout);
	prepare();
	int t, i=0;
	int j, k, tot, a1, a2, b1, b2;
	scanf("%d", &t);
	while (t--){
		printf("Case #%d: ", (++i));
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		tot = 0;
		for (k=a1; k<=a2; k++)
			for (j=b1; j<=b2;j++)
				if (isWin(k, j)) tot++;
		printf("%d\n", tot);
	}
	return 0;
}
