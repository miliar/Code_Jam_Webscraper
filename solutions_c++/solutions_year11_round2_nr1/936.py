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

int nTest, n;
char A[MAXN][MAXN];
double W[MAXN], L[MAXN], WP[MAXN], OWP[MAXN], OOWP[MAXN];

double cp_percentage(double w, double l)
{
    return w/(w+l);   
}

void cp_wp()
{
    memset(W, 0, sizeof(W));
    memset(L, 0, sizeof(L));
    For(i, 1, n){
        For(j, 1, n){
            if (A[i][j] == '1')
                W[i]++;
            else if (A[i][j] == '0')
                L[i]++;   
        }
        WP[i] = cp_percentage(W[i], L[i]);
    }
}



void cp_owp()
{
    double sum;
    double count;
    memset(OWP, 0, sizeof(OWP));
    For(i, 1, n){
        sum = 0;
        count = 0;
        For(j, 1, n){
            if (A[i][j] != '.'){
                count++;
                if (A[i][j] == '1')
                    sum += cp_percentage(W[j], L[j]-1);
                else
                    sum += cp_percentage(W[j]-1, L[j]);
            }   
        }
        OWP[i] = sum/count;
                
    }
    
}

void cp_oowp()
{
    memset(OOWP, 0, sizeof(OOWP));
    int count;
    For(i, 1, n){
        count = 0;
        For(j, 1, n){
            if (A[i][j] != '.'){
                OOWP[i] += OWP[j];
                count++;
            }
        }
        OOWP[i] /= count;
       
    }
}


int main()
{
    cin >> nTest;
    For(k, 1, nTest){
        cin >> n;
        For(i, 1, n){
            For(j, 1, n){
                cin >> A[i][j];   
            }   
        }
        cp_wp();
        cp_owp();
        cp_oowp();
        cout << "Case #" << k << ":" << endl;
        For(i, 1, n){
            cout << 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] << endl;
        }
    }
 //   system("pause");
    return 0;
}

