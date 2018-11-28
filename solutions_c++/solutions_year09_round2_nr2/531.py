#include <iostream>
using namespace std;

int T;
string S;
int cnt[10];

void findnext();
void printnext();

int main() {
    string s;

    cin >> T;
    for (int t = 1; t <= T; t++) {
        for (int i = 0; i < 10; i++)
            cnt[i] = 0;
        cin >> S;
        S = "0" + S;

        findnext();

        cout << "Case #" << t << ": ";
        printnext();
        cout << endl;
    }

    return 0;
}

void findnext() {
    int last = -1;
    int i,j,k;

    for (i = S.length()-1; i >= 0; i--) {
        if (last != -1 && S[i]-'0' < last)
            break;
        last = S[i]-'0';
        cnt[last]++;
    }
    
    cnt[S[i]-'0']++;
    for (j = S[i]-'0'+1; j < 10; j++)
        if (cnt[j]) {
            S[i] = (char)(j+'0');
            cnt[j]--;
            break;
        }

    for (j = i+1; j < S.length(); j++)
        for (k = 0; k < 10; k++)
            if (cnt[k]) {
                S[j] = (char)(k+'0');
                cnt[k]--;
                break;
            }
}

void printnext() {
    int i = 0;
    while (S[i] == '0')
        i++;
    while (i < S.length()) {
        cout << S[i];
        i++;
    }
}
