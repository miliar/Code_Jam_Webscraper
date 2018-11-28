#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
#include<iomanip>
#include<algorithm>

#define SPEED 0.5
#define BSPEED 1

using namespace std;

void get_file();
void readt();
void readLTNC();
void reada();
void setDistances();
void getPosition();
bool sortAlgo (int i,int j) { return (i>j); }

char arr[500000];

unsigned long long int tk=0,tnum,pos=0,x=0,k=0,n=0,num,totalTime,button_c[100],button_p[100],line,table[100][100],r=0,c=0,t=0,TotalTime=0,l,cur_pos,travelled,defaultDistance=0;

float a[1000000],distances[1000000];

void main()
{
	get_file();
	readt();
	for (int ii=0;ii<tk;ii++)
	{
		readLTNC();
		
		reada();
		setDistances();
		
		if(defaultDistance*2 > t)
		{
		travelled = SPEED * t;
		TotalTime=t;
		getPosition();
		sort(distances, distances + n,sortAlgo);
		cur_pos=0;
		while(l >0)
		{
			TotalTime = TotalTime + distances[cur_pos];
			cur_pos++;
			l--;
		}
		for(int jj=cur_pos;jj<n;jj++)
			TotalTime = TotalTime + (2*distances[jj]);
		}
		else
			TotalTime = defaultDistance *2;
		//cout << "\nTotal Time = " << TotalTime;
		ofstream fout;
		fout.open("output.in" , ios :: app);
		fout << "Case #" << ii+1 << ": " << TotalTime << "\n";
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
		tk =  (tk*10) + (arr[pos] - 48);
		pos++;
	}
}

void readLTNC()
{
	//cout << "5";
	l=t=n=c=0;
	pos++;
	while (arr[pos] != ' ')
	{
		l =  (l*10) + (arr[pos] - 48);
		pos++;
	}
	pos++;
	while (arr[pos] != ' ')
	{
		t =  (t*10) + (arr[pos] - 48);
		pos++;
	}
	pos++;
	while (arr[pos] != ' ')
	{
		n =  (n*10) + (arr[pos] - 48);
		pos++;
	}
	pos++;
	while (arr[pos] != ' ')
	{
		c =  (c*10) + (arr[pos] - 48);
		pos++;
	}
}

void reada()
{
	//cout << "3";
	pos++;
	for(int ii =0; ii<c;ii++)
	{
		a[ii]=0;
		while (arr[pos] != ' ' && arr[pos] != '\n' && arr[pos] != '\0')
		{
			a[ii] =  (a[ii]*10) + (arr[pos] - 48);
			pos++;
		}
		pos++;
	}
	pos--;
}

void setDistances()
{
	defaultDistance=0;
	//cout << "2";
	int count =0;
	for(int ii = 0;ii<n;ii++)
	{
		distances[ii] = a[count];
		defaultDistance += distances[ii];
		count++;
		if(count == c)
			count = 0;
	}
}

void getPosition()
{
	//cout << "1";
	cur_pos=0;
	while(travelled-distances[cur_pos] >=0)
	{
		travelled = travelled - distances[cur_pos];
		distances[cur_pos] = 0;
		cur_pos++;
	}
	distances[cur_pos] = distances[cur_pos] - travelled;
}