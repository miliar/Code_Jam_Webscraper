#include <iostream>
#include <string>
#include <sstream>

using namespace std;

/*
int u[][] = {
    {
        // 3‚ÅŠ„‚Á‚Ä‚ ‚Ü‚è‚ª0‚Ì‚Æ‚«
        { 0, 0, 0}
        {-1, 0, 1}
    },
    {
        // 3‚ÅŠ„‚Á‚Ä‚ ‚Ü‚è‚ª1‚Ì‚Æ‚«
        {0, 1, 0},
        {-1, 1, 1}, # useless
    },
    {
        // 3‚ÅŠ„‚Á‚Ä‚ ‚Ü‚è‚ª2‚Ì‚Æ‚«
        {1, 0, 1},
        {0, 2, 0},
    }
    
};
*/

int main() {
    int T;
    cin >> T;
    string dummy;std::getline(cin, dummy);
    for(int i = 0; i < T; i++ ) {
        int N, S, p;
        cin >> N >> S >> p;
        cerr << N << "," << S << "," << p << " ";

        int result = 0;
        for(int j = 0 ; j < N ; j++) {
            int t;
            cin >> t;
            switch(t%3) {
                case 0:
                    {
                        if (p <= t/3) {
                            cerr << "0 ";
                            result++;
                        } else if(1 <= S && 1 <= t/3 && t/3 == p-1) {
                            cerr << "0* ";
                            S--;
                            result++;
                        }
                    }
                    break;
                case 1:
                    {
                        if (p-1 <= t/3) {
                            cerr << "1 ";
                            result++;
                        }
                    }
                    break;
                case 2:
                    {
                        if (p-1 <= t/3) {
                            cerr << "2 ";
                            result++;
                        } else if(1 <= S && t/3  == p-2) {
                            cerr << "2* ";
                            S--;
                            result++;
                        }
                    }
                    break;
            }
        }
        cerr << endl;
        cout << "Case #" << (i+1) << ": " << result << endl;
    }
}
