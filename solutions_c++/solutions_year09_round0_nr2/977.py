#include <iostream>
#include <deque>
#include <utility>
using namespace std;

const int MAX = 100000000;
int map[102][102];
int t;
int h, w;
char out[102][102];
int mark[102][102];

int X[4] = {0, 1, 0, -1}; // E, S, W, N
int Y[4] = {1, 0, -1, 0};

void solve() {
    deque<pair<int,int> > dq;

    char current = 'a';
    for (int ii = 1; ii <= h; ii++)
    {
        for (int jj = 1; jj <= w; jj++) {
            
            if (mark[ii][jj]) continue;
            mark[ii][jj] = 1;
            dq.push_back(make_pair(ii, jj));
            while (!dq.empty())
            {
                int x = dq[0].first, y = dq[0].second;
                for (int i = 0; i < 4; i++)
                {
                    int xx = x + X[i];
                    int yy = y + Y[i];
                    
                                        
                    if (mark[xx][yy]) continue;
                    if (map[xx][yy] == MAX) continue;
                    
                    if (map[xx][yy] > map[x][y])
                    {
                        int flag = 0;
                        for (int j = 0; j < 4; j++)
                        {
                            if (map[xx + X[j]][yy + Y[j]] < map[x][y])
                            {
                                flag = 1; break;
                            }    
                        }    
                        if (!flag) {
                            if (i == 0) {
                                if (map[xx - 1][yy] > map[x][y]) dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            } else if (i == 1) {
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            } else if (i == 2) {
                                if (map[xx - 1][yy] > map[x][y] && map[xx][yy - 1] > map[x][y])
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            }    
                             else {
                               if (map[xx - 1][yy] > map[x][y] && map[xx][yy - 1] > map[x][y]
                                && map[xx][yy + 1] > map[x][y])
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            }  
                        }                
                    }  else if (map[xx][yy] < map[x][y]) {
                        int flag = 0;
                        for (int j = 0; j < 4; j++)
                        {
                            if (map[xx][yy] > map[x + X[j]][y + Y[j]])
                            {
                                flag = 1; break;
                            }    
                        }    
                        if (!flag)
                        {
                            if (i == 0) {
                                if (map[xx][yy] < map[x][y - 1] && map[xx][yy] < map[x - 1][y]) dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            } else if (i == 1) {
                                if (map[xx][yy] < map[x][y - 1] && map[xx][yy] < map[x - 1][y]
                                && map[xx][yy] < map[x][y + 1])
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            } else if (i == 2) {
                                if (map[xx][yy] < map[x - 1][y])
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            }    
                             else {
                                dq.push_back(make_pair(xx, yy)), mark[xx][yy] = 1;
                            } 
                        }    
                    }  
                    //cout << dq[dq.size() - 1].first << " " << dq[dq.size() - 1].second << endl;    
                } 
                //cout << dq.size() << endl;
                out[x][y] = current;
                dq.pop_front();   
            }   
            current++; 
        }
    }        
}    

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    int testcase = 1;
    while (t--)
    {
        memset(out, 0, sizeof(out));
        memset(mark, 0, sizeof(mark));
        for (int i = 0; i < 102; i++)
        {
            for (int j = 0; j < 102; j++)
            {
                map[i][j] = MAX;
            }    
        }   
        cin >> h >> w;
        for (int i = 1; i <= h; i++)
        {
            for (int j = 1; j <= w; j++)
            {
                cin >> map[i][j];
            }    
        }    
        solve();
        cout << "Case #" << testcase++ << ":" << endl; 
        for (int i = 1; i <= h; i++)
        {
            for (int j = 1; j < w; j++)
            {
                cout << out[i][j] << " ";
            }    
            cout << out[i][w] << endl;
        }        
    } 
       
}    
