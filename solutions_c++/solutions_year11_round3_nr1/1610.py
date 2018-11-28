#include <assert.h>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class A
{
public:
    bool Solve()
    {
        for (unsigned int i = 0; i < boardM.size(); i++) {
            for (unsigned int j = 0; j < boardM[i].length(); j++) {
                if (boardM[i][j] == '#') {
                    if (i + 1 < boardM.size()) {
                        if (j + 1 < boardM[0].length()) {
                            if (boardM[i + 1][j] == '#' &&
                                boardM[i + 1][j + 1] == '#' &&
                                boardM[i][j + 1] == '#') {
                                boardM[i][j] = '/';
                                boardM[i][j + 1] = '\\';
                                boardM[i + 1][j + 1] = '/';
                                boardM[i + 1][j] = '\\';
                            }
                            else {
                                return false;
                            }
                        }
                        else {
                            return false;
                        }
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        
        for (unsigned int i = 0; i <boardM.size(); i++) {
            for (unsigned int j = 0; j < boardM[i].length(); j++) {
                if (boardM[i][j] == '#') {
                    return false;
                }
            }
        }
        
        return true;
    }

    void Start()
    {
        int T = 0;
        cin >> T;
        
        for (int t = 0; t < T; t++) {
            int R = 0;
            cin >> R;
            int C = 0;
            cin >> C;
            boardM.resize(R);
            for (int r = 0; r < R; r++)
            {
                cin >> boardM[r];
            }

            cout << "Case #" << (t + 1) << ":\n";
            if (!this->Solve()) {
                cout << "Impossible\n";
            }
            else {
                for (unsigned int i = 0; i < boardM.size(); i++) {
                    cout << boardM[i] << "\n";
                }
            }
        }
    }
    
private:
    vector<string> boardM;
};

int main(int argc, const char *argv[])
{
    A g;
    g.Start();
    return 0;
}
