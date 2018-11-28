#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int k;
string s;
int perm[5];

int score (string& news) {
    int g = 0;
    char c = -1;

    for (int i = 0; i < news.size(); ++i) {
        if (news[i] != c)
            ++g;
        c = news[i];
    }

    return g;
}

int perm_score () {
    string news(s);
    for (int i = 0; i < s.size(); i += k) {
        for (int j = 0; j < k; ++j) {
            news[i+j] = s[i+perm[j]];
        }
    }

    return score(news);
}

int main () {
    int N;
    cin >> N;


    for (int cas = 1; cas <= N; ++cas) {
        cin >> k;
        cin >> s;
       
        for (int i = 0; i < k; ++i) {
            perm[i] = i;
        }

        int ming = 50001;
        
        do {
            ming = min(ming, perm_score());
        } while (next_permutation(perm, perm+k));

        cout << "Case #" << cas << ": " << ming << endl;
    }
}
