
#include <iostream>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

//#define debug

inline long long int pow(int base, int power) {
    long long int ret = base;
    if (power == 0)
        return 1;
    for (int i = 1; i < power; i++)
        ret *= (long long int)base;
    return ret;
}


int main() {

    unsigned int N;
    cin >> N;

    long long int result = 0;
    char c[64];
    for (int u = 0; u < N; u++) {
        result = 0;

        cin >> c;
        // counts distinct nums...
        vector <char> marks;
        for (int i = 0; i < strlen(c); i++) {
            bool found = false;
            for (int j = 0; j < marks.size(); j++)
                if (marks[j] == c[i]) {
                    found = true;
                    break;
                }
            if (!found)
                marks.push_back(c[i]);          
            
        }

        int base = marks.size();

        if (base == 1)
            base = 2;
        
        map <char, int> dict;
        for (int i = 0; i < base; i++)
            dict[marks[i]] = -1;
        

        #ifdef debug
        cerr << " base = " << base << endl;
        #endif

        int last_used = -1;
        for (int i = 0; i < strlen(c); i++) {

            #ifdef debug
            cerr << "i = " << i << " c[i] : " << c[i] << " dict[c[i]] = " << dict[c[i]]<< endl;
            #endif
            if (dict[c[i]] == -1) {
                if (i == 0)
                    dict[c[i]] = 1;
                else {
                    if (last_used == 0) last_used++;
                    dict[c[i]] = ++last_used;
                }
            }
            #ifdef debug
            cerr << "i = " << i << " c[i] : " << c[i] << " dict[c[i]] = " << dict[c[i]]<< endl;
            #endif


            result += ((long long int) dict[c[i]]) * pow(base, strlen(c) - i - 1);

            #ifdef debug
            cerr << " pow = " << pow(base, strlen(c) -i - 1) << endl << endl;
            #endif

            
        }
        
        cout << "Case #" << u+1 << ": " << result << endl;
    }

    return 0;
}
