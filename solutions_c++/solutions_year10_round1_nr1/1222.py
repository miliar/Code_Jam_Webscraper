
// (c) Alvaro Salmador 2010

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N=0,K=0;

class Matrix {
public:
	Matrix(int n) : _N(n) {
		_mat = new char [_N*_N+5];
	}

	inline char& a(int x, int y)
	{
		return _mat[y*_N+x];
	}

	void print() 
	{
		for(int j=0; j<_N; ++j)
		{
			for(int i=0; i<_N; ++i)
				fputc(a(i,j), stderr);
			fputc('\n', stderr);
		}
	}

	bool isWinner(char wc, int K)
	{
		int count,j,i;
		for(j=0; j<_N; ++j) {
			count=0;
			for(i=0; i<_N; ++i) {
				if (a(i,j)==wc) {
					if (++count>=K)
						return true;
				} else count=0;

			}
		}

		for(int j=0; j<_N; ++j) {
			count=0;
			for(int i=0; i<_N; ++i) {
				if (a(j,i)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
			}
		}

		/*for(int j=0; j<_N; ++j)
		{
			count=0;
			for(int i=0; i<_N && i+j<_N; ++i)
				if (a(i+j,i)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}
		for(int j=0; j<_N; ++j)
		{
			count=0;
			for(int i=0; i<_N && i+j<_N; ++i)
				if (a(i,i+j)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}*/

		for(int j=0; j<_N; ++j)
		{
			count=0;
			for(int ij=0; j+ij<_N; ++ij)
				if (a(ij,j+ij)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}
		for(int i=0; i<_N; ++i)
		{
			count=0;
			for(int ij=0; j+ij<_N; ++ij)
				if (a(i+ij,ij)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}

		for(int j=0; j<_N; ++j)
		{
			count=0;
			for(int ij=0; j+ij<_N; ++ij)
				if (a( _N-1-ij, j+ij)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}
		for(int i=0; i<_N; ++i)
		{
			count=0;
			for(int ij=0; j+ij<_N; ++ij)
				if (a( N-1-(i+ij), ij)==wc) { 
					if (++count>=K)
						return true;
				}
				else count=0;
		}

		return false;
	}

	~Matrix()
	{
		delete [] _mat;
	}

	char* _mat;

private:
	int _N;
	Matrix() {}
};

Matrix* matrix = NULL;

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d %d", &N, &K)!=2)
			return false;

		matrix = new Matrix(N);

		while(fgetc(stdin)!='\n') ;

		int i;
		for(i=0; i<N; ++i)
		{
			fgets((matrix->_mat)+(i*N), 55, stdin);
		}

		return true;
	}
	else
		return false;
}

#define A(xxx,yyy) matrix->a(xxx,yyy)

int main()
{
	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		for(int j=0; j<N; ++j)
		{
			int i;

			int k=N-1;
			for(i=N-1; i>=0; --i)
			{
				if (A(i,j)!='.' && i!=k)
				{
					A(k--,j)=A(i,j);
					A(i,j)='.';
				}
				else 
					if (A(i,j)!='.') 
						k--;
			}
		}

		bool winB = matrix->isWinner('B', K);
		bool winR = matrix->isWinner('R', K);

		if (winB && winR)
			printf("Both\n");
		else if (winB)
			printf("Blue\n");
		else if (winR)
			printf("Red\n");
		else
			printf("Neither\n");

		//fprintf(stderr, "\n");
		//matrix->print();

		delete matrix;
	}

	return 0;
}