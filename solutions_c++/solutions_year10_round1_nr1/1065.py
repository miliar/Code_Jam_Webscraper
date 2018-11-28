#include<iostream>
#include<fstream>
using namespace std;

char map[100][100];
char tmp[100][100];
char fin[100][100];
int a,b;
void rotate()
{
	for(int i=0;i<a;i++)
	{
		for(int j=0;j<a;j++)
			tmp[j][a-i-1] = map[i][j];
	}
	for(int i=0;i<a;i++)
	{
		for(int j=0;j<a;j++)
			if(tmp[i][j]!='.')
			{
				int c=0;
				for(int k=i;k<a;k++)
				{
					if(tmp[k][j]=='.')
						c++;
				}
				fin[i+c][j] = tmp[i][j];
			}
	}
}

int check()
{
	bool fin1,fin2;
	fin1 = fin2 = false;
	for(int i=0;i<a && !fin1;i++)
	{
		for(int j=0;j<a && !fin1;j++)
		{
			if(fin[i][j]=='B')
			{
				int c = 0;
				for(int k=i;k<a;k++)
				{
					if(fin[k][j]=='B')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin1 = true;
					break;
				}
				c = 0;
				for(int k=j;k<a;k++)
				{
					if(fin[i][k]=='B')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin1 = true;
					break;
				}
				c = 0;
				for(int k=0;i+k<a && j+k<a;k++)
				{
					if(fin[i+k][j+k]=='B')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin1 = true;
					break;
				}
				c = 0;
				for(int k=0;i+k<a && j-k>=0;k++)
				{
					if(fin[i+k][j-k]=='B')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin1 = true;
					break;
				}
			}
		}
	}
	for(int i=0;i<a && !fin2;i++)
	{
		for(int j=0;j<a && !fin2;j++)
		{
			if(fin[i][j]=='R')
			{
				int c = 0;
				for(int k=i;k<a;k++)
				{
					if(fin[k][j]=='R')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin2 = true;
					break;
				}
				c = 0;
				for(int k=j;k<a;k++)
				{
					if(fin[i][k]=='R')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin2 = true;
					break;
				}
				c = 0;
				for(int k=0;i+k<a && j+k<a;k++)
				{
					if(fin[i+k][j+k]=='R')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin2 = true;
					break;
				}
				c = 0;
				for(int k=0;i+k<a && j-k>=0;k++)
				{
					if(fin[i+k][j-k]=='R')
						c++;
					else
						break;
				}
				if(c>=b)
				{
					fin2 = true;
					break;
				}
			}
		}
	}
	return fin1+fin2*2;
}

int main()
{
	int t;
	ofstream fout("ans");
	cin >> t;
	for(int m=0;m<t;m++)
	{
		cin >> a >> b;
		for(int i=0;i<100;i++)
			for(int j=0;j<100;j++)
				fin[i][j] = 0;
		for(int i=0;i<a;i++)
			cin >> map[i];
		rotate();
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<a;j++)
				cout << fin[i][j];
			cout << endl;
		}
		int k = check();
		fout << "Case #"<<m+1 << ": ";
		if(k==1)
			fout << "Blue" << endl;
		else if(k==2)
			fout << "Red" << endl;
		else if(k==3)
			fout << "Both" << endl;
		else
			fout << "Neither" << endl;
	}
}