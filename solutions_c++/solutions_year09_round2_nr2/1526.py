#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#define For(i,a,b) for(i=a;i<b;i++)
#define Forto(i,n) For(i,0,n)

using namespace std;

int num[10];

int vtoi(int * str, int vsize) {
    int i;
    int num =0;
    Forto(i, vsize) {
        num += str[i] * (int)pow(10.0, vsize-i-1);
    }
    return num;
}

int solveCase(int * str, int vsize, int n) {
  do {
    int next = vtoi(str, vsize);
    if (next > n) return next;
  } while ( next_permutation (str,str+vsize) );

  for (int i=vsize-1; i >= 0; i--)
    str[i+1] = str[i];
  str[0]=0;
  return solveCase(str, vsize+1, n);
}

int main()
{
    int T, Case = 1;
    int next;
    long long n;
    int i,j,k;
    int str[100] = {3, 2, 4};

    cin >> T;

    while (T--) {

        cin >> n;

        Forto(i, 9) num[i] = 0;

        char tmp[100];
        itoa(n, tmp, 10);
        int vsize=strlen(tmp);
        Forto(i, vsize) {
            str[i] = tmp[i] - '0';
            num[str[i]]++;
        }

        next = solveCase(str, vsize, n);

        cout << "Case #" << Case++ << ": " << next << endl;
    }

    return 0;
}
