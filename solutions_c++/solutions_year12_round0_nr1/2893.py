#include<iostream>
#include<fstream>
#include<map>
#include<stdio.h>
#include<string.h>
#include<cstring>
using namespace std;
char st[105];
map<char,char> m;
FILE *fin = fopen("A-small-attempt0.in","r");
FILE *fout = fopen("out.txt","w");
void init()
{
	m['a'] = 'y'; m['b'] = 'h'; m['c'] = 'e'; m['d']='s';
	m['e'] = 'o'; m['f'] = 'c'; m['g'] = 'v'; m['h']='x';
	m['i'] = 'd'; m['j'] = 'u'; m['k'] = 'i'; m['l'] ='g';
	m['m'] ='l'; m['n']= 'b'; m['o'] ='k'; m['p'] ='r';
	m['q'] ='z'; m['r'] ='t'; m['s'] ='n'; m['t'] ='w';
	m['u']='j'; m['v'] = 'p'; m['w']='f'; m['x']='m';
	m['y']='a'; m['z']='q';
}
int main()
{
	int  ca; fscanf(fin,"%d",&ca);int k =0;
	init();
	char ch; fscanf(fin,"%c",&ch);
	while(ca--){
	fgets(st,105,fin);
	int i; int len = strlen(st)-1;
	fprintf(fout,"Case #%d: ",++k);
	for(i=0;i<len;++i)
		if(st[i]!=' ')
		fprintf(fout,"%c",m[st[i]]);
		else fprintf(fout," ");
	fprintf(fout,"\n");
	}
	return 0;
}