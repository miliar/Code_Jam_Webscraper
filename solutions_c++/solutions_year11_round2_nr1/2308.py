#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
#include<iomanip>

using namespace std;

void get_file();
void readt();
void readn();
void readLine();
void getWP();
void getOWP();
void OWP();
void OOWP();


char arr[500000];

long int tk=0,tnum,pos=0,x=0,k=0,n=0,t=0,num,totalTime,button_c[100],button_p[100],line,table[100][100],rpos=0,cpos=0;
float wp[100],Xowp[100],owp[100][100],oowp[100];
//long int wp[100],Xowp[100],owp[100][100],oowp[100];
void main()
{
	get_file();
	readt();
	for (int ii=0;ii<t;ii++)
	{
		readn();
		rpos=0;
		cpos=0;
		cout <<  setprecision (9);
		for(int jj=0;jj<n;jj++)
		{
			cpos=0;
			readLine();
			getWP();
			getOWP();
			rpos++;
		}
		OWP();
		OOWP();
		ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << ii+1 << "\n";
		for(int jj =0;jj<n;jj++)
		{
			//cout << "\nWP = " << wp[jj] << " OWP = " << Xowp[jj] << " OOWP = " << oowp[jj] << "\n";
			fout <<  setprecision (8) << (0.25*wp[jj]) +( 0.50 * Xowp[jj]) + (0.25* oowp[jj]) <<"\n";
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
void readn()
{
	n=0;
	pos++;
	while (arr[pos] != '\n')
	{
		n = (n*10) + ( arr[pos] - 48 );
		pos++;
	}
}

void readLine()
{
	pos++;
	while(arr[pos] != '\n' && arr[pos] != '\0')
	{
		if(arr[pos] == '.')
		{table[rpos][cpos] = -1;}
		else
			table[rpos][cpos] = arr[pos] -48;
		cpos++;
		pos++;
	}
	
	
}

void getWP()
{
	float tot=0;
	double win=0;
	for(int ii =0;ii<n;ii++)
	{
		if(table[rpos][ii] == -1)
			continue;
		if(table[rpos][ii] == ('1' - 48))
			win++;
		tot++;
	}
	wp[rpos] = (double)((double)(win)/(double)(tot));
	
}

void getOWP()
{
	for(int ii =0; ii <n; ii++)
	{
		if(table[rpos][ii] == -1)
		{table[rpos][ii] = -1;owp[rpos][ii] = -1;continue;}
		int tot=0;
		int win=0;
		for(int jj = 0;jj < n; jj++)
		{
			if(ii == jj)
				continue;
			if(table[rpos][jj] == -1)
				continue;
			if(table[rpos][jj] == 1)
				win++;
			tot++;
		}
		if(tot!=0)
			owp[rpos][ii] = (double)((double)(win)/(double)tot);
		if(tot==0)
			owp[rpos][ii] = -1;
	}
}

void OWP()
{
	for(int ii=0;ii<n;ii++)
	{
		int tot=0;
		double win=0;
		for(int jj =0;jj<n;jj++)
		{
			if(ii==jj)
				continue;
			if(owp[jj][ii] == -1)
				continue;
			win = win + owp[jj][ii];
			tot++;
		}
		Xowp[ii] = win/tot;
	
	}
	
}

void OOWP()
{
	for(int ii=0;ii<n;ii++)
	{
		float tot=0;
		float win=0;
		for(int jj=0;jj<n;jj++)
		{
			if(ii==jj)
				continue;
			if(table[ii][jj] == -1)
				continue;
			win = win + Xowp[jj];
			tot++;
		}
		oowp[ii] = win/tot;
	}
}