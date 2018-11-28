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
#define MAXN 110

using namespace std;

int n, L, R;
int A[MAXN];

int main()
{
    int nTest;
    ifstream fin("C.inp");
    fin >> nTest;
    For(k, 1, nTest){
        fin >> n >> L >> R;
        For(i, 1, n){
            fin >> A[i];
        }
        int result = 0;   
        bool ok;
        For(i, L, R){
            ok = true;
            For(j, 1, n){
                if (i % A[j] != 0 && A[j]%i != 0){
                    ok = false;
                    break;   
                }
            }
            if (ok){
                result = i;
                break;   
            }
        }
        if (result == 0)
            cout << "Case #" << k << ": NO" << endl;
        else
            cout << "Case #" << k << ": " << result << endl;
    }
    fin.close();
    //system("pause");
    return 0;
}

