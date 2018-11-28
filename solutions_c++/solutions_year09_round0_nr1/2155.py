#include <iostream>
#include <fstream>
#include<cstring>
using	namespace	std;
const	int		maxd = 5000 + 10;
const	int		maxn = 500 + 10;
const	int		maxl = 15 + 10;

int		L, D, N;
char	w[maxd][maxl];
char	pt[maxn][maxl][26];
string	tmp;

int		main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> L >> D >> N;
    for( int i = 0; i < D; i ++ ) cin >> w[i];
    for( int i = 0; i < N; i ++ )
    {
        cin >> tmp;
        int	len = tmp.length(), st = 0, kh = 0;
        for( int j = 0; j < len; j ++ )
        {
            if( tmp[j] == '(' ) kh = 1;
            else if( tmp[j] == ')' ) {kh = 0; st ++;}
            else
            {
                pt[i][st][tmp[j] - 'a'] = 1;
                if( kh == 0 ) st ++;
            }    
        }
    }
    for( int i = 0; i < N; i ++ )
    {
        int		ans = 0;
        for( int j = 0; j < D; j ++ )
        {
            int		ok = true;
            for( int k = 0; k < L; k ++ )
                if( !pt[i][k][w[j][k] - 'a'] )
                {
                    ok = false;
                    break;
                }
            if( ok ) ans ++;
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
