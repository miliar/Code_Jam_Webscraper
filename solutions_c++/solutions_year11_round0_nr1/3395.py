#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#define For(i, a, b) for(int i = a; i <= b; i++)
#define ForL(i, a, b) for(int i = a; i >= b; i--)
#define pb push_back
#define MAXN

using namespace std;

int main()
{
    int nT, n, x;
    int cO, cB, time, pO, pB, temp;
    string s;
    cin >> nT;
    For(i, 1, nT){
        cin >> n;
        cO = 1; pO = 0;
        cB = 1; pB = 0;
        time = 0;
        For(i, 1, n){
            cin >> s >> x;
            if (s == "B"){   
                pB = abs(x - cB) - pB;
                if (pB < 0) pB = 0;
                cB = x;
                pO += pB + 1;
                time += pB + 1;
                pB = 0;
            }
            else{
                pO = abs(x-cO) - pO;
                if (pO < 0) pO = 0;
                cO = x;
                pB += pO + 1;
                time += pO + 1;
                pO = 0;
            }                      
        }
        cout << "Case #" << i << ": " << time;
        if (i < nT)
            cout << endl;
    }
   // system("pause");
    return 0;
}

