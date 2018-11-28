#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <utility>

#define pb push_back


using namespace std;

int main() {
    int t, r, c;
    string s[51];
    cin >> t;
    for(int w=1; w<=t; w++) {
        cin >> r >> c;
        for(int i=0; i<r; i++)
            cin >> s[i];

        bool flag = true;
        for(int i=0;i<r && flag;i++) {
            for(int j=0; j<c && flag; j++) {
                if(s[i][j] == '#') {
                    if(s[i+1][j] == '#' && s[i+1][j+1] == '#' && s[i][j+1] == '#') {
                        s[i][j] = '/';
                        s[i+1][j] ='\\';
                        s[i+1][j+1] = '/';
                        s[i][j+1] = '\\';
                    } else {
                        flag = false;
                    }
                }
            }
        }

        cout << "Case #" << w << ":\n";
        if(flag) {
            for(int i=0;i<r;i++)
                cout << s[i] << "\n";
        } else
            cout << "Impossible\n";
    }
}
