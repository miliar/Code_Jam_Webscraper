#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    vector<string> SE;
    string str;
    int i, j, S, Q, kase;
    cin >> kase;
    int flag[110];
    for(i = 1; i <= kase; i++){
        cin >> S;
        getline(cin, str);
        SE.clear();
        for(j = 0; j < S; j++){
            getline(cin, str);
            SE.push_back(str);
        }
        cin >> Q;
        getline(cin, str);
        memset(flag, 0, sizeof(flag));
        int ans = 0;
        int left = S, tmp = -1;
        for(j = 0; j < Q; j++){
            getline(cin, str);
            int k = find(SE.begin(), SE.end(), str) - SE.begin();
            if(flag[k] == 0) { 
                if(left == 1){
                    ++ans;
                    memset(flag, 0, sizeof(flag));
                    flag[k] = 1;
                    left = S - 1;
                }
                else{
                    flag[k] = 1; 
                    left--;
                }
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    //system("pause");
    return 0;
}
