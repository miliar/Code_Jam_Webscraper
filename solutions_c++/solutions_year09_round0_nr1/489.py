#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(c) (int)((c).size())
#define f first
#define s second

#define fin  "A.IN"
#define fout "A.OUT"

char txt[5010][17], buff[1000000];
char cuv[16][26];

int L, D, N;

int main()
{
	int i, j, k, id, cnt;

	ifstream f1(fin);
	ofstream f2(fout);

	f1 >> L >> D >> N;
	for ( i = 0; i < D; ++i )
		f1 >> txt[i];
	
	for ( i = 0; i < N; ++i )
	{
		f1 >> buff;
		id = 0;
		memset(cuv,0,sizeof(cuv));
		for ( j = 0; j < strlen(buff); ++j )
			if ( buff[j] == '(' )
			{
				for ( ++j; buff[j] != ')'; ++j )
					cuv[ id ][ buff[j] - 'a' ] = 1;
				++id;
			}
			else
				cuv[ id++ ][ buff[j] - 'a' ] = 1;

		char flag = 1;

		cnt = 0;

		for ( j = 0; j < D; ++j )
		{
			flag = 1;
			for ( k = 0; k < L; ++k )
				if ( !cuv[ k ][ txt[j][k] - 'a' ] )
					flag = 0;
			if ( flag ) 
				++cnt;
		}

		f2 << "Case #" << i + 1 << ": " << cnt << endl;
	}

	return 0;
}