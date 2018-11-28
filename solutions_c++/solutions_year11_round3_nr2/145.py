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
#define fi first
#define se second
#define MAXN 1000100

using namespace std;

double A[MAXN];
long long L, t, n, C;

long long cp()
{
    double time = 0;
    int i = 0;
    while (i <= n-1 && time < t){
        time += A[i]*2;
        i++;
    }

    A[n] = (time - t)/2.0;
    time = time - A[n]*2.0;
    sort(A+i, A+n+1);
    ForL(j, n, i){
        if (L > 0){
            time += A[j];
            L--;   
        }else{   
            time += A[j]*2;
        }
    }
    return round(time);
}

int main()
{
    int nTest;
    int temp;
    int x;
    ifstream fin("B.inp");
    fin >> nTest;
    For(k, 1, nTest){
        memset(A, 0, sizeof(A));
        fin >> L >> t >> n >> C;
        For(i, 0, C-1){
            fin >> x;   
            temp = 0;
            while (1){
                if (temp*C+i+1 > n){
                    break;    
                }
                A[temp*C+i] = x;
                temp++;
            }
        }
        cout << "Case #" << k << ": " << cp() << endl;
    }
    fin.close();
   // system("pause");
    return 0;
}

