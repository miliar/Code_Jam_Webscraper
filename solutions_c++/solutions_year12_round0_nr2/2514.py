#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>

using namespace std;

char arr[50000];
unsigned long int pos=0,x=0,t,n,s,p;
int c[101],count;

void readFile();
long int get_int();
int calculate_max_p();

void main()
{
	int result;
	readFile();
	t = get_int();
	ofstream fout;
	for(int xx =0;xx<t;xx++)
	{
		count = 0;
		n = get_int();
		s = get_int();
		p = get_int();
		//cout << "\nN | S | P " << n << " | " << s  << " | " << p;
		for(int yy = 0;yy <n; yy++)
			c[count++] = get_int();
		//cout << "\n CASE : " << xx+1;
		result = calculate_max_p();
		//getch();
		fout.open("outputm.in",ios::app);
		fout << "Case #" << xx+1<<": " << result <<"\n";
		fout.close();
	}
}

void readFile()
{
	ifstream fin;
	fin.open("input.in", ios::in);
	while(fin)
	{
		fin.get(arr[x]);
		x++;
	}
	fin.close();
}

long int get_int()
{
	long int return_value=0;
	while(arr[pos] < '0' || arr[pos] > '9')
		pos++;
	while(arr[pos] >= '0' && arr[pos] <= '9')
		return_value = (return_value*10) + (arr[pos++]-'0');
	return return_value;
}

int calculate_max_p()
{
	int retValue = n,diff;
	
	for(int xx=0;xx<n;xx++)
	{
		diff = c[xx] - p;
		if(diff >= 0)
			c[xx] -= p;
		else
		{retValue--;continue;}
		
		c[xx] = c[xx] /2;
		if(c[xx] >=p)
			continue;
		if(p-c[xx] == 2)
		{
			if(s)
				s--;
			else
				retValue--;
		}
		else if(p-c[xx] >2)
			retValue--;
		
	}
	return retValue;
}