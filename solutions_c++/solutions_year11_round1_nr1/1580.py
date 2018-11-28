#include<iostream>
using namespace std;

int ca = 2;
void minuses(int &a, int &b)
{
    while((a%ca != 0 || b%ca != 0) && ca <= 100)
        ca++;
    a/=ca; 
    b/=ca;
}
/*
void muti(int &a, int &b, int n)
{
    int c = n/a + 1;
    a *= c;
    b *= c;
}
*/

bool doit(int n, int d, int g)
{
    int md = 100, mg = 100;
    int ld = d;
    while (md > n && ca <= 100)
        minuses(ld, md);
    if (ca > 100)
        return false;
    if (d != 100 & g == 100)
        return false;
    if (d != 0 && g == 0)
        return false;
    return true;
}

int main()
{
    int t, r;
    cin >> t;
    for (r = 0; r < t; r++) {
        int n, d, g;
        cin >> n >> d >> g;
        cout << "Case #" << r+1 << ": ";
        if (doit(n, d, g))
            cout << "Possible\n";
        else
            cout << "Broken\n";
        ca = 2;
    }
    return 0;
}
