#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;

void solve(int);

int main()
{
    int total_cases;
    cin >> total_cases;
    cin.get();

    for (int i = 0; i < total_cases; i++)
        solve(i+1);

    return 0;
}

void solve(int ncase)
{
    int N;
    cin >> N;
    cin.get();

    int M[40][40];
    int last_one[40];
    memset(M, 0, sizeof(M));
    memset(last_one, -1, sizeof(last_one));

    for (int i = 0; i < N; i++) {
        string line;
        //cin.getline(line, N);
        cin >> line;
        cin.get();
        for (int j = 0; j < N; j++) {
            M[i][j] = line[j] - '0';
        }
        last_one[i] = line.rfind('1');
        //cout << i << ":" << last_one[i]<< endl; 
    }

    int ret = 0;
    for (int i = 0; i < N; i++) {
        if (last_one[i] > i) {
            //cout << "Searching alterntive for " << i << ":" << endl;
            int row = -1;
            for (int j = i+1; j < N; j++) {
                if (last_one[j] <= i) {
                    row = j;
                    break;
                }
            }
            if (row > 0) {
               // cout << row << endl;
                int temp = last_one[row];
                for (int j = row; j > i; j--) {
                    last_one[j] = last_one[j-1];
                }
                last_one[i] = temp;
                ret += row - i;
            }
        }
    }

    cout << "Case #" << ncase << ": " << ret << endl;
    return;
}
