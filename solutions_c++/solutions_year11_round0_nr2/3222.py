#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
        int total = 0;
        cin >> total;
        for (int i = 1; i <= total; ++i) {
                char rules[256][256] = {0};
                memset(rules, 0, sizeof(rules));
                for (int j = 0; j < 256; ++j) {
                        for (int k = 0; k < 256; ++k) {
                                rules[j][k] = '\0';
                        }
                }
                int comb = 0;
                cin >> comb;
                for (int j = 0; j < comb; ++j) {
                        string r;
                        cin >> r;
                        char a = r[0], b = r[1], c = r[2];
                        rules[a][b] = c;
                        rules[b][a] = c;
                }
                int oppo = 0;
                cin >> oppo;
                unsigned int op[27][27] = {0};
                memset(op, 0, sizeof(op));
                for (int j = 0; j < oppo; ++j) {
                        string r;
                        cin >> r;
                        char a = r[0], b = r[1];
                        op[a - 'A'][b - 'A'] = 1;
                        op[b - 'A'][a - 'A'] = 1;
                }
                int len = 0;
                cin >> len;
                string result = "";
                int lcount[27] = {0};
                memset(lcount, 0, sizeof(lcount));
                for (int j = 0; j < len; ++j) {
                        char temp = '\0';
                        cin >> temp;
                        //for (char m = 'A'; m <= 'Z'; ++m) { cout << lcount[m-'A'] << ",";} cout << endl;
                        if (result.length() <= 0) {
                                if (temp != '\0') {
                                        result += temp;
                                        lcount[temp - 'A']++;
                                }
                        }
                        else {
                                while (result.length() > 0) {
                                        char top = result[result.length() - 1];
                                        if (rules[top][temp] != '\0'){
                                                result = result.substr(0, result.length() - 1);
                                                lcount[top - 'A']--;
                                                temp = rules[top][temp];
                                        }
                                        else {
                                                bool clear = false;
                                                for (char k = 0; !clear && k < 27; k++) {
                                                        if(op[temp - 'A'][k] != 0 && lcount[k] > 0)
                                                                clear = true;
                                                        //cout << "check " << char(temp) << "," << char(k + 'A') << " " << clear << endl;
                                                }
                                                if (clear){
                                                        result = "";
                                                        temp = '\0';
                                                        memset(lcount, 0, sizeof(lcount));
                                                }
                                                break;
                                        }
                                }
                                if (temp != '\0') {
                                        result += temp;
                                        lcount[temp - 'A']++;
                                }
                        }
                }
                cout << "Case #" << i << ": [";
                for (int j = 0; j < result.length(); ++j)  {
                        if (j > 0) cout << ", ";
                        cout << result[j];
                }
                cout << "]" << endl;
        }

        return 0;
}
