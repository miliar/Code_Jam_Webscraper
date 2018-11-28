#include <iostream>
#include <vector>
using namespace std;

#define INPUT_FILE "in.txt"
#define OUTPUT_FILE "out.txt"

#define ABS(a) (a<0?-a:a)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,a,b) for(int i=(a); i<=(b); i++)
#define REP(i,n) FOR(i,0,n)
#define SZ(v) ((int)(v).size())
typedef long long ll;

int main()
{
	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
	
	int T;
    
	cin >> T;
    for (int t = 0; t < T; t++)
    {
		int R, C;
		char matrix[50][50];
        cout << "Case #" << (t+1) << ": " << endl;
		cin >> R >> C;
		REP(r,R)
		{
			REP(c,C)
			{
				cin >> matrix[r][c];
			}
		}
		int impossible = 0;
		REP(r,R)
		{
			REP(c,C)
			{
				if (matrix[r][c]=='#')
				{
					if( ((c+1)<C) && ((r+1)<R) )
					{
						if((matrix[r][c+1]=='#')&&
						   (matrix[r+1][c]=='#')&&
						   (matrix[r+1][c+1]=='#'))
						{
							matrix[r][c]='/';
							matrix[r][c+1]='\\';
							matrix[r+1][c]='\\';
							matrix[r+1][c+1]='/';
							c++;
						}
						else
						{
							impossible = 1;
						}
					}
					else
					{
						impossible = 1;
					}
				}
				if (impossible==1) break;
			}
			if(impossible==1) break;
		}
		
		if (impossible==1)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			REP(r,R)
			{
				REP(c,C)
				{
					cout << matrix[r][c];
				}
				cout << endl;
			}
		}
    }
	return 0;
}
