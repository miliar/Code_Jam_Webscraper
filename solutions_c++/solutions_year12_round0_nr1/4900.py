#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main()
{
	char a[100] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char b[100] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char c[100] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char e[100] = "our language is impossible to understand";
	char f[100] = "there are twenty six factorial possibilities";
	char g[100] = "so it is okay if you want to just give up";

	char m[5000];

	m[0] = 'y';
	m[25] = 'q';
	m['q'-'a']='z';
	for (int i = 0; i < strlen(a); i++)
	{
		if (a[i] != ' ')
		m[a[i]-'a'] = e[i];
	}	
	for (int i = 0; i < strlen(b); i++)
		if (b[i] != ' ')
		m[b[i]-'a'] = f[i];
	
	for (int i = 0; i < strlen(c); i++)
		if (c[i] != ' ')
		m[c[i]-'a'] = g[i];
	
		//	cout << (char)('a' + i) << ' ' << m[i] << endl;
	FILE *in = fopen("C:\\Users\\acer\\Desktop\\A-small-attempt8.in", "r");
	FILE *out = fopen("C:\\Users\\acer\\Desktop\\A-small-attempt0.out", "w");
	//in = stdin;
	//out = stdout;
	int n;
	fscanf(in, "%d", &n);
fgetc(in);
	for (int k = 1; k <= n; k++)
	{
		char x[200];
		fgets(x, 150, in);
		int len = strlen(x)-1;
		
			x[len] = 0;
			cout << x << endl;
	
		//cout << len << endl;
		//cout << (int)x[18] << endl; 
		for (int i = 0; i < len; i++)
			if (x[i] != ' ')
			{
			//	cout << x[i];
				x[i] = m[x[i]-'a'];
			}
		x[len] = 0;
		//for (int i = 0; i < len; i++)
		//	cout << x[i];\
		//x[1]='a';
		//cout << strlen(x) << endl;
		cout << x << endl;
		//cout << (int)x[18] << endl;
		fprintf(out, "Case #%d: %s\n", k, x);
	}
}
