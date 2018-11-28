
#include <iostream>
#include <vector>
#include <map>
#include <cstring>

//#define debug

using namespace std;

int main() {
    
    int N;
    cin >> N;

    char *match = "welcome to code jam";
    int m_l = strlen(match);

    int where[m_l];
    int w_l;

    char c[600];
        cin.getline(c, 600);

    for (int i = 0; i < N; i++) {
        int result = 0;
        cin.getline(c, 600);
        int l = strlen(c);
        map <int, int> matches;
        for (int k = 0; k < m_l; k++)
            matches[k] = 0;

        for (int j = 0; j < l; j++) {
            w_l = 0;
            for (int k = 0; k < m_l; k++)
                if (match[k] == c[j]) {
                    where[w_l] = k;
                    w_l++;
                }

            #ifdef debug
            cerr << "j: "<<  j << " c[j]: " << c[j] << endl;
            for (int j = 0; j < w_l; j++)
                cerr << "\twhere[" << j << "] : " << where[j] << endl;
            #endif

            for (int k = 0; k < w_l; k++) {
                if (where[k] == 0)
                    matches[where[k]]++;
                else
                    matches[where[k]] = (matches[where[k]-1]+matches[where[k]])%100000;
            }
        }
//        for (int j = 0; j < matches.size(); j++)
//                result += matches[j];

        #ifdef debug
        cerr << "matches: " << endl;
        for (int j = 0; j < m_l; j++)
            cerr << "matches[" << j << "] : " << matches[j] << endl;
        #endif
        result = matches[m_l-1];
        result %= 10000;
//        cout << "Case #" << i+1 << ": ";
        printf("Case #%d: %04d\n",i+1, result);
    }

    return 0;
}
