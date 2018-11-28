#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int getCode(char c)
{
	switch (c)
	{
	case 'Q':
		return 0;
	case 'W':
		return 1;
	case 'E':
		return 2;
	case 'R':
		return 3;
	case 'A':
		return 4;
	case 'S':
		return 5;
	case 'D':
		return 6;
	case 'F':
		return 7;
	default:
		return 8;
	}
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("B-large.out");
	string buf;
	char T[9][9];
	bool X[9][9];
	

	int n;
	int C,D,N;
	in>>n;
	char Q[100];
	int k=0;
	for (int i=0; i<n; i++)
	{
		for (int q=0; q<9; q++)
		for (int j=0; j<9; j++)
		{T[q][j]=0;X[q][j]=0;}
		k=0;

		in>>C;
		for (int j=0; j<C; j++)
		{
			in>>buf;
			T[getCode(buf[0])][getCode(buf[1])]=buf[2];
			T[getCode(buf[1])][getCode(buf[0])]=buf[2];
		}
		in>>D;
		for (int j=0; j<D; j++)
		{
			in>>buf;
			X[getCode(buf[0])][getCode(buf[1])]=1;
			X[getCode(buf[1])][getCode(buf[0])]=1;
		}
		in>>N>>buf;
		for (int j=0; j<N; j++)
		{
			Q[k++]=buf[j];
			if (k<2) continue;

			if (T[getCode(Q[k-1])][getCode(Q[k-2])]) 
			{Q[k-2]=T[getCode(Q[k-1])][getCode(Q[k-2])];--k;}
			else for (int q=0; q<=k-2; q++)
				if (X[getCode(Q[q])][getCode(Q[k-1])]) 
					k=0;

		};


		out<<"Case #"<<i+1<<": [";
		for (int j=0; j<k-1; j++)
			out<<(char)Q[j]<<", ";
		if (k) out<<(char)Q[k-1];
		out<<"]"<<endl;

	}
	in.close();
	out.close();
	return 0;
}