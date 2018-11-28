#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");


#define cin fin
#define cout fout


int n;
int H, L;
int a[20000];

bool can(int x)
{
    for (int i = 1; i <= n; ++i )
        if ( (a[i]%x) && (x%a[i]) ) return false;
    return true;
}


int work()
{
    cin >> n >> L >> H;
    for (int i = 1; i <= n; ++i )
        cin >> a[i];
    for (int i = L; i <= H; ++i)
        if (can(i)) return i;
    return 0;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t )
    {
        cout << "Case #" << t << ": ";
        int tmp = work();
        if (tmp)
            cout << tmp << endl;
        else 
            cout << "NO" << endl;
    }
}
