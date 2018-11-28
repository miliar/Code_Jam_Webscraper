#include "iostream"
#include "fstream"
#include "string"

using namespace std;

#define R 1
#define B 2
#define North 10
#define West 11
#define East 12
#define South 13
#define NW 14
#define NE 15
#define SW 16
#define SE 17

void rotate(int** table, int N)
{
	int **rotTable = new int*[N];
	for(int i=0; i<N; i++)
	{
		rotTable[i] = new int[N];
		memset(rotTable[i], 0, N*sizeof(int));
	}
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<N; j++)
		{
			if(table[i][j] == 0)
				continue;
			//int tmp = table[i][j];
			//table[i][j] = table[j][N-i-1];
			//table[j][N-i-1] = tmp;
			rotTable[j][N-i-1] = table[i][j];
		}
	}
	for(int i=0; i<N; i++)
	{
		memcpy(table[i], rotTable[i], N*sizeof(int));
	}
}

void move(int** table, int N)
{
	for(int i=N-1; i>=0; i--)
	{
		for(int j=0; j<N; j++)
		{
			if(table[i][j] == 0)
				continue;
			if(i < N-1)
			{
				int k = i + 1;
				if(table[k][j] != 0)
					continue;
				while(table[k][j] == 0)
				{
					k++;
					if(k > N-1)
						break;
				}
				k--;
				table[k][j] = table[i][j];
				table[i][j] = 0;
			}
		}
	}
}
int next(int** table, int** map, int N, int r, int c, int type, int orient)
{
	switch(orient)
	{
	case North:
		r--;
		break;
	case East:
		c++;
		break;
	case West:
		c--;
		break;
	case South:
		r++;
		break;
	case NE:
		r--;
		c++;
		break;
	case NW:
		r--;
		c--;
		break;
	case SE:
		r++;
		c++;
		break;
	case SW:
		r++;
		c--;
		break;
	}
	if(r<0 || r>N-1)
		return 0;
	if(c<0 || c>N-1)
		return 0;
	if(map[r][c] != 0)
		return 0;
	if(table[r][c] != type)
		return 0;
	int sum = 1;
	//map[r][c] = 1;
	return sum + next(table, map, N, r, c, type, orient);
}
int check(int** table, int** map, int N, int K)
{
	int type1 = -1;
	int type2 = -1;
	for(int i=0; i<N; i++)
	{
		if(type1 != -1 && type2 != -1)
			break;
		for(int j=0; j<N; j++)
		{
			if(table[i][j] == 0)
				continue;
			//if(map[i][j] != 0)
			//	continue;
			int type = table[i][j];
			if(type == type1)
				continue;
			if(type == type2)
				continue;
			map[i][j] = 1;
			int sum;
			for(int oo = North; oo<=SE; oo++)
			{
				sum = 1 + next(table, map, N, i, j, type, oo);
				if(sum == K)
				{
					if(type1 == -1)
						type1 = type;
					else if(type2 == -1)
						type2 = type;
				}
			}
		}
	}
	if(type1 != -1 && type2 != -1)
		return 3;
	if(type1 != -1)
		return type1;
	if(type2 != -1)
		return type2;
	if(type1 == -1 && type2 == -1)
		return -1;
}

void printMat(int** table, int N)
{
	for(int j=0; j<N; j++)
	{
		for(int k=0; k<N; k++)
		{
			if(table[j][k] == 0)
				cout << ".";
			if(table[j][k] == R)
				cout << "R";
			if(table[j][k] == B)
				cout << "B";
		}
		cout << endl;
	}
}
void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int N, K, T;
	infile >> T;
	for(int i=0; i<T; i++)
	{
		infile >> N >> K;
		int ** table = new int*[N];
		int ** map = new int*[N];
		string str = "Neither";
		for(int j=0; j<N; j++)
		{
			table[j] = new int[N];
			map[j] = new int[N];
			for(int k=0; k<N; k++)
			{
				map[j][k] = 0;
				char c;
				infile >> c;
				if(c == '.')
				{
					table[j][k] = 0;
				}
				else if(c == 'R')
				{
					table[j][k] = R;
				}
				else if(c == 'B')
				{
					table[j][k] = B;
				}
			}
		}
		rotate(table, N);
		//printMat(table, N);
		move(table, N);
		//cout << K << endl;
		//printMat(table, N);
		
		int res = check(table, map, N, K);
		
		if(res == B)
			str = "Blue";
		if(res == R)
			str = "Red";
		if(res == 3)
			str = "Both";
		outfile << "Case #" << i+1 << ": " << str << endl;
		cout << "Case #" << i+1 << ": " << str << endl;
		
		delete[]table;
		delete[]map;
	}

	infile.close();
	outfile.close();
}