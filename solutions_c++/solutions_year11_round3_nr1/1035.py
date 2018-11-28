#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int R, C;
char a[100][100];

#define cin fin
#define cout fout

bool work()
{
    cin >> R >> C;
    for (int i = 0; i < R; ++i )
        cin >> a[i];
    for (int i = 0; i < R; ++i )
        for (int j = 0; j < C; ++j )
            if (a[i][j]=='#')
            {
                if (a[i][j+1]!='#') return false;
                if (a[i+1][j]!='#') return false;
                if (a[i+1][j+1]!='#') return false;
                a[i][j] = a[i+1][j+1] = '/';
                a[i+1][j] = a[i][j+1] = '\\';
            }
    return true;     
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t )
    {
        cout << "Case #" << t << ": " << endl;
        if ( work() )
        {
            for (int i = 0; i < R; ++i )
                cout << a[i] << endl;
        }
        else 
            cout << "Impossible" << endl;
    }
}
