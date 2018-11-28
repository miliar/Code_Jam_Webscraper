#include <iostream>
#include <iomanip>
#include <cstdlib>

#include<assert.h>

using namespace std;

inline int read(int &x){
	x = 0; // reset x;
	int sign, ch = getchar();
	while ((ch < '0' || ch > '9') && ch != '-' && ch != EOF) ch = getchar();
	if (ch=='-') sign = -1, ch = getchar();
	else sign = 1;
	do x = (x << 3) + (x << 1) + ch - '0';
	while((ch=getchar())>='0' && ch<='9');
	x *= sign;
	return 1;
}

inline void swap(int& a, int& b)
{
	int temp = a; a = b; b = temp;
}

int cmp(const void *v1, const void *v2)
{
	const int i1 = *(const int *)v1;
	const int i2 = *(const int *)v2;

	return i1 < i2 ? -1 : ( i1 > i2 );
}

inline int modValue(const int n)
{
	return n >= 0? n : -n;
}


const int DIM = 4;
int main() 
{
	int n_cases;

	read(n_cases);
	char B[DIM][DIM];
	char right[DIM], down[DIM], fd, rd;

	int case_no = 1;
	while ( case_no <= n_cases)
	{
		fd = 0; rd = 0;
		for(int q = 0; q < DIM; q++)
		{
			right[q] = 0; down[q] = 0; 
		}
		char state = 'I';

		char ch;
		int n_dots = 0;
		for ( int i = 0; i < DIM; i++)
		{
			for (int j = 0; j < DIM; j++)
			{

				while(1)
				{
					ch = getchar();
					if (ch == 'O' || ch == '.' || ch == 'X' || ch == 'T') break;
				}
				B[i][j] = ch;

				/* case 'right' */
				if(B[i][j] != '.')
				{
					if (j > 0)
					{
						if(B[i][j] == B[i][j-1] || B[i][j] == 'T' || (B[i][j-1] == 'T' && (j == 1 || B[i][j] == B[i][j-2])))
						{
							right[i]++;
							if (right[i] == DIM)
							{
								state = B[i][j];
								if (state = 'T') state = B[i][j-1];
							}
						}
						else
							right[i] = 1;
					}
					else 
						right[i] = 1;
				}
				else
				{
					right[i] = 0;
					n_dots++;
				}

				/* case 'down' */
				if(B[i][j] != '.')
				{
					if (i > 0)
					{
						if(B[i][j] == B[i - 1][j] || B[i][j] == 'T' || (B[i - 1][j] == 'T' && (i == 1 || B[i][j] == B[i - 2][j])))
						{
							down[j]++;
							if (down[j] == DIM)
							{
								state = B[i][j];
								if (state = 'T') state = B[i - 1][j];
							}
						}
						else
							down[j] = 1;
					}
					else 
						down[j] = 1;
				}
				else
					down[j] = 0;

				/* Case forward diag */
				if(i == j)
				{
					if (B[i][j] != '.')
					{
						if(i > 0)
						{
							if(B[i][j] == B[i - 1][j - 1] || B[i][j] == 'T' || (B[i - 1][j - 1] == 'T' && (i == 1 || B[i][j] == B[i - 2][j - 2])))
							{
								fd++;
								if (fd == DIM)
								{
									state = B[i][j];
									if (state = 'T') state = B[i - 1][j - 1];
								}
							}
							else
								fd = 1;
						}
						else
							fd = 1;
					}
					else
					{
						fd = 0;
					}
				}

				/* Case reverse diag */
				int _j = DIM - 1 - j;
				if(i == _j)
				{
					if (B[i][j] != '.')
					{
						if(i > 0)
						{
							if(B[i][j] == B[i - 1][j + 1] || B[i][j] == 'T' || (B[i - 1][j + 1] == 'T' && (i == 1 || B[i][j] == B[i - 2][j + 2])))
							{
								rd++;
								if (rd == DIM)
								{
									state = B[i][j];
									if (state = 'T') state = B[i - 1][j + 1];
								}
							}
							else
								rd = 1;
						}
						else
							rd = 1;
					}
					else
					{
						rd = 0;
					}
				}
			}
		}
		if (n_dots == 0 && state == 'I') state ='D';


		switch(state)
		{
		case 'X': case 'O': cout << "Case #" << case_no << ": " << state << " won" << endl;
			break;
		case 'D': cout << "Case #" << case_no << ": Draw" << endl;
			break;
		case 'I': cout << "Case #" << case_no << ": Game has not completed" << endl;
			break;
		}

		case_no++;
	}

	// system("PAUSE");
	return 0;
}
