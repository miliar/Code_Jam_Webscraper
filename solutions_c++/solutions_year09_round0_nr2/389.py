#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int avail;
map<int,char> mapeo;

vector<vector<int> > board;
vector<vector<int> > res;


int mx[] = {0, 0, -1, +1, 0};
int my[] = {0, -1, 0, 0, +1};

int solve (int x, int y) {
    vector<pair<int,int> > nei;
    pair<int, int> n;
    if (res[y][x] != 0)
        return res[y][x];
    if (y>0) {n.first=board[y-1][x];n.second=1;nei.push_back (n);}
    if (x>0) {n.first=board[y][x-1];n.second=2;nei.push_back (n);}
    if (x<board[0].size()-1) {n.first=board[y][x+1];n.second=3;nei.push_back (n);}
    if (y<board.size()-1) {n.first=board[y+1][x];n.second=4;nei.push_back (n);}

    if (nei.size() == 0) return res[y][x] = 1;

    sort (nei.begin(),nei.end());

    if (nei[0].first >= board[y][x]) { return res[y][x] = avail++; }

    return res[y][x] = solve(x+mx[nei[0].second], y+my[nei[0].second]);
}

int main () {
    int T;
    int counter = 1;
    cin >> T;
    while (T--) {
        int W, H;
        cin >> H >> W;
        mapeo.clear();
        avail = 1;
        vector<vector<int> > b(H,vector<int>(W,0));
        res = b;
        for (int i = 0; i < W*H; i++)
            scanf("%d", &b[i/W][i%W]);
        board = b;
        for (int i = 0; i < W*H; i++)
            solve(i%W,i/W);
        char current = 'a';
        cout << "Case #" << counter++ <<":" <<endl;
        for (int i = 0; i < W*H; i++) {
            if (mapeo.find(res[i/W][i%W]) == mapeo.end())
                mapeo[res[i/W][i%W]] = current++;
            cout << mapeo[res[i/W][i%W]];
            if ((i+1)%W == 0) cout << "\n";
                         else cout << " ";
        }
    }
    return 0;
}

