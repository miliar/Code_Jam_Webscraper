#include <fstream>
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int c[101][1001];
string search_engine[101];
string queries[1001];
int N, S, Q;
int solution;

int min( int a, int b ) { return ( a < b ? a : b ); }

int main()
{
	int loop, i, j, k;
	string str;
	ifstream in("a.in");
	FILE *fo = fopen("a.out", "w");
	in >> N;
	for (loop = 1; loop <= N; loop ++ )
    {
		in >> S; getline(in, str);
		for (i=1; i<=S; i++)
			getline(in, search_engine[i]);
		in >> Q; getline(in, str);
		for (i=1; i<=Q; i++)
			getline(in, queries[i]);
		solution = 100000;
		for (i=1; i<=S; i++)
		{
			for (j=1; j<=Q; j++) c[i][j] = 100000;
			c[i][0] = 0;
		}      
		for (j=1; j<=Q; j++)
			for (i=1; i<=S; i++)
			{
				if (search_engine[i] != queries[j])
				{
					c[i][j] = c[i][j-1];
					for (k=1; k<=S; k++)
						if (k != i)
							c[i][j] = min(c[i][j], c[k][j-1]+1);
				}
			}
		for (i=1; i<=S; i++)
			solution = min(solution, c[i][Q]);
		fprintf(fo, "Case #%d: %d\n", loop, solution);
    }
	in.close();
	fclose(fo);
	return 0;
}
