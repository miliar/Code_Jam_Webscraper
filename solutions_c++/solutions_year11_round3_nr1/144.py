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
#define MAXN

using namespace std;

int n, m;
char A[60][60];

int main()
{
    int nTest;
    ifstream fin("A.inp");
    fin >> nTest;
    For(k, 1, nTest){
        fin >> n >> m;
        For(i, 1, n){
            For(j, 1, m){
                fin >> A[i][j];   
            }   
        }
        For(i, 1, n-1){
            For(j, 1, m-1){
                if (A[i][j] == '#' && A[i+1][j] == '#' && A[i][j+1] == '#' && A[i+1][j+1] == '#'){
                    A[i][j] = '/';
                    A[i][j+1] = '\\';
                    A[i+1][j] = '\\';
                    A[i+1][j+1] = '/';
                }   
            }   
        }
        bool done = true;
        For(i, 1, n){
            For(j, 1, m){
                if (A[i][j] == '#'){
                    done = false;   
                }
            }      
        }
        cout << "Case #" << k << ":" << endl;
        if (!done){
            cout << "Impossible" << endl;   
        }else{
            For(i, 1, n){
                For(j, 1, m){
                    cout << A[i][j];   
                }   
                cout << endl;
            }   
        }
    }
    fin.close();
   // system("pause");
    return 0;
}

