#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int n, m;
vector< pair<int, int> > lina[1000];
int main(){
    int T, k, x, y;
    ifstream cin("B-small-attempt0.in");
    ofstream cout("out.txt");
    cin >> T;
    for(int t = 1; t <= T; ++ t){
        cin >> n >> m;
        for(int i = 0; i < m; ++ i){
            lina[i].clear();
            cin >> k;
            while (k--){
                cin >> x >> y;
                lina[i].push_back(make_pair(x, y));
            }
        }
        int ans;
        int minmalted = n + 1;
        for(int d = 0; d < (1 << n); ++ d){
            int malted = 0, td = d;
            for(int i = 0; i < n; ++ i){
                malted += td % 2;
                td /= 2;
            }
            //if (d == 1) cout << "hoh" << endl;
            bool ok;
            for(int i = 0; i < m; ++ i){
                ok = false;
                for(vector< pair<int, int> >::iterator it = lina[i].begin(); it != lina[i].end(); ++ it)
                    if ((d >> (it->first - 1)) % 2 == it->second){
                        //cout << it->first << ' ' << it->second << endl;
                        ok = true;
                        break;
                    }
                if (!ok) break;
            }
            if (ok){
                if (malted < minmalted){
                    minmalted = malted;
                    ans = d;
                }
            }
        }
        if (minmalted == n + 1)
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else{
            cout << "Case #" << t << ":";
            for(int i = 0; i < n; ++ i){
                cout << ' ' << ans % 2;
                ans /= 2;
            }
            cout << endl;
        }
    }
    return 0;
}
