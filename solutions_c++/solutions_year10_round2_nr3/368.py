#include <iostream>
#include <vector>
using namespace std;

int fib[600] = {0};

void calc()
{
    fib[0] = 1; fib[1] = 2;
    for ( int i = 2; i < 520; ++i )
        fib[i] = (fib[i-1] + fib[i-2])%100003;
}

bool verify( vector<int> v )
{
    //cout << "v: ";
    //for ( int i = 0; i < v.size(); ++i ) cout << v[i] << " ";
    //cout << endl;
    
    int pos = v.size();
    while ( pos != 1 )
    {
        //cout << pos << " ";
        
        int n = pos;
        bool found = false;
        for ( int i = 0; i < v.size(); ++i )
            if ( v[i] == n)
            {
                found = true;
                pos = i+1;
            }
            else if ( v[i] > n )
                break;
        
        if ( !found ) break;
    }
    if ( pos == 1 ) return true;
    return false;
}

int subset(int n)
{
    int resp = 0;
    for (int i = 1<<(n-2); i < 1<<(n-1); ++i)
    {
        //cout << i << endl;
        vector<int> v;
        for (int j = 0; j < n; ++j)
            if ( i & 1<<j )
                v.push_back( j+2 );
        
        if ( verify(v) )
            ++resp;
    }
    return resp;
}

int main()
{
    calc();
    
    for (int i = 2; i < 26; ++i)
    {
        int x = subset( i );
        fib[i-2] = x%100003;
        //cout << "x: " << x << endl;
    }
    
    //return 0;
    
    
    int t; cin >> t;
    for (int caso = 0; caso < t; ++caso)
    {
        int n;
        cin >> n;
        cout << "Case #" << caso+1 << ": " << fib[n-2] << endl;
    }
}
