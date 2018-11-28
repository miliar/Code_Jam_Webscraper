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

#define fin  "B.IN"
#define fout "B.OUT"

int T;
char desc[100], buff[100];

int main()
{
	int t, i, j, rem;

	ifstream f1(fin);
	ofstream f2(fout);

	f1 >> T;

	for ( t = 1; t <= T; ++t )
	{
		f1 >> buff;

		j = 0;
		for ( i = strlen(buff) - 1; i >= 0; --i )
			desc[ ++j ] = buff[i] - '0';
		desc[0] = j;

		for ( i = desc[0] + 1; i > 2; --i )
		{
			for ( j = i - 1; j > 1 && desc[j] >= desc[j - 1]; --j );

			if ( j == 1 )
				break;
		}
		//cout << N << endl;
		f2 << "Case #" << t << ": ";

		if ( i == desc[0] + 1 )
		{
			sort(&desc[1],&desc[ desc[0] ]);
			
			for ( j = 1; desc[j] == 0; ++j );
			f2 << (char)(desc[ j ] + '0') << "0";
			for ( i = 1; i <= desc[0]; ++i )
				if ( i != j ) 
					f2 << (char)(desc[i] + '0');
			f2 << endl;
		}
		else
		{
			for ( j = desc[0]; j > i; --j )
				f2 << (char)(desc[j] + '0');
			rem = desc[i];
			sort(&desc[1],&desc[i + 1]);
			for ( j = i; j > 0 && desc[j] > rem; --j );
			if ( j < i )
				f2 << (char)(desc[j+1] + '0'), rem = j + 1;
			else
				f2 << (char)(rem + '0'), rem = j;
			for ( j = 1; j <= i; ++j )
				if ( j != rem )
					f2 << (char)(desc[j] + '0');
			f2 << endl;
		}
	}

	return 0;
}