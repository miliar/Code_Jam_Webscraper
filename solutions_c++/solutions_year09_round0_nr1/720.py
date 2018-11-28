#include <iostream>
#include <string>

using namespace std;

char pattern[500][15][26];

int main(){
    int L, D, N;

    cin >> L >> D >> N;

    string *dict = new string[D];

    for (int i = 0; i < D; i++)
        cin >> dict[i];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < L; j++){
            char c;
            cin >> c;
            if (c == '('){
                while (true){
                    cin >> c;
                    if (c == ')')
                        break;
                    pattern[i][j][c-'a'] = 1;
                }
            } else
                pattern[i][j][c-'a'] = 1;
        }

    for (int k = 0; k < N; k++){
        int count = 0;
        for (int i = 0; i < D; i++){
            bool good = true;
            for (int j = 0; j < L; j++)
                if (!pattern[k][j][dict[i][j]-'a']){
                    good = false;
                    break;
                }
            if (good)
                ++count;
        }
        cout << "Case #" << k+1 << ": " << count << endl;
    }

    delete[] dict;
    return 0;
}
