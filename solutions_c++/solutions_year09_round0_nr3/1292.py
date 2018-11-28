#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
    int N;
    cin >> N;
    cin.get();

    string T[100];
    for (int i = 0; i < N; i++)
        getline(cin, T[i]);

    string pattern = "welcome to code jam";
    int size = pattern.size();
    for (int i = 0; i < N; i++) {
        vector <int> P[27];
        for (int j = 0; j < T[i].size(); j++) {
            if (T[i][j] == ' ') P[26].push_back(j);
            else P[T[i][j]-'a'].push_back(j);
        }

        int C[500][19];
        memset(C, 0, sizeof(C));
        for (int k = 0; k < P['m'-'a'].size(); k++)
            C[P['m'-'a'][k]][18] = 1;

        for (int j = size-2; j >= 0; j--) {
            int n = pattern[j] - 'a';
            if (pattern[j] == ' ') n = 26;

            for (int k = 0; k < P[n].size(); k++) {
                int m = pattern[j+1] - 'a';
                if (pattern[j+1] == ' ') m = 26;
                for (int q = 0; q < P[m].size(); q++) if (P[m][q] > P[n][k]) {
                    C[P[n][k]][j] += C[P[m][q]][j+1];
                    C[P[n][k]][j] %= 10000;
                }
            }
        }

        int result = 0;
        for (int k = 0; k < P['w'-'a'].size(); k++)
            result = (result + C[P['w'-'a'][k]][0]) % 10000;

        printf("Case #%d: %04d\n", i+1, result);
    }

    return 0;
}
