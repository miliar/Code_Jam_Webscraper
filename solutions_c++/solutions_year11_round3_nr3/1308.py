#include <stdio.h>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
bool primo[10000];
vector <int> primos;
int npri[10000][10000];
int M[10000];
int freq[10000];
bool ok,ooka;
bool isInt (double f)
{
    return (f-(int)f) < 1e-9;
}
int main (void)
{
    int n,caso, i,j,k, ncaso,l,h;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> ncaso;
    memset (primo, 0, sizeof(primo));
    memset (npri,0,sizeof(npri));
    memset (M, 0, sizeof(M));
//    for (i = 2; i < 10000; i++)
//    {
//        if (!primo[i])
//        {
//            primos.push_back(i);
//            for (j = i; j < 10000; j += i)
//                primo[j] = true;
//        }
//    }
    for (caso = 1; caso <= ncaso; caso++)
    {
        cin>>n>>l>>h;
        for (i = 0; i < n; i++)
        {
            cin >> freq[i];
        }
        ok = true;
        for (j = l; j <= h; j++)
        {
            ooka = true;
//            cout << "j:" << j << endl;
            for (i = 0; ooka && i < n; i++)
            {
//                cout <<"OK" <<  ooka << " ";
                if (!(isInt((double)j/(double)freq[i])||isInt((double)freq[i]/(double)j)))
                    ooka = false;
            }
//            cout << "ok:" << ooka << " ";
            if (ooka)
                break;
        }
        printf ("Case #%d: ",caso);
        if (!ok || j > h)   cout <<"NO\n";
        else    cout << j << endl;


    }
    return 0;
}
