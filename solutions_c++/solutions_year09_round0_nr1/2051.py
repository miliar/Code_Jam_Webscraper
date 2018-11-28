#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

template < class T>
T** array(int m, int n)
{
	T **p;
	p = (T**)malloc(m*sizeof(T*));
	p[0] = (T*)malloc(m*n*sizeof(T));
	if ( p[0] == NULL )
	{
		cout<<"error."<<endl;
	}
	memset(p[0],0,m*n*sizeof(T));
	for (int i=1; i<m; ++i)
		p[i]=p[i-1]+n;
	return p;
}

template < class T>
void freearray(T** p)
{
	free(*p); free(p);
}

int main()
{
	int L,D,N;
	ifstream ifs( "A-large.in" );
	ofstream ofs( "A-large-out.txt" );

	ifs>>L>>D>>N;
	char ch;
	char **letter = array<char>(D,L);
	for (int i = 0; i < D; i++ )
	{
		for (int j = 0; j < L; j++ )
		{
			ifs>>letter[i][j];
		}
	}
	for (int i = 0; i< N; i++ )
	{
		int **pattern = array<int>(N,26);
		for (int j = 0; j < L; j++ )
		{
			ifs>>ch;
			if (ch!='(')
			{
				pattern[j][ch-'a'] = 1;
			}
			else
			{
				while ( (ch = ifs.get()) != ')' )
				{
					pattern[j][ch-'a'] = 1;
				}
			}
		}
		int number = 0;
		for (int m = 0; m < D; m++ )
		{
			int match = 1;
			for (int n = 0; n < L; n++ )
			{
				match *= pattern[n][ letter[m][n] - 'a' ];
				if (match == 0)	break;
			}
			number += match;
		}
		freearray(pattern);
		ofs<<"Case #"<<i+1<<": "<<number<<endl;
	}
	ifs.close();
	ofs.close();

	return 0;
}    