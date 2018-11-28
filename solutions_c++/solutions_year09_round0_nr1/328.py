#include <iostream>
#include <vector>

using namespace std;



int main() {
    int len, wordn, cases;
    cin >> len >> wordn >> cases;

    vector<string> words;
    for(int i=0; i<wordn; i++) {
        string w;
        cin >> w;
        words.push_back(w);
    
    }

    for(int c=0; c<cases; c++) {
        string ptn;
        cin >> ptn;
        vector<int> p;
        int pos =0;
        while(pos < ptn.size()) {
            int m = 0;
            if (ptn[pos] == '(') {
                pos++;
                while(ptn[pos] != ')') {
                    m |= (1<<(ptn[pos]-'a'));
                    pos++;
                }
            }
            else { m |= (1<<(ptn[pos]-'a')); }
            pos++;
            p.push_back(m);
        }
        
        if (p.size() != len) cout << "ERROR!"<<endl;
        int ans=0;
        for(int w=0; w<words.size(); w++) {
            bool good = true;
            string word = words[w];
            for(int i=0; i<p.size(); i++) {
                if ((p[i] & (1<<(word[i]-'a'))) == 0) { good = false; break; }
            }
            if (good) ans++;
        }

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
