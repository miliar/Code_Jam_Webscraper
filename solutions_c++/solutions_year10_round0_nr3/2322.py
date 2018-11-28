// IMPORTANT :: The Input File should be in the same folder as the .exe file and with the name "input.in"
// Coded in Visual C++

#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <fstream>
#include <math.h>
using namespace std;
void read();
void readt();
void readr();
void readk();
void readn();
void readgrp();
void defgrp();
char arr[90000000];
unsigned long int pos=0,x=0,k=0,n=0,r=0,grp[10000000],run,sit,gr,cost,t=0,flag=0,countr;
void main()
{
	ofstream fout;
	fout.open("output.in",ios :: out);
	read();
	readt();
	for (unsigned long int xx =0; xx < t; xx++)
	{
		readr();
		readk();
		readn();
		defgrp();
		readgrp();
		run=0;
		gr=0;
		cost = 0;
		flag=0;
		while (run != r)
		{
			sit=0;
			flag=0;
			countr=0;
			//cout << "K = " << k << "\n";
			while(sit <= k)
			{
				if (countr == n)
				{flag=1;goto label;}
				if(gr==n)
				{gr=0;}
				sit = sit + grp[gr];
				gr++;
				countr++;
				//cout<<"Sit = " << sit<< " Count = " << countr << " Group = " << gr <<"\n";
			}
			gr--;
			cost = cost + sit - grp[gr];
label:
			;
			if (gr==n)
			{
				gr=0;
			}
			if(flag==1)
			{
				cost = cost + sit;
			}
			run++;
			//cout << "\n";
			//getch();
		}
		
		fout << "Case #" << xx +1 << ": " << cost << "\n";
		
				
	}
	fout.close();
	getch();
}
void read()
{
	ifstream fin;
	fin.open("input.in" , ios :: in);
	while(fin)
	{
		fin.get(arr[x]);
		x++;
	}
	fin.close();
}
void readt()
{
	while (arr[pos] != '\n')
	{
		t =  (t*10) + (arr[pos] - 48);
		pos++;
	}
}
void readr()
{
	r=0;
	pos++;
	while(arr[pos] != ' ')
	{
		r = (r * 10) + (arr[pos] - 48);
		pos++;
	}
}
void readk()
{
	k=0;
	pos++;
	while (arr[pos] != ' ')
	{
		k = (k*10) + (arr[pos] - 48);
		pos++;
	}
}
void readn()
{
	n=0;
	pos++;
	while ((arr[pos] != '\n')&&(arr[pos] != '\0'))
	{
		n = (n*10) + (arr[pos] - 48);
		pos++;
	}
}
void defgrp()
{
	for (unsigned long int xx =0;xx<n;xx++)
	{
		grp[xx]=0;
	}
}
void readgrp()
{
	pos++;
	for (unsigned long int xx =0; xx <n;xx ++)
	{
		while((arr[pos] != ' ') && (arr[pos] != '\n') && (arr[pos] != '\0'))
		{
			grp[xx] = ( grp[xx] * 10) + (arr[pos] - 48);
			pos++;
		}
		pos++;
	}
	pos--;
}