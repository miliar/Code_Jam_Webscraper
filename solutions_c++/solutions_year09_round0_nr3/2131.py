#include<iostream>
#include<fstream>
#include<vector>
#include<string>
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

#define M 19
#define MAX 1000

int main()
{
	int nCase,N;
	ifstream ifs( "C-large.in" );
	ofstream ofs( "C-large-out.txt" );

	char str[MAX];
	char wel[] ={"welcome to code jam"};

	ifs>>nCase;
	ifs.getline(str, MAX);//get a enter.
	for (int iCase = 0; iCase < nCase; iCase++ )
	{
		ifs.getline(str, MAX);
		N = strlen(str);
		int **mat = array<int>( M + 1, N + 1 );
		//initialize mat
		for (int i = 0; i <= N; i++ )
			mat[0][i] = 1;
		for (int i = 1; i <= M; i++ )
		{
			for (int j = 1; j <= N; j++ )
			{
				if ( wel[i-1] == str[j-1] )
				{
					mat[i][j] = mat[i-1][j] + mat[i][j-1];
					mat[i][j] %= 10000;
				}
				else
					mat[i][j] = mat[i][j-1];
			}
		}
		if ( mat[M][N]< 10)
			ofs<<"Case #"<<iCase+1<<": 000"<<mat[M][N]<<endl;
		else if ( mat[M][N]< 100)
			ofs<<"Case #"<<iCase+1<<": 00"<<mat[M][N]<<endl;
		else if ( mat[M][N]< 1000)
			ofs<<"Case #"<<iCase+1<<": 0"<<mat[M][N]<<endl;
		else
			ofs<<"Case #"<<iCase+1<<": "<<mat[M][N]<<endl;
		printf("%d,",mat[M][N]);

		freearray(mat);
	}
	
	ifs.close();
	ofs.close();

	return 0;
}    