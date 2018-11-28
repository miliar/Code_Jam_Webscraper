#include <iostream>
#include <fstream>
using namespace std;

long gcd( long a, long b )
{
    long temp;
    if ( a < b )
    {
        temp = a;
        a = b;
        b = temp;
    }
    while( a%b )
    {
        temp = a;
        a = b;
        b = temp%b;
    }
    return b;
}

int main()
{
    ifstream cin("B-small-attempt0 (1).in");
	ofstream cout("B-small-attempt0 (1).out");

    int C;
    cin >> C;
    int cnt = 1;

    long N;
    long a[3];
    long result;
    long min;
    long tg;
    long tempa;
    while(C--)
    {
        cin >> N;
        for(int i = 0; i < N; i++)
            cin >> a[i];

        min = a[0];
        for(int i = 1; i < N; i++)
            if( min > a[i] ) min = a[i];

        for(int i = 0; i < N; i++)
            a[i] -= min;

        for(int i = 0; i < N; i++)
            if( a[i] > 0 )
            {
                tg = a[i];
                break;
            }

        for(int i = 0; i < N; i++)
            if( a[i] > 0 )
            {
                tg = gcd(a[i], tg);
            }

        tempa = a[0] + min;
        if( tempa % tg == 0 )result = 0;
        else result = tg - tempa % tg;

        cout << "Case #" << cnt++ << ": " ;
        cout << result << endl;
    }

    cin.close();
    cin.close();
    return 0;
}
