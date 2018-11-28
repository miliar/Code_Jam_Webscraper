#include<iostream>
#include<string>

using namespace std;

bool match(int* a, const string& word, int L) {
    for(int i=0; i<L; i++) {
        if((a[i] & (1 << (word[i] - 'a'))) == 0) return false;
    }
    return true;
}

int main() {
    int L, D, N;
    cin >> L >> D >> N;

    string word[5000];
    for(int i=0; i<D; i++) cin >> word[i];

    for(int i=1; i<=N; i++) {
        string input;
        cin >> input;

        int a[16] = {0};
        for(int j=0, k=0; j<L; j++, k++) {
            if(input[k] == '(') {
                k++;
                while(input[k] != ')') {
                    a[j] |= (1 << (input[k] - 'a'));
                    k++;
                }
            }
            else {
                a[j] = (1 << (input[k] - 'a'));
            }
        }

        int total = 0;
        for(int j=0; j<D; j++) {
            if(match(a, word[j], L)) total++;
        }

        cout << "Case #" << i << ": " << total << endl;
    }
}

