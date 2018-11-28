#include <iostream>

using namespace std;


struct Pair
{
    int x;
    int y;
    
    Pair(int a, int b)
    {
        x = a;
        y = b;
    }
    
    Pair()
    {
    }
};

Pair f[10000];
int test, n;

bool cat(Pair a, Pair b)
{
    if ( a.x <= b.x && a.y <= b.y ) return false;
    if ( a.x >= b.x && a.y >= b.y ) return false;
    return true;
}

void process()
{
    int dem = 0;
    for ( int i = 0 ; i < n ; i ++ )
        for ( int j = i + 1 ; j < n ; j ++ ){
            if (cat(f[i], f[j]))
                dem ++; 
        }
    cout << dem << endl;
}

void load()
{
    
    cin >> test;
    for ( int i = 0 ; i < test ; i ++ ){
        cin >> n;
        int a, b;
        for ( int j = 0 ; j < n ; j ++ ){
            cin >> a >> b;
            Pair temp(a, b);
            f[j] = temp;
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
