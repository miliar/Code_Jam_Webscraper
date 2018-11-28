// IMPORTANT :: The Input File should be in the same folder as the .exe file and with the name "input.in"

#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <fstream>
#include <math.h>
using namespace std;
void read();
void readt();
void readn();
void readk();
char arr[90000000];
unsigned long int tk=0,tnum,pos=0,x=0,k=0,n=0,t=0,num;;

void main()
{
	read();
	readt();
	for (unsigned long int xx=0;xx<t;xx++)
	{
		num=2;
		readn();
		readk();
		for(unsigned long int yy =0;yy <n-1;yy++)
		{
			num= num *2;
		}
		//cout << "k = " << k << " num = " << num << " and k % num = " << k%num;
		if ( k % num == num - 1)
		{
			ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << xx+1 << ": " << "ON\n";
			fout.close();
		}
		else
		{
			ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << xx+1 << ": " << "OFF\n";
			fout.close();
		}
		//cout <<"\n";
		//getch();
	}
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
void readn()
{
	n=0;
	pos++;
	while (arr[pos] != ' ')
	{
		n = (n*10) + ( arr[pos] - 48 );
		pos++;
	}
}
void readk()
{
	k=0;
	pos++;
	while ((arr[pos] != '\n')&& (arr[pos] != '\0'))
	{
		k = (k*10) + ( arr[pos] - 48 );
		pos++;
	}
}