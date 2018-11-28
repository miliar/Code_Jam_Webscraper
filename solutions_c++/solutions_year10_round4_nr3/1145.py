#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    int T; 
    int X1, X2, Y1, Y2;
    
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int answer = 0;
        int count = 0;
        int R;
        cin >> R;
//        cout << R << "\t";
        vector < vector <int> > table(101, vector<int>(101,0));
        for (int r = 0; r < R; ++r) {
            cin >> X1 >> Y1 >> X2 >> Y2;
            for (int i = X1; i <= X2; ++i)
                for (int j = Y1; j <= Y2; ++j) {
                    if (table[i][j] != 1) {
                        table[i][j] = 1;
                        ++count;
                    }
                }
        }

        while (count>0) {
            for (int i = 100; i>0; --i)
                for (int j = 100; j>0; --j) {
                    int current = table[i][j];
                    if(table[i-1][j] == table[i][j-1])
                        table[i][j] = table[i-1][j];
                    count += table[i][j] - current;
                }
            ++answer;
        }
        cout << "Case #" << t << ": " << answer << endl;
    }
    
    return 0;
}
