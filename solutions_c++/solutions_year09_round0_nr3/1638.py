#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

string codejam = "welcome to code jam";
string s;
int res;

void func(int x, int sx)
{
	if(x==codejam.size()) { res+=1; return; }
	while(1)
	{
		int a = s.find_first_of(codejam[x], sx);
		if (a!=string::npos)
		{
			sx+=a-sx+1;
			func(x+1, sx);
//			cout << "> a = " << a << "\n";
		}
		else break;
	}
}

int wmain(void)
{
	FILE* fin = fopen("A-small.in", "r");
	FILE* fout = fopen("out", "w");
	int n;
	char c; 
	fscanf(fin, "%d", &n);
	fscanf(fin, "%c", &c);
	for(int i=0;i<n;++i)
	{
		s="";
		c=1;
		while(c!=0&&c!=10&&!feof(fin)){fscanf(fin, "%c", &c);s+=c;}
		cout << s;
		res=0;

		func(0, 0);

		fprintf(fout, "Case #%d: %04d\n", i+1, res%1000);
		printf("Case #%d: %04d\n", i+1, res%1000);
	}
	fclose(fin);fclose(fout);
	return 0;
}

