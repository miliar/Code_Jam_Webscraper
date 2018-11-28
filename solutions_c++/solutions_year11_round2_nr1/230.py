#include <iostream>
#include <cassert>
#include <iomanip>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int n;
    char results[105][105];
    int wins[105];
    int against[105];
    double wp[105];
    double owp[105];
    double oowp[105];
    double rpi[105];


    for (coden = 1; coden <= t; coden++)
    {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> results[i];
        }
        // results[i][j] == '1' means team #i win against team #j
        
        for (int i = 0; i < n; i++) {
            wins[i] = 0;
            against[i] = 0;
            for (int j = 0; j < n; j++) {
                if (results[i][j] == '1') {
                    ++wins[i];
                    ++against[i];
                } else if (results[i][j] == '0') {
                    ++against[i];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            wp[i] = double(wins[i]) / against[i];
            cerr << "wp[" << i << "] = " << wp[i] << endl;
        }

        for (int i = 0; i < n; i++) {
            double sum = 0;
            int count = 0;
            for (int j = 0; j < n; j++) {
                // if #i against #j
                // sum += wp of j without counting i which = (wins[j] - (#i wins #j?0:1)) / (against[j] - 1)
                // ++count
                if (results[i][j] != '.') {
                    int winnum = wins[j] - ((results[i][j] == '1') ? 0 : 1);
                    sum += double(winnum) / (against[j] - 1);
                    ++count;
                }
            }
            owp[i] = sum / count;
            cerr << "owp[" << i << "] = " << owp[i] << endl;
        }

        for (int i = 0; i < n; i++) {
            double sum = 0;
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (results[i][j] != '.') {
                    sum += owp[j];
                    ++count;
                }
            }
            oowp[i] = sum / count;
            rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        }



        // output result
        cout << "Case #" << coden << ":" << endl;
        for (int i = 0; i < n; i++) {
            cout << setprecision(10) << rpi[i] << endl;
        }
    }
    return 0;
}

