#include<string>
#include<iostream>
#include<fstream>
using namespace std;

	ifstream infile("PA.in");
	ofstream ofile("PA.txt");
	int stat[4][4];
	int sum1[4];
	int sum2[4];
	bool comp;



void init()
{
	for (int i=0; i!=4; ++i)
	{
		for (int j=0; j!=4; ++j)
		{
			stat[i][j]=0;
		}
		sum1[i]=0;
		sum2[i]=0;
	}
	comp=true;
}
void read()
{
	for (int i=0; i!=4; ++i)
	{
		for (int j=0; j!=4; ++j)
		{
			char ch;
			infile>>ch;
			switch (ch)
			{
			case 'X':
				stat[i][j]=-1;break;
			case 'O':
				stat[i][j]=1;break;
			case 'T':
				stat[i][j]=100;break;
			case '.':
				comp=false;
				stat[i][j]=0;break;
			}
			sum1[i]+=stat[i][j];
			sum2[j]+=stat[i][j];
		}
	}
}
string calc()
{
	for (int i=0; i!=4; ++i)
	{
		int tmp1=stat[0][0]+stat[1][1]+stat[2][2]+stat[3][3];
		int tmp2=stat[0][3]+stat[1][2]+stat[2][1]+stat[3][0];
		if ((sum1[i]==-4)||(sum1[i]==97)||(sum2[i]==-4)||(sum2[i]==97)||(tmp1==-4)||(tmp1==97)||(tmp2==-4)||(tmp2==97))
		{
			return "X won";
		}
		if ((sum1[i]==4)||(sum1[i]==103)||(sum2[i]==4)||(sum2[i]==103)||(tmp1==4)||(tmp1==103)||(tmp2==4)||(tmp2==103))
		{
			return "O won";
		}
		if (comp)
		{
			return "Draw";
		}
		else
			return "Game has not completed";
	}
}
void print(int i,string s)
{
	ofile<<"Case #"<<i<<": "<<s<<endl;
}


int main()
{

	int t;
	infile>>t;

	for (int i=0; i!=t; ++i)
	{
		init();
		read();
		string s=calc();
		print(i+1,s);
	}

	return 0;
}






