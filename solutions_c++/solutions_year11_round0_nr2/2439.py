#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {

        // Input
        int C; cin >> C;
        vector< vector<char> > combine(200, vector<char>(200, '-'));
        for(int i = 0; i < C; ++i) {
            string s; cin >> s;
            combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
        }

        int D; cin >> D;
        vector< vector<bool> > opposed(200, vector<bool>(200, false));
        for(int i = 0; i < D; ++i) {
            string s; cin >> s;
            opposed[s[0]][s[1]] = opposed[s[1]][s[0]] = true;
        }

        int N; cin >> N;
        string s; cin >> s;

        // Computing
        vector<char> list;
        for(int i = 0; i < N; ++i) {
            if(!list.empty() && combine[list[list.size()-1]][s[i]] != '-')
                list[list.size()-1] = combine[list[list.size()-1]][s[i]];
            else {
                bool is_opposing = false;
                for(int k = 0; k < list.size(); ++k)
                    if(opposed[s[i]][list[k]])
                        is_opposing = true;

                if(is_opposing)
                    list.clear();
                else
                    list.push_back(s[i]);
            }
        }

        // Output
        cout << "Case #" << t << ": [";
        for(int i = 0; i < list.size(); ++i) {
            if(i != 0) cout << ", ";
            cout << list[i];
        }
        cout << "]" << endl;
    }

    return 0;
}
