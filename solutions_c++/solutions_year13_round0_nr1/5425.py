#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
/************************************************************************/
/* 1表示X,2表示0,3表示draw,4表示未完成                                                                     */
/************************************************************************/
int test(char a[4][4]);
int test2(char a[4]);
int main()
{
	ifstream input("A-small-attempt0.in");
	ofstream out("a.out");
	int N;
	input>>N;
	char data[1000][4][4];
	for(int i=0;i<N;i++)
	{
		for(int i1=0;i1<4;i1++)
			for(int j1=0;j1<4;j1++)
			{
				input>>data[i][i1][j1];
			}

		switch(test(data[i]))
		{
		case 1:
			out<<"Case #"<<i+1<<": X won"<<endl;
			break;
		case 2:
			 out<<"Case #"<<i+1<<": O won"<<endl;
			break;
		case 3:
			 out<<"Case #"<<i+1<<": Draw"<<endl;
			break;
		case 4:
			 out<<"Case #"<<i+1<<": Game has not completed"<<endl;
			break;
		}


	}
	input.close();
	out.close();
	return 0;
}
int test(char a[4][4])
{
	bool X=false;
	bool O=false;
	bool draw=false;
	bool Not=false;
	char b[4];
	//横着四个
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		b[j]=a[i][j];

		switch(test2(b))
		{
		case 1:
			X=true;
			break;
		case 2:
			O=true;
			break;
		case 3:
			draw=true;
			break;
		case 4:
			Not=true;
			break;
		}
	}
	//竖着四个
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
			b[j]=a[j][i];

		switch(test2(b))
		{
		case 1:
			X=true;
			break;
		case 2:
			O=true;
			break;
		case 3:
			draw=true;
			break;
		case 4:
			Not=true;
			break;
		}
	}
	//左斜一个
		for(int i=0;i<4;i++)
			b[i]=a[i][i];

		switch(test2(b))
		{
		case 1:
			X=true;
			break;
		case 2:
			O=true;
			break;
		case 3:
			draw=true;
			break;
		case 4:
			Not=true;
			break;
		}
	//右斜一个
		for(int i=0;i<4;i++)
			b[i]=a[i][3-i];

		switch(test2(b))
		{
		case 1:
			X=true;
			break;
		case 2:
			O=true;
			break;
		case 3:
			draw=true;
			break;
		case 4:
			Not=true;
			break;
		}
	
	if(X)
		return 1;
	if(O)
		return 2;
	if(Not)
		return 4;
	if(draw)
		return 3;
	
}
int test2(char a[4])
{
	if(a[0]=='T')
	{
		for(int i=1;i<4;i++)
			if(a[i]=='.')
				return 4;
		if(a[1]!=a[2]||a[1]!=a[3]||a[2]!=a[3])
			return 3;
	}else if(a[0]=='X'||a[0]=='O')
	{
		for(int i=1;i<4;i++)
		{
			if(a[i]=='.')
				return 4;
			if(a[i]!=a[0]&&a[i]!='T')
				return 3;
		}
		if(a[0]=='X')
			return 1;
		if(a[0]=='O')
			return 2;
	}else if(a[0]=='.')
	{
			return 4;
	}

	
}