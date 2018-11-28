#include <iostream>
#include <queue>
#include <vector>
#include <map>

using namespace std;

int dr[] = {-1,0,1,0,0};
int dc[] = {0,-1,0,1,0};

string m[15];
int rows, cols;

bool cvis[15][15];
bool cbox[15][15];

int conngo(int r, int c) {
    if (r<0 || c<0 || r>=rows || c>=cols || cvis[r][c] || !cbox[r][c]) return 0;
    cvis[r][c] = 1;
    return 1 + conngo(r+1,c) + conngo(r-1,c) + conngo(r,c+1) + conngo(r, c-1);
}

int conn(vector<pair<int,int> > v) {
    memset(cvis,0,sizeof(cvis));
    memset(cbox,0,sizeof(cbox));

    for(int i=0; i<v.size(); i++) cbox[v[i].first][v[i].second] = 1;

    return conngo(v[0].first, v[0].second);
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        cin >> rows >> cols;

        for(int i=0; i<rows; i++) cin >> m[i];

        vector<pair<int,int> > boxes;
        vector<pair<int,int> > tgt;
        for(int i=0; i<rows; i++) for(int j=0;j<cols;j++) {
            if (m[i][j] == 'w' || m[i][j] == 'o') boxes.push_back(make_pair(i,j));
            if(m[i][j] == 'w' || m[i][j]=='x') tgt.push_back(make_pair(i,j));
        }

        sort(boxes.begin(), boxes.end());
        sort(tgt.begin(), tgt.end());

        map<vector<pair<int,int> >, int > dist;
        queue<vector<pair<int,int> > > q;
        dist[boxes] = 0;
        q.push(boxes);

        while(!q.empty()) {
            vector<pair<int,int> > cur = q.front();
            int curdist = dist[cur];
            q.pop();

            //for(int i=0; i<cur.size(); i++) cout << cur[i].first<<","<<cur[i].second<<" "; cout<<endl;
            /*
            cout<<"DIST="<<curdist<<endl;
            vector<string> temp(rows);
            for(int i=0; i<rows; i++) temp[i] = string(cols, '.');
            for(int i=0; i<rows; i++) for(int j=0; j<cols; j++) if(m[i][j] == '#') temp[i][j] = '#';
            for(int i=0; i<cur.size(); i++) temp[cur[i].first][cur[i].second] = 'O';
            for(int i=0; i<temp.size(); i++) cout << temp[i]<<endl;
            cout<<endl;
            */

            if (cur == tgt) break;

            for(int b=0; b<cur.size(); b++) {
                for(int d=0; d<4; d++) {
                    vector<pair<int,int> > cur2 = cur;
                    int nr = cur[b].first + dr[d];
                    int nc = cur[b].second + dc[d];
                    cur2[b].first = nr;
                    cur2[b].second = nc;
                    if (nr < 0 || nc < 0 || nr>=rows || nc >= cols || m[nr][nc] == '#') continue;
                    int onr = cur[b].first - dr[d];
                    int onc = cur[b].second - dc[d];
                    if (onr < 0 || onc < 0 || onr>=rows || onc >= cols || m[onr][onc] == '#' || find(cur.begin(), cur.end(), make_pair(onr,onc)) != cur.end()) continue;

                    if ((conn(cur)==cur.size()) || (conn(cur2)==cur.size())) {
                        sort(cur2.begin(), cur2.end());
                        bool good = 1;
                        for(int i=0; i+1<cur2.size(); i++) if (cur2[i] == cur2[i+1]) good = 0;
                        if (good && dist.count(cur2) == 0) {
                            dist[cur2] = curdist + 1;
                            q.push(cur2);
                        }
                    }
                }
            }
        }
        int ans = dist.count(tgt) == 0 ? -1 : dist[tgt];

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
