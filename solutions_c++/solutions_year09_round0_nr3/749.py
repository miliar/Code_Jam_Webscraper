#include <iostream>
#include <cstring>

using namespace std;

int m[501][19];

const char P[] = "welcome to code jam";
const int p = 19;

char T[501];
int t;

int solve(int i, int j){
    if (i >= t || j >= p)
        return 0;

    if (m[i][j] != -1)
        return m[i][j];

    if (j == p-1){
        int count = 0;
        for (int k = i; k < t; k++)
            if (T[k] == P[j])
                count++;
        m[i][j] = count;
        return count;
    }

    if (T[i] == P[j])
        m[i][j] = (solve(i+1, j+1) + solve(i+1, j))%10000;
    else
        m[i][j] = solve(i+1, j)%10000;
    return m[i][j];
}

int main(){
    int N;
    cin >> N;
    cin.getline(T, 501); //skip first newline

    for (int n = 0; n < N; n++){
        cin.getline(T, 501);
        t = cin.gcount();

        memset(m, -1, sizeof(m));
        int res = solve(0, 0);
        cout << "Case #" << n+1 << ": ";

        if (res < 1000) cout << "0";
        if (res < 100) cout << "0";
        if (res < 10) cout << "0";
        cout << res << endl;
    }

    return 0;
}
