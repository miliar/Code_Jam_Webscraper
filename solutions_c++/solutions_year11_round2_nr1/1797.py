#include <iostream>
#include <string>

using namespace std;

string pole[100];
double wp[100], owp[100], oowp[100], sum[100], count[100];

int main() {
        int t;
        cin >> t;
        for (int test = 1; test <= t; test++) {
                for (int i = 0; i < 100; i++)
                        sum[i] = count[i] = wp[i] = owp[i] = oowp[i] = 0;
                int n;
                cin >> n;
                for (int i = 0; i < n; i++) {
                        cin >> pole[i];
                        for (int j = 0; j < pole[i].length(); j++)
                                if (pole[i][j] != '.') {
                                        if (pole[i][j] == '1')
                                                sum[i]++;
                                        count[i]++;
                                }
                        wp[i] = sum[i] / count[i];
                }
                for (int i = 0; i < n; i++) {
                        double sumr = 0, cont = 0;
                        for (int j = 0; j < n; j++)
                                if (i != j)
                                        if (pole[i][j] != '.') {
                                                sumr += (sum[j] - (pole[j][i] - '0')) /  (count[j] - 1);
                                                cont++;
                                        } 
                        owp[i] = sumr / cont;
                }
                for (int i = 0; i < n; i++) {
                        double sumr = 0;
                        for (int j = 0; j < n; j++)
                                if (i != j)
                                        if (pole[i][j] != '.')
                                                sumr += owp[j];
                        oowp[i] = sumr / count[i];
                }
                cout << "Case #" << test << ":" << endl;
                for (int i = 0; i < n; i++) {
                        cout << 0.2500000 * wp[i] + 0.5000000 * owp[i] + 0.25000000000 * oowp[i] << endl;
                }
        }
}
