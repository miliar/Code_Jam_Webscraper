#include <iostream>

using namespace std;

int n, m;
string a[200], b[200];


int tinh(string u, string v)
{
    int i = 0;
    while ( i < u.length() && i < v.length() && u[i] == v[i] )
        i ++;
    if ( i == u.length() )
        return 0;
    int dem = 0;
    for ( int j = i ; j < u.length() ; j ++ )
        if ( u[j] == '/' ) dem ++;
    return dem;
}

void process()
{
    if ( m == 0 )
    {
        cout << 0 << endl;
        return;
    }
    int dem = 0;
    for ( int i = 0 ; i < m ; i ++ ){
        int min = 999999999;
        for ( int j = 0 ; j < n ; j ++ )
            if ( min > tinh(b[i], a[j] ))
                min = tinh(b[i], a[j]);
        dem += min;
        a[n++] = b[i];
    }
    cout << dem << endl;
}

int test;
void load()
{
    cin >> test;
    for ( int i = 0 ; i < test ; i ++ ){
        cin >> n >> m;
        if ( n == 0 ){
            a[n++] = '/';
        }
        else {
        for ( int u = 0 ; u < n ; u ++ ){
            cin >> a[u];
            a[u] += '/';
        }
        }
        
        for ( int u = 0 ; u < m ; u ++ ){
            cin >> b[u];
            b[u] += '/';
        }
        cout << "Case #" << i + 1 << ": ";
        process();
    }
}


int main()
{
    load();
    return 0;
}
