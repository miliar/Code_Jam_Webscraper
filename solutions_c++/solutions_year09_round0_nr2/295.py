// eddie s.j. du
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <list>
#include <sstream>
#include <map>
#include <queue>

#define ui unsigned int
#define ll long long
#define ul unsigned long
#define ull unsigned long long
#define fore(i,a,b) for(int i=(a),__b=(b);i<__b;i++)
#define rep(i,a) fore(i,0,a)
#define repo(i,a) for(int i=(1),__b=(a);i<=__b;i++)
#define pb push_back

using namespace std;

//c style
//FILE *fin = fopen("cowxor.in", "r");

//c++ style

    //ofstream fout ("gift1.out");
    ifstream fin ("B-large.in");


int main () {
    // c style
    freopen ("B-large.out","w",stdout);
    // ie int n; fscanf (fin,"%d",&n);

    // constants
    const int NORTH = 0;
    const int WEST = 1;
    const int EAST = 2;
    const int SOUTH = 3;
    const int HELL = 4;
    const int COMPLETE = 5;

    int dir [4] = {NORTH,WEST,EAST,SOUTH};
    int dx [4] = {0,-1,1,0};
    int dy [4] = {-1,0,0,1};

    int cas;
    fin >> cas;
    rep(casNo,cas){
        int height, width;
        fin >> height >> width;
        int mp [height+2][width+2];
        int txt [height+2][width+2];
        char res [height+2][width+2];

        rep(i,height+2) {mp[i][0]=-1;mp[i][width+1]=-1;}
        rep(j,width+2) {mp[0][j]=-1;mp[height+1][j]=-1;}

        repo(i,height) repo(j,width) {
            fin >> mp[i][j];
            res[i][j] = '?';
        }

        int min;
        repo(i,height) repo(j,width) {
            txt[i][j] = HELL;
            min = mp[i][j];
            rep(k,4) if (mp[i+dy[k]][j+dx[k]] >= 0){
                 if (min > mp[i+dy[k]][j+dx[k]]) {
                     min = mp[i+dy[k]][j+dx[k]];
                     txt[i][j] = k;
                 }
            }
        }

        char nextLabel = 'a';
        int nextY, nextX, tNextY, tNextX;
        pair <int,int> nextPair;
        repo(i,height) repo(j,width) if (res[i][j] == '?') {
            list < pair <int,int> > ls;
            ls.pb (make_pair(i,j));

            // flood down -> 1 way down
            nextY = i; nextX = j;
            while (txt[nextY][nextX] != HELL) {
                tNextY = nextY + dy[txt[nextY][nextX]];
                tNextX = nextX + dx[txt[nextY][nextX]];
                nextY = tNextY;
                nextX = tNextX;
                //cout << nextY << " " << nextX <<endl;
                                                    assert (res[nextY][nextX]=='?');
                ls.pb (make_pair(nextY,nextX));
            }

            // flood up -> many (single) ways up
            while (!ls.empty()) {
                nextPair = ls.front(); ls.pop_front();
                if (res[nextPair.first][nextPair.second]!='?') continue;
                res[nextPair.first][nextPair.second] = nextLabel;
                rep(k,4) {
                    if(mp[nextPair.first+dy[k]][nextPair.second+dx[k]] >= 0) {
                        bool good = false;
                        switch(k) {
                         case NORTH: if (txt[nextPair.first+dy[k]][nextPair.second+dx[k]]==SOUTH) good = true; break;
                         case SOUTH: if (txt[nextPair.first+dy[k]][nextPair.second+dx[k]]==NORTH) good = true; break;
                         case EAST: if (txt[nextPair.first+dy[k]][nextPair.second+dx[k]]==WEST) good = true; break;
                         case WEST: if (txt[nextPair.first+dy[k]][nextPair.second+dx[k]]==EAST) good = true; break;
                        }
                        if (good && res[nextPair.first+dy[k]][nextPair.second+dx[k]]=='?') {
                         ls.pb (make_pair(nextPair.first+dy[k],nextPair.second+dx[k]));
                        }
                    }
                }
            }
            nextLabel ++;
        }

        cout << "Case #"<<casNo+1<<":"<<endl;
        repo(i,height) {
            repo(j,width-1) {
                cout << res[i][j] << " ";
            }
            cout << res[i][width] << endl;
        }
    }
    return 0;
}
