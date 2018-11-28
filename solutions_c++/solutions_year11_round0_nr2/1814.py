#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int Maxl = 26;

int t, n;
char comb[Maxl][Maxl];
bool opp[Maxl][Maxl];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        vector <char> List;
        string s;
        fill((char*)comb, (char*)comb+Maxl*Maxl, 'A'-1);
        cin >> n;
        while (n--) {
              cin >> s;
              comb[s[0]-'A'][s[1]-'A'] = s[2];
              comb[s[1]-'A'][s[0]-'A'] = s[2];
        }
        fill((bool*)opp, (bool*)opp+Maxl*Maxl, false);
        cin >> n;
        while (n--) {
              cin >> s;
              opp[s[0]-'A'][s[1]-'A'] = opp[s[1]-'A'][s[0]-'A'] = true;
        }
        cin >> n >> s;
        for (int i = 0; i < n; i++)
           if (List.empty()) List.push_back(s[i]);
           else if (comb[s[i]-'A'][List.back()-'A'] >= 'A')
              List[List.size()-1] = comb[s[i]-'A'][List.back()-'A'];
           else {
                int j;
                for (j = 0; j < List.size(); j++)
                   if (opp[s[i]-'A'][List[j]-'A']) break;
                if (j < List.size()) List.clear();
                else List.push_back(s[i]);
           }
        cout << "Case #" << tc << ": [";
        for (int i = 0; i < List.size(); i++) {
            cout << List[i];
            if (i < List.size()-1) cout << ", ";
        }
        cout << "]\n";
    }
    return 0;
}
