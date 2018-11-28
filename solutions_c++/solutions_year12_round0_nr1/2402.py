#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<string>
#include<fstream>

using namespace std;

char arr[10000],inpt[101],out_p[101];

long long x=0,t=0,pos=0,len=0;
short int map[26]={-1},count=1;

void readFile();
void read_t();
void read_string();
void map_string();
void main()
{
	
	char str1[3][100]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"},str2[3][100]={"our language is impossible to understand","there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	for(int yy=0;yy<3;yy++)
	{
		for(int xx = 0; xx<strlen(str1[yy]);xx++)
		{
			if(str1[yy][xx] == ' ')
				continue;
			map[str1[yy][xx] - 'a'] = str2[yy][xx];
		}
	}
	map['z'-'a'] = 'q';
	map['q'-'a'] = 'z';
	
	for(int mn =0;mn<26;mn++)
		cout << char(mn + 'a') << " = " << char(map[mn]) << "\n";

	readFile();
	read_t();
	cout << "T="<<t <<"\n";

	while(t--)
	{
		read_string();
		map_string();
		//puts(inpt);
		//puts(out_p);
		//getch();
		ofstream fout;
		fout.open("output.in",ios::app);
		fout << "Case #" << count << ": "<< out_p <<"\n";
		fout.close();
		count++;
	}
}

void readFile()
{
	ifstream fin;
	fin.open("input.in", ios::in);
	while(fin)
	{
		fin.get(arr[x]);
		//cout << arr[x];
		x++;
	}
	fin.close();
}

void read_t()
{
	while(arr[pos] != '\n')
	{
		t=(t*10) + (arr[pos] - '0');
		pos++;
	}
}

void read_string()
{
	len=0;
	if(arr[pos] == '\n')
		pos++;
	while(arr[pos] != '\n' && arr[pos] != '\0' && pos != x)
		inpt[len++] = arr[pos++];
	inpt[len++] = '\0';
}

void map_string()
{
	for(int xx=0;xx<strlen(inpt);xx++)
	{
		if(inpt[xx] == ' ')
		{out_p[xx] = ' ';continue;}
		out_p[xx] = map[inpt[xx] - 'a'];
	}
	out_p[strlen(inpt)] = '\0';
}