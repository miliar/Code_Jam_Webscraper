/*
ID: aditya21
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
char curel='a';
char processrec(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat, int x, int y);
void processmap(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat);

int main() 
{
	ifstream fin ("d:\\io\\B-large.in");
	ofstream fout ("d:\\io\\B-large.out");

	int a, b, c;
	int i, j, k;
	int p, q, r, x, y, z;
	
	vector<vector<char> > mat;
	vector<char> chrow;
	int cost,max;
	string str1,str2;
	char str[510];
	vector<vector<int> > table;
	vector<int> row;
	
	fin>>a;
	for(i=0;i<a;i++)
	{
		fout<<"Case #"<<(i+1)<<": \n";
		cout<<"Case #"<<(i+1)<<": \n";
		fin>>b>>c;
		curel = 'a';
		table.clear();
		for(j=0;j<b;j++)
		{
			row.clear();
			for(k=0;k<c;k++)
			{
				fin>>z;
				row.push_back(z);
			}
			table.push_back(row);
		}
		mat.clear();
		for(j=0;j<b;j++)
		{
			chrow.clear();
			for(k=0;k<c;k++)
			{
				chrow.push_back('$');
			}
			mat.push_back(chrow);
		}
		
		processmap(table,b,c,mat);

		for(j=0; j<b; j++)
		{
		for(k=0;k<c;k++)
		{
			fout<<mat[j][k]<<" ";
		}
			fout<<endl;
		}

	}
}

void processmap(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat)
{
	int i,j,k,p,q,r;
	for(i=0; i<b; i++)
	{
		for(j=0; j<c; j++)
		{
			if(mat[i][j] == '$')
			{
				if(processrec(table, b, c, mat, i, j) == curel)
					curel++;
			}
		}
	}
}

char processrec(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat, int x, int y)
{
	int p,q;
	int min;
	p = x;
	q = y;
	char ch;
	if(mat[x][y] != '$')
		return mat[x][y];
	min = table[x][y]-1;
	if(x<b-1 && min >= table[x+1][y] )
	{
		p = x+1; q = y;
		min = table[x+1][y];
	}
	if(y<c-1 && min >= table[x][y+1] )
	{
		q = y+1; p = x;
		min = table[x][y+1];
	}
	if(y>0 && min >= table[x][y-1])
	{
		q = y-1; p = x;
		min = table[x][y-1];
	}
	if(x>0 && min >= table[x-1][y])
	{
		p = x-1; q = y;
		min = table[x-1][y];
	}

	if(p != x || q != y)
	{
		ch = processrec(table, b, c, mat, p, q);
	}
	else
		ch = curel;

	mat[x][y] = ch;
	return ch;
}
