#include <iostream>
#include <vector>
#include <string>
using namespace std;


string solve(int n, int m, vector<string>& d, string& a)
{
    int result = -1;
    string result_s;
    vector<bool> act(n);
    for (int i = 0; i < n; ++i) {
        int cresult = 0;
        int wl = (int) d[i].length();
        // Убираем все слова другой длины
        for (int j = 0; j < n; ++j) {
            act[j] = d[j].length() == wl;
        }
        // Считаем число возможных слов
        int nact = 0;
        for (int j = 0; j < n; ++j) {
            if (act[j]) {
                ++nact;
            }
        }
        for (int j = 0; j < 26; ++j) {
            bool present = false;
            // Ищем в активном словаре эту букву
            for (int k = 0; k < n; ++k) {
                if (act[k]) {
                    for (int l = 0; l < wl; ++l) {
                        if (d[k][l] == a[j]) {
                            present = true;
                        }
                    }
                }
            }
            // Если такая буква вообще есть в словаре
            if (present) {
                bool sat = false;
                vector<bool> mask(wl);
                for (int k = 0; k < wl; ++k) {
                    if (d[i][k] == a[j]) {
                        mask[k] = true;
                        sat = true;
                    }
                }
                // Если такая буква есть
                if (sat) {
                    // Убираем все слова, в которых эта буква стоит не так
                    for (int k = 0; k < n; ++k) {
                        if (act[k]) {
                            for (int l = 0; l < wl; ++l) {
                                if ((d[k][l] == a[j]) != mask[l]) {
                                    act[k] = false;
                                    --nact;
                                    break;
                                }
                            }
                        }
                    }
                } else {
                    ++cresult;
                    // Убираем все слова с такой буквой
                    for (int k = 0; k < n; ++k) {
                        if (act[k]) {
                            for (int l = 0; l < wl; ++l) {
                                if (d[k][l] == a[j]) {
                                    act[k] = false;
                                    --nact;
                                    break;
                                }
                            }
                        }
                    }
                }
                if (nact == 1) {
                    break;
                }
            }
        }
        if (cresult > result) {
            result = cresult;
            result_s = d[i];
        }
    }
    return result_s;
}


int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int n, m;
        cin >> n >> m;
        vector<string> d(n), l(m);
        for (int i = 0; i < n; ++i) {
            cin >> d[i];
        }
        for (int i = 0; i < m; ++i) {
            cin >> l[i];
        }
        cout << "Case #" << (test + 1) << ": ";
        for (int i = 0; i < m; ++i) {
            cout << solve(n, m, d, l[i]) << " ";
        }
        cout << endl;
    }
}
