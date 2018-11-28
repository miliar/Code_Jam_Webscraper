#include <iostream>
#include <string>
#include <vector>

using namespace std;

main() {
    int l, d, n, teste = 1;

    cin >> l >> d >> n;
    vector<string> words;

    for (int i = 0; i < d; i++) {
        string temp;
        cin >> temp;
        words.push_back(temp);
    }


    for (int i = 0; i < n; i++) {
        vector<string> pattern;

        string temp;
        cin >> temp;
        
        int num = 0;

        for (int j = 0; j < temp.size(); j++) {
            string s;
            char str[2];

            if (temp[j] == '(') {
                j++;
                while (temp[j] != ')') {
                    str[0] = temp[j++];
                    str[1] = '\0';
                    s.append(string(str));
                }

            } else {
                str[0] = temp[j];
                str[1] = '\0';
                s.append(string(str));
            }

            pattern.push_back(s);
        }

        vector<string> w;

        for (int j = 0; j < words.size(); j++) {
            bool ok = true;

            for (int k = 0; k < words[j].size(); k++) {
                if (pattern[k].find(words[j][k]) == string::npos) {
                    ok = false;
                    break;
                }
            }

            if (ok) num++;
        }

        cout << "Case #" << teste++ << ": " << num << endl;
    }
}
