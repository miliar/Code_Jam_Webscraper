#include    <iostream>
#include    <string>
using   namespace   std;

char    c[300] = {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main ()
{   
    freopen ("gcj.in", "r", stdin);
    freopen ("gcj.out", "w", stdout);

    int casenum, N;
    string  s;
    int i=0,j;
    char    t, e;

    cin >> casenum; getline (cin, s);
    for (N=1; N<=casenum; ++N)
    {
        cout << "Case #" << N << ": ";
        getline (cin, s);
        for (i=0; i<s.length (); ++i)
            cout << c[s[i]];
        cout << endl;
    }

    return 0;
}



