#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
#include<iomanip>

using namespace std;

void get_file();
void readt();
void readRC();
void readPaint();
void replaceRed();
bool checkBlueLeft();


char arr[500000];
char paint[55][55];
long int tk=0,tnum,pos=0,x=0,k=0,n=0,t=0,num,totalTime,button_c[100],button_p[100],line,table[100][100],r=0,c=0,blue=0;


void main()
{
	get_file();
	readt();
	for (int ii=0;ii<t;ii++)
	{
		readRC();
		readPaint();
		if(blue%4 != 0)
		{
			ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << ii+1 << ":\n";
			fout << "Impossible\n";
			fout.close();
			continue;
		}
		replaceRed();
		
		if(checkBlueLeft() == true)
		{
			ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << ii+1 << ":\n";
			fout << "Impossible\n";
			fout.close();
			continue;
		}
		ofstream fout;
		fout.open("output.in" , ios :: app);
		fout << "Case #" << ii+1 << ":\n";
		for(int kk =0;kk<r;kk++)
		{
			for(int jj =0;jj<c;jj++)
				fout << paint[kk][jj];
			fout << "\n";
		}
		fout.close();

	}
	
}


void get_file()
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

void readRC()
{
	r=0;
	c=0;
	pos++;
	while (arr[pos]!= ' ')
	{
		r =  (r*10) + (arr[pos] - 48);
		pos++;
	}
	
	pos++;
	while (arr[pos]!= '\n')
	{
		c =  (c*10) + (arr[pos] - 48);
		pos++;
	}
	
}

void readPaint()
{
	blue=0;
	pos++;
	for(int ii =0;ii<r;ii++)
	{
		for(int jj =0;jj<c;jj++)
		{
			paint[ii][jj] = arr[pos];
			if(paint[ii][jj] == '#')
				blue++;
			pos++;
		}
		pos++;
	}
	pos--;
}

void replaceRed()
{
	for(int ii =0;ii<r-1;ii++)
	{
		for(int jj =0;jj<c-1;jj++)
		{
			if(paint[ii][jj]== '#' && paint[ii][jj+1] == '#' && paint[ii+1][jj]== '#' && paint[ii+1][jj+1] == '#')
			{
				paint[ii][jj]= '/';
				paint[ii][jj+1] = '\\';
				paint[ii+1][jj]= '\\';
				paint[ii+1][jj+1] = '/';
				jj++;
			}
			
		}
	}
}

bool checkBlueLeft()
{
	for(int ii =0;ii<r;ii++)
		for(int jj =0;jj<c;jj++)
			if(paint[ii][jj] == '#')
				return true;
	return false;
}
