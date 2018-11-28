// 2013.4.13-google code jam-A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
using namespace std;
#include<fstream>

int _tmain(int argc, _TCHAR* argv[])
{ 
	char str[4][4];
	const char t='T',x='X',o='O',d='.';
	int i,j,m,T,z1,z2,z3,z4;
	bool tt;
	int hen(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile),shu(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile),pie(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile),na(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile);
	ifstream infile;
	ofstream outfile;
	infile.open("problem_1i.dat",ios::in);
	outfile.open("problem_1o.dat",ios::out | ios::app);
	if(!outfile||!infile)
	{
		cerr<<"open error!"<<endl;
	}
	infile>>T;
	m=0;
	while(m<T)
	{
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
			{
				str[i][j]=d;
				infile>>str[i][j];
			}
		}
		z1=hen(str,t,x,o,d,m,outfile);
		z2=shu(str,t,x,o,d,m,outfile);
		z3=pie(str,t,x,o,d,m,outfile);
		z4=na(str,t,x,o,d,m,outfile);
		tt=false;
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
			{
				if(str[i][j]==d&&z1==0&&z2==0&&z3==0&&z4==0)
				{
					tt=true;
					break;
				}
			}
			if(tt)
				break;
		}
		if(tt&&z1==0&&z2==0&&z3==0&&z4==0)
			outfile<<"Case #"<<m+1<<":"<<"Game has not completed"<<endl;
		else if(!tt&&z1==0&&z2==0&&z3==0&&z4==0)
			outfile<<"Case #"<<m+1<<":"<<"Draw"<<endl;

		m++;
	}
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}

int hen(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile)
{
	int i,j,z,xx,oo;
	z=0;
	for(i=0;i<=3;i++)
	{
			xx=0;
			oo=0;
			for(j=0;j<=3;j++)
			{
				if(a[i][j]==x)
					xx++;
				else if(a[i][j]==o)
					oo++;
				else if(a[i][j]==t)
				{
					xx++;
					oo++;
				}
			}
			if(xx==4)
			{
				outfile<<"Case #"<<m+1<<": "<<"X won"<<endl;
				z=1;
				break;
			}
			else if(oo==4)
			{
				outfile<<"Case #"<<m+1<<": "<<"O won"<<endl;
				z=1;
				break;
			}
	}
	return z;
}

int shu(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile)
{
	int i,j,z,xx,oo;
	z=0;
	for(j=0;j<=3;j++)
	{
		xx=0;
		oo=0;
		for(i=0;i<=3;i++)
		{
			if(a[i][j]==x)
				xx++;
			else if(a[i][j]==o)
				oo++;
			else if(a[i][j]==t)
				{
					xx++;
					oo++;
				}
		}
		if(xx==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"X won"<<endl;
			z=2;
			break;
		}
		else if(oo==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"O won"<<endl;
			z=2;
			break;
		}
	}
	return z;
}

int pie(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile)
{
	int i,z,xx=0,oo=0;
	z=0;
	for(i=0;i<=3;i++)
		{
			if(a[i][i]==x)
				xx++;
			else if(a[i][i]==o)
				oo++;
			else if(a[i][i]==t)
				{
					xx++;
					oo++;
				}
		}
		if(xx==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"X won"<<endl;
			z=3;
		}
		else if(oo==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"O won"<<endl;
			z=3;
		}
	return z;
}

int na(char a[4][4],char t,char x,char o,char d,int m,ofstream &outfile)
{
	int i,z,xx=0,oo=0;
	z=0;
	for(i=0;i<=3;i++)
		{
			if(a[i][3-i]==x)
				xx++;
			else if(a[i][3-i]==o)
				oo++;
			else if(a[i][3-i]==t)
				{
					xx++;
					oo++;
				}
		}
		if(xx==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"X won"<<endl;
			z=4;
		}
		else if(oo==4)
		{
			outfile<<"Case #"<<m+1<<": "<<"O won"<<endl;
			z=4;
		}

	return z;
}