#include <iostream>
#include <map>
#include <vector>

using namespace std;

int a[110][110];
int drain[110][110];
int rows, cols;
int sinks;

int dr[] = { -1, 0, 0, 1 };
int dc[] = { 0, -1, 1, 0};

int go(int r, int c) {
    if (drain[r][c] != -1) return drain[r][c];

    int lo = a[r][c];
    int best = -1;
    for(int d=0; d<4; d++) {
        int nr=r + dr[d];
        int nc=c + dc[d];
        if (nr>=0 && nc>=0 && nr<rows && nc<cols ) {
            if (a[nr][nc] < lo) {
                best = d;
                lo = a[nr][nc];
            }
        }
    }

    int sink;
    if (best != -1) { sink = go(r+dr[best], c+dc[best]); }
    else { sink = sinks++; }

    return drain[r][c] = sink;
}

int main() {
    int cases;
    cin >> cases;

    for(int cs=0; cs<cases; cs++) {
        cin >> rows >> cols;
        sinks = 0;

        vector<pair<int, pair<int,int> > > pts;
        for(int r=0;r<rows;r++) for(int c=0;c<cols;c++) {
            int hg;
            cin >> hg; a[r][c] = hg;
            pts.push_back(make_pair(-hg, make_pair(r,c)));
        }
        sort(pts.begin(), pts.end());

        memset(drain,-1,sizeof(drain));
        for(int i=0; i<pts.size(); i++) {
            int r = pts[i].second.first;
            int c = pts[i].second.second;
            go(r, c);
        }

        char nextch='a';
        map<int,char> ind;

        cout << "Case #" <<(cs+1)<<":"<<endl;
        for(int r=0;r<rows;r++) {
            for(int c=0;c<cols;c++) {
                if(c)cout<<" ";

                if (drain[r][c] == -1) cout << "BAD"<<endl;
                if (!ind.count(drain[r][c])) ind[drain[r][c]] = nextch++;
                cout << ind[drain[r][c]];
            }

            cout << endl;
        }
    }
}
