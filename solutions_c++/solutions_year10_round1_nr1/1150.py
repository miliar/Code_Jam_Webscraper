#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <stdio.h>
#include <conio.h>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

// Global variables


int main() 
{
    /* Files */
    ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
    
    /* Variables */
    int T, N, K;
	char rotate[60][60];
	string aux;
	bool On;
    
    /* Read File */
    fin >> T;
    For (n, 1, T)
    {
        // Read Case
        fin >> N >> K;

		Fill (rotate, '.');
        For (i, 1, N)
        {
            fin >> aux;
			int p = N;
			Ford (j, aux.length()-1, 0)
			{
				if (aux[j] != '.')
				{
					rotate[i][p] = (char)aux[j];
					p--;
				}
			}
        }

		// Process Rows
		bool Red = false;
		bool Blue = false;
		int nRed = 0;
		int nBlue = 0;
		For (i, 1, N)
		{
			For (j, 1, N)
			{
				if ((rotate[i][j] == 'R') && (rotate[i][j-1] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[i][j] == 'B') && (rotate[i][j-1] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
			}
		}

		// Process Columns
		nRed = 0;
		nBlue = 0;
		For (i, 1, N)
		{
			For (j, 1, N)
			{
				if ((rotate[j][i] == 'R') && (rotate[j-1][i] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[j][i] == 'B') && (rotate[j-1][i] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
			}
		}

		// Process Diagonals (1)
		nRed = 0;
		nBlue = 0;
		For (i, 1, N)
		{
			int j = 0;
			while (j + i <= N)
			{
				if ((rotate[i + j][j + 1] == 'R') && (rotate[i + j - 1][j] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[i + j][j + 1] == 'B') && (rotate[i + j - 1][j] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
				j++;
			}
		}

		// Process Diagonals (2)
		nRed = 0;
		nBlue = 0;
		For (i, 1, N)
		{
			int j = 0;
			while (j + i <= N)
			{
				if ((rotate[(N + 1) - (i + j)][j + 1] == 'R') && (rotate[N + 1 - (i + j) + 1][j] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[(N + 1) - (i + j)][j + 1] == 'B') && (rotate[N + 1 - (i + j) + 1][j] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
				j++;
			}
		}

		// Process Diagonals (3)
		nRed = 0;
		nBlue = 0;
		For (i, 1, N)
		{
			int j = 0;
			while (j + i <= N)
			{
				if ((rotate[i + j][N + 1 - (j + 1)] == 'R') && (rotate[i + j - 1][N + 1 - (j + 1) + 1] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[i + j][N + 1 - (j + 1)] == 'B') && (rotate[i + j - 1][N + 1 - (j + 1) + 1] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
				j++;
			}
		}
        
		// Process Diagonals (4)
		nRed = 0;
		nBlue = 0;
		For (i, 1, N)
		{
			int j = 0;
			while (j + i <= N)
			{
				if ((rotate[N + 1 - (i + j)][N + 1 - (j + 1)] == 'R') && (rotate[N + 1 - (i + j) + 1][N + 1 - (j + 1) + 1] == 'R'))
					nRed++;
				else
					nRed = 0;
				if (nRed >= K-1)
					Red = true;
				if ((rotate[N + 1 - (i + j)][N + 1 - (j + 1)] == 'B') && (rotate[N + 1 - (i + j) + 1][N + 1 - (j + 1) + 1] == 'B'))
					nBlue++;
				else
					nBlue = 0;
				if (nBlue >= K-1)
					Blue = true;
				j++;
			}
		}

        /* Print answer */
        fout << "Case #" << n << ": ";
		if (Red && Blue)
			fout << "Both";
		else
			if (!Red && !Blue)
				fout << "Neither";
			else
				if (Red)
					fout << "Red";
				else
					fout << "Blue";
		fout << endl;
    }
    
    //getch();
    //cin.get();
    fout.close();
    fin.close();
	exit(0);
}
