// Problem A
// Problem's source: Google Code Jam - Round 1B
// Program by Plamen Petrov (C) 2008
// http://digitalphysics.org/~ppetrov

#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

long long x[100100], y[100100];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    
    int t, tests;
    long long n, i, j, k, A, B, C, D, x0, y0, M, X, Y;
    long long res;
    
    cin >> tests;
    for(t=1; t<=tests; t++)
    {
        res=0;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        
        //pseudocode
        X = x0; Y = y0;
        x[0]=x0; y[0]=y0;
        //cout << X <<" " << Y << endl;
        for (i=1; i<=n-1; i++)
        {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            x[i]=X;
            y[i]=Y;
            //cout << X <<" " << Y << endl;
        }
        
        for (i=0; i<=n-1; i++)
            for (j=i+1; j<=n-1; j++)
                for (k=j+1; k<=n-1; k++)
                {
                    if(((x[i] + x[j] + x[k]) % 3 == 0) && ((y[i] + y[j] + y[k]) % 3 == 0)) res++;
                }
        
        cout << "Case #" << t << ": " << res << endl;
        
    }

    return 0;
}
