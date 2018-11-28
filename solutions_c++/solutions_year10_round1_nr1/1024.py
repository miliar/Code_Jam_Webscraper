//////////////////////////
// Author:
// Date:
// Title:
// Function:
//////////////////////////
#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<conio.h>
using namespace std;

#define xin fin
#define xout fout
#define f(i,a,b) for (i=a;i<=b;i++)

bool row(char map[][51],char c);
bool col(char map[][51], char c);
bool dia(char map[][51], char c);
int n,k;
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	char map[51][51];
	register int p,q,m,i,j,z;
	int t;
	char c;
	bool yes,B,R;
	xin >> t;
	f(z,1,t)
	{
		xin >> n >> k;
		for (j=n;j>0;j--)
		{
			f(i,1,n)
			{
				xin >> map[i][j];
			}
		}
		for(i=n;i>0;i--)
		{
			yes = true;
			f(j,1,n)
			{
				if (map[i][j] != '.')
				{
					yes = false;
					break;
				}
			}
			if (!yes)
			{
				f(j,1,n)
				{
					p = i;
					q = i-1;
					while (q > 0)
					{
						while ((p > 0)&&(map[p][j] != '.'))
						{
							p--;
						}
						q = p - 1;
						if (q <= 0)
						{
							break;
						}
						while ((q > 0)&&(map[q][j] == '.'))
						{
							q--;
						}
						if (q == 0)
						{
							break;
						}
						map[p][j] = map[q][j];
						map[q][j] = '.';
						p --;
					}
				}
				break;
			}
		}
		xout << "Case #" << z << ": ";
		B = row(map,'B');
		if (!B)
		{
			B = col(map, 'B');
			if (!B)
				B = dia(map,'B');
		}
		R = row(map,'R');
		if (!R)
		{
			R = col(map, 'R');
			if (!R)
				R = dia(map,'R');
		}
		if (R && B)
		{
			xout << "Both" << endl;
		}
		else
		{
			if (R)
			{
				xout << "Red\n";
			}
			else
			{
				if (B)
				{
					xout << "Blue\n";
				}
				else
				{
					xout << "Neither\n";
				}
			}
		}
	}
	fin.close();;
	fout.close();
	return 0;
}
bool row(char map[][51],char c)
{
	register int i,j;
	int count;
	bool res;
	f(i,1,n)
	{
		res = false;
		count = 0;
		j = 1;
		while (j<=n)
		{
			while ((j<=n) && (map[i][j]) != c)
			{
				j++;
			}
			count = 0;
			while((j<=n) && map[i][j] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			break;
		}
	}
	return res;
}
bool col(char map[][51], char c)
{
	register int i,j;
	int count;
	bool res;
	f(i,1,n)
	{
		res = false;
		count = 0;
		j = 1;
		while (j<=n)
		{
			while ((j<=n) && (map[j][i]) != c)
			{
				j++;
			}
			count = 0;
			while((j<=n) && map[j][i] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			break;
		}
	}
	return res;
}
bool dia(char map[][51], char c)
{
	register int i,j;
	int count,l;
	bool res;
	f(i,1,n)
	{
		res = false;
		count = 0;
		j = 0;
		l = n + 1 - i;
		if (l < k)
		{
			break;
		}
		while (j<l)
		{
			while ((j<l) && (map[1+j][i+j]) != c)
			{
				j++;
			}
			count = 0;
			while((j<l) && map[1+j][i+j] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			return res;
			break;
		}
	}

	f(i,2,n)
	{
		res = false;
		count = 0;
		j = 0;
		l = n + 1 - i;
		if (l < k)
		{
			break;
		}
		while (j<l)
		{
			while ((j<l) && (map[i+j][1+j]) != c)
			{
				j++;
			}
			count = 0;
			while((j<l) && map[i+j][1+j] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			return res;
			break;
		}
	}

	f(i,k,n)
	{
		res = false;
		count = 0;
		j = 0;
		l = i;
		while (j<l)
		{
			while ((j<l) && (map[j+1][l-j]) != c)
			{
				j++;
			}
			count = 0;
			while((j<l) && map[1+j][l-j] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			return res;
			break;
		}
	}

	f(i,2,n+1-k)
	{
		res = false;
		count = 0;
		j = 0;
		l = n+1-i;
		while (j<l)
		{
			while ((j<l) && (map[j+i][n-j]) != c)
			{
				j++;
			}
			count = 0;
			while((j<l) && map[i+j][n-j] == c)
			{
				count++;
				j++;
			}
			if (count >= k)
			{
				res  = true;
				break;
			}
		}
		if (res)
		{
			return res;
			break;
		}
	}
	return res;
}
