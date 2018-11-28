#include <iostream>
#include <fstream>

using namespace std;

static int alt[100][100];
static char basin[100][100];
static int H, W;
static char ch;

bool serarchNextPos(int m, int n, int & m_next, int & n_next)
{
	int surAlt[] = {10001, 10001, 10001, 10001};//north, west, east, south's altitude
	int maxAlt = 10000;
	int i = 0;
	
	if (m - 1 >= 0)	
	{
		surAlt[0] = alt[m - 1][n];	
	}
	
	if (n - 1 >= 0)
	{
		surAlt[1] = alt[m][n - 1];	
	}
	
	if (n + 1 < W)
	{
		surAlt[2] = alt[m][n + 1];
	}
	
	if (m + 1 < H)
	{
		surAlt[3] = alt[m + 1][n];
	}
	
	for (maxAlt = surAlt[0], i = 1; i < 4; i++)
	{
		if (surAlt[i] < maxAlt)
		{
			maxAlt = surAlt[i];	
		}
	}
	
	if (alt[m][n] > maxAlt)
	{
		i = 0;
		do
		{
			if (surAlt[i] == maxAlt)
			{
				break;
			}else
			{
				i++;	
			}
		}while(i < 4);
		
		switch(i)
		{
			case 0 : m_next = m - 1; n_next = n; break;
			case 1 : m_next = m; n_next = n - 1; break;
			case 2 : m_next = m; n_next = n + 1; break;
			case 3 : m_next = m + 1; n_next = n; break;
			default :;
		}
		return true;
	}else
	{
		return false;	
	}	
}

void fill(int m, int n)
{
	int m_next, n_next;
	if (serarchNextPos(m, n, m_next, n_next))
	{		
		if (basin[m_next][n_next] == '#')
		{
			fill(m_next, n_next);
			basin[m][n] = basin[m_next][n_next];
		}else
		{
			basin[m][n] = basin[m_next][n_next];	
		}
	}else 
	{
		basin[m][n] = ch++;	
	}
}

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");
	
	int N;
	
	infile >> N;
	
	for (int i = 0; i < N; i++)
	{	
		int j = 0, k = 0;
		
		ch = 'a';
			
		infile >> H >> W;
			
		for (j = 0; j < H; j++)
		{
			for (k = 0; k < W; k++)
			{
				infile >> alt[j][k];
				basin[j][k] = '#';
			}	
		}
		
		for (j = 0; j < H; j++)
		{
			for (k = 0; k < W; k++)
			{
				if (basin[j][k] == '#')
				{
					fill(j, k);	
				}
			}
		}
		
		outfile << "Case #" << i + 1 << ":" << endl;
		
		for (j = 0; j < H; j++)
		{
			for (k = 0; k < W - 1; k++)
			{
				outfile << basin[j][k] << ' ';
			}
			
			outfile << basin[j][k] << endl;
		}
		
	}
	
	infile.close();
	outfile.close();

	return 0;	
}
