#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int L, D, N, n;
    cin >> L >> D >> N;
    vector<string> words;
    n = N;
    while(D--) {
        string t;
        cin >> t;
        words.push_back(t);
    }
    while(N--) {
        string p;
        cin >> p;
        vector<int> w;
        vector<int> ww;
        vector<int>::iterator k;
        int i = 0, j = 0;
        for (i = 0; i < words.size(); i++)
            w.push_back(i);

        bool par = false;
        for (i = 0; i < p.size(); i++) {
            if (j >= L) {
                w.clear();
                break;
            }
            switch(p[i]) {
                case '(':
                    par = true;
                    continue;
                case ')':
                    par = false;
                    j++;
                    w = ww;
                    ww.clear();
                    continue;
                default:
                    if (par) {
                        for (k = w.begin(); k != w.end();)
                            if (words[*k][j] == p[i]) {
                                ww.push_back(*k);
                                k = w.erase(k);
                            } else {
                                k++;
                            }
                    } else {
                        for (k = w.begin(); k != w.end();)
                            if (words[(*k)][j] != p[i])
                                k = w.erase(k);
                            else
                                k++;
                        j++;
                    }
            }
        }
        cout << "Case #" << n-N << ": " << w.size() << endl;
    }
    return 0;
}








