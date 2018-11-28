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
#define MAXN 30

using namespace std;

int n, nC, nD, nT;
int C[30][30], D[30][30];
int Res[150];
int nR;

int canCombined(int i, int j){
    return C[i][j];
}

bool isOpposed()
{
    int i = Res[nR];
    For(k, 1, nR-1){
        int j = Res[k];
        if (D[i][j] == 1){
            return true;   
        }   
    }   
    return false;
}


int main()
{
    string s;
    int u, v, t, nS, temp;
    cin >> nT;
    For(k, 1, nT){
        cin >> nC;
        // init
        nR = 0;
        memset(C, 0, sizeof(C));
        memset(D, 0, sizeof(D));
        For(i, 1, nC){
            cin >> s;   
            u = s[0] - 'A';
            v = s[1] - 'A';
            t = s[2] - 'A';
            C[u][v] = t;
            C[v][u] = t;
        }   
        cin >> nD;
        For(i, 1, nD){
            cin >> s;   
            u = s[0] - 'A';
            v = s[1] - 'A';
            D[u][v] = 1;
            D[v][u] = 1;
        }   
        cin >> n >> s;
        nS = s.length();
        For(i, 0, nS-1){
            nR++;
            Res[nR] = s[i] - 'A';
            if (nR >= 2){
                temp = canCombined(Res[nR-1], Res[nR]);
                if (temp != 0){
                    nR--;
                    Res[nR] = temp;   
                }
                if (nR >= 2 && isOpposed()){
                    nR = 0;
                }
            }
        }
        cout << "Case #" << k << ": [";
        For(i, 1, nR){
            cout << char(Res[i]+'A');
            if (i < nR)
               cout << ", ";   
        }
        cout << "]";
        if (k < nT)
            cout << endl;
    }
    //system("pause");
    return 0;
}

