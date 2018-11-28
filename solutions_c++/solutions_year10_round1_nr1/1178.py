#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int T, N, K;
int RWIN=0, BWIN=0;
char board[50][50];
char newboard[50][50];
char temp[50];
char cur;
int cts; // continuous occurrings of c

void pb()
{
	cout << "board" << endl;
	for (int i=0;i<N;i++)
	{
		for (int j=0;j<N;j++)
			cout << board[j][i];
		cout << endl;
	}
		cout << endl;
}

void pnb()
{
	cout << "new board" << endl;
	for (int i=0;i<N;i++)
	{
		for (int j=0;j<N;j++)
			cout << newboard[j][i];
		cout << endl;
	}
		cout << endl;
}

void rotate()
{
	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++)
			newboard[N-j-1][i] = board [i][j];
}

void fall()
{
	for (int z=0;z<N-1;z++)
	{
		for (int i=N-2;i>=z;i--)
		{
			for (int j=0;j<N;j++)
			{
				if (newboard[j][i] != '.' &&  newboard[j][i+1] == '.')
				{
					newboard[j][i+1] = newboard[j][i];
					newboard[j][i] = '.';
				}
	//		newboard[N-j-1][i] = board [i][j];
			}
		}
	}			
}

void checkhorz()
{
	for (int i=0;i<N;i++)
	{
		cur = newboard[0][i];
		cts = 1;
		for (int j=1;j<N;j++)
		{
			if (newboard[j][i] != '.' && newboard[j][i] == cur)
				cts++;
			else
			{
				cts = 1;
				cur = newboard[j][i];
			}
			if (cts == K)
			{
				if (cur == 'R')
					RWIN = true;
				else if (cur == 'B')
				{
					BWIN = true;
				}  
				else
					cout << "This is bad" << endl;
			}
		}
	}	
}

void checkvert()
{
	for (int j=0;j<N;j++)
	{
		cur = newboard[j][0];
		cts = 1;
		for (int i=1;i<N;i++)
		{
			if (newboard[j][i] != '.' && newboard[j][i] == cur)
				cts++;
			else
			{
				cts = 1;
				cur = newboard[j][i];
			}
//			cout << "here is cts " <<  cts << endl;
			if (cts == K)
			{
				if (cur == 'R')
					RWIN = true;
				else if (cur == 'B')
					BWIN = true;
				else
					cout << "This is bad" << endl;
//					cout << "someone won" <<endl;
			}
		}
	}	
}


void checkdiag()
{
	int x =0, i=0;
	for (int y=0;y<N;y++)
	{
//		for (int i=y+1;i<N;i++)
		{
			i=y+1;
			cur = newboard[x][y];
			cts = 1;
			for (int j=1;j<N && i<N;j++)
			{ 
				if (newboard[j][i] != '.' && newboard[j][i] == cur)
					cts++;
				else
				{
					cts =1;
					cur = newboard[j][i];
				}
				if (cts == K)
				{
					if (cur == 'R')
						RWIN = true;
					else if (cur == 'B')
						BWIN = true;
					else
						cout << "This is bad" << endl;
				}
				i++;
			}
		}			
	}	
	
	x =0;
	for (int y=0;y<N;y++)
	{
//		for (int i=y+1;i<N;i++)
		{
			i=y-1;
			cur = newboard[x][y];
			cts = 1;
			for (int j=1;j<N && i>=0;j++)
			{ 
				if (newboard[j][i] != '.' && newboard[j][i] == cur)
					cts++;
				else
				{
					cts =1;
					cur = newboard[j][i];
				}
				if (cts == K)
				{
					if (cur == 'R')
						RWIN = true;
					else if (cur == 'B')
						BWIN = true;
					else
						cout << "This is bad" << endl;
				}
				i--;
			}
		}			
	}	
	x =N-1;
	for (int y=0;y<N;y++)
	{
//		for (int i=y+1;i<N;i++)
		{
			i=y+1;
			cur = newboard[x][y];
			cts = 1;
			for (int j=N-2;j>=0 && i<N;j--)
			{ 
				if (newboard[j][i] != '.' && newboard[j][i] == cur)
					cts++;
				else
				{
					cts =1;
					cur = newboard[j][i];
				}
				if (cts == K)
				{
					if (cur == 'R')
						RWIN = true;
					else if (cur == 'B')
						BWIN = true;
					else
						cout << "This is bad" << endl;
				}
				i++;
			}
		}			
	}	
	x =N-1;
	for (int y=0;y<N;y++)
	{
//		for (int i=y+1;i<N;i++)
		{
			i=y-1;
			cur = newboard[x][y];
			cts = 1;
			for (int j=N-2;j>=0 && i>=0;j--)
			{ 
				if (newboard[j][i] != '.' && newboard[j][i] == cur)
					cts++;
				else
				{
					cts =1;
					cur = newboard[j][i];
				}
				if (cts == K)
				{
					if (cur == 'R')
						RWIN = true;
					else if (cur == 'B')
						BWIN = true;
					else
						cout << "This is bad" << endl;
				}
				i--;
			}
		}			
	}	
}
int main()
{
	ofstream out;
	ifstream in;
	out.open("rotate_large.out");
	in.open("A-large.in");
	in >> T;
	for (int l=0;l<T;l++)
	{
		in >> N >> K;
		RWIN =0;
		BWIN =0;
		cts =0;
		cur = 'q';
		for(int y=0;y<N;y++)
		{
		 	in >> temp;
			for (int i=0;i<N;i++)
				board[i][y] = temp[i];
		}	
	//	pb();
		rotate();
	//	pnb();
		fall();
		pnb();
		checkhorz();
		checkvert();
		checkdiag();
		cout << "Case #" << l+1 << ": ";
		out << "Case #" << l+1 << ": ";
		if (RWIN && BWIN)
		{
			cout << "Both" << endl;
			out << "Both" << endl;
		}
		else if (RWIN)
		{
			cout << "Red" << endl;
			out << "Red" << endl;
		}
		else if (BWIN)
		{
			cout << "Blue" << endl;
			out << "Blue" << endl;
		}
		else
		{
			cout << "Neither" <<endl;
			out << "Neither" <<endl;
		}	
//		for (int y=0;y<N;y++)
//			cout << board[*][y] << endl;
	}
	
	system("PAUSE");
	return 0;
}
