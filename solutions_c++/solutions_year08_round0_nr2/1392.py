#include	<fstream>
#include	<vector>
#include	<algorithm>
#include	<cmath>
#include	<string>

using namespace	std;

ifstream	in("B-large.in");
ofstream	out("B-large.out");

short	A[26][65][102];
short	B[26][65][102];

void	func(string str, int& a, int& b)
{
	a = 10*(str[0]-'0')+(str[1]-'0');
	b = 10*(str[3]-'0')+(str[4]-'0');
}

int	main(int argc, char** argv)
{
	int	N, NA, NB, T;
	int i, j, k, l;
	int	h, m;
	int res1, res2;
	bool b;
	int q;
	int tmpA1, tmpA2, tmpB1, tmpB2;

	string	departure, arrival;

	in >> N;
	for(k = 1; k <= N; ++k)
	{
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));

		in >> T;
		in >> NA >> NB;

		for(i = 0; i < NA; ++i)
		{
			in >> departure >> arrival;
			func(departure, h, m);
			for(l = 0; A[h][m][l]; ++l);
				//nothing, see loop :)
			A[h][m][l] = 1;

			func(arrival, h, m);
			m += T;
			h += (m/60);
			m %= 60;
			for(l = 0; B[h][m][l]; ++l);
				//
			B[h][m][l] = 1;
		}
		for(i = 0; i < NB; ++i)
		{
			in >> departure >> arrival;
			func(departure, h, m);
			for(l = 0; B[h][m][l]; ++l);
				//
			B[h][m][l] = 2;

			func(arrival, h, m);
			m += T;
			h += (m/60);
			m %= 60;
			for(l = 0; A[h][m][l]; ++l);
				//
			A[h][m][l] = 2;
		}

		res1 = res2 = 0;
		q = 0;
		b = false;
		tmpA1 = tmpA2 = tmpB1 = tmpB2 = 0;

		if(NA != 0)
		{
			for(i = 0; i < 24; ++i)
			{
				for(j = 0; j < 60; ++j)
				{
					tmpA1 = 0;
					tmpA2 = 0;
					for(l = 0; A[i][j][l]; ++l)
					{
						if(A[i][j][l] == 2)
							tmpA2++;
						else if(A[i][j][l] == 1)
						{
							tmpA1++;
							/*if(q == 0)
								res1++;
							else
								q--;*/
						}
					}
					if(tmpA1 >= tmpA2)
					{
						if(tmpA2 != 0)
							tmpA1 -= tmpA2;
						if(q != 0)
						{
							if(q >= tmpA1)
							{
								q -= tmpA1;
								tmpA1 = 0;
							}
							else
							{
								tmpA1 -= q;
								q = 0;
							}
						}
						if(!q)
							res1 += tmpA1;
					}
					else if(tmpA1 < tmpA2)
					{
						if(tmpA1 != 0)
							tmpA2 -= tmpA1;
						q += tmpA2;
					}
				}
			}
		}

		q = 0;
		if(NB != 0)
		{
			for(i = 0; i < 24; ++i)
			{
				for(j = 0; j < 60; ++j)
				{
					tmpB1 = 0;
					tmpB2 = 0;
					for(l = 0; B[i][j][l]; ++l)
					{
						if(B[i][j][l] == 1)
							tmpB1++;
						else if(B[i][j][l] == 2)
						{
							tmpB2++;
							/*if(q == 0)
								res2++;
							else
								q--;*/
						}
					}
					if(tmpB2 >= tmpB1)
					{
						if(tmpB1 != 0)
							tmpB2 -= tmpB1;
						if(q != 0)
						{
							if(q >= tmpB2)
							{
								q -= tmpB2;
								tmpB2 = 0;
							}
							else
							{
								tmpB2 -= q;
								q = 0;
							}
						}
						if(!q)
							res2 += tmpB2;
					}
					else if(tmpB2 < tmpB1)
					{
						if(tmpB2 != 0)
							tmpB1 -= tmpB2;
						q += tmpB1;
					}

					//if(tmpB - q < 0)
					//{
					//	if(q != 0)
					//		tmpB -= q;
					//	res2 += tmpA;
					//}
					//else if(tmpB - q > 0)
					//{
					//	if(tmpB != 0)
					//		q -= tmpB;
					//}
				}
			}
		}
		out << "Case #" << k << ": " << res1 << ' ' << res2 << endl;
	}
	return	0;
}