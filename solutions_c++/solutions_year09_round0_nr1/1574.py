#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int wmain(void)
{
	FILE* fin = fopen("A-small.in", "r");
	int l,d,n;
	fscanf(fin, "%d%d%d", &l, &d, &n);
	FILE* fout = fopen("out", "w");
	string w(l,' ');
	string words[5000];
	for(int i=0;i<d;++i) { 
		fscanf(fin, "%s", &w);
	words[i].assign(w); }
//	for(int i=0;i<d;++i) cout << words[i] << "\n";

	for(int i=0;i<n;++i)
	{
		char c=' ';
		
		string subs[15];
		fscanf(fin, "%c", &c);
		for(int j=0;j<l;++j)
		{
			subs[j]="";
			fscanf(fin, "%c", &c);
			if(c!='(') subs[j]+=c;
			else
			{
				while(c!=')') {fscanf(fin, "%c", &c);subs[j]+=c;}
			}
		}
		int res=0;
		for(int j=0;j<d;++j)
		{
			int fl=1;
			for(int k=0;k<l;++k)
				if (subs[k].find(words[j][k])==string::npos) {fl=0;break;}
			res+=fl;
		}
		fprintf(fout, "Case #%d: %d\n", i+1, res);
		printf("Case #%d: %d\n", i+1, res);
	}
	fclose(fin);fclose(fout);
	return 0;
}
