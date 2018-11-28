#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define FOR(a,b,c) for(int (a)=(b);(a)<(c);(a)++)
#define sor(a) sort((a).begin(),(a).end())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    FOR(tc,1,t+1){
        cout << "Case #" << tc << ": ";
        string grid[4];
        FOR(i,0,4)
            cin >> grid[i];
        bool won=false;
        map<char,int> map;
        FOR(i,0,4){
            map.clear();
            FOR(j,0,4)
                map[grid[i][j]]++;
            if(map['X'] + map['T'] == 4){
                cout << "X won" << endl;
                won = true;
                break;
            }else if(map['O'] + map['T'] == 4){
                cout << "O won" << endl;
                won = true;
                break;
            }
        }

        if(!won){
            FOR(i,0,4){
                map.clear();
                FOR(j,0,4)
                    map[grid[j][i]]++;
                if(map['X'] + map['T'] == 4){
                    cout << "X won" << endl;
                    won = true;
                    break;
                }else if(map['O'] + map['T'] == 4){
                    cout << "O won" << endl;
                    won = true;
                    break;
                }
            }
        }
        map.clear();
        FOR(i,0,4)
            map[grid[i][i]]++;
        if(!won && map['X'] + map['T'] == 4){
                cout << "X won" << endl;
                won = true;
        }else if( !won && map['O'] + map['T'] == 4){
            cout << "O won" << endl;
            won = true;
        }
        map.clear();
        FOR(i,0,4)
            map[grid[i][3-i]]++;
        if(!won && map['X'] + map['T'] == 4){
            cout << "X won" << endl;
            won = true;
        }else if(!won && map['O'] + map['T'] == 4){
            cout << "O won" << endl;
            won = true;
        }

        bool done = true;
        FOR(i,0,4)
            FOR(j,0,4)
                if(grid[i][j]=='.')
                    done = false;

        if(done && !won )
            cout << "Draw" << endl;
        else if(!done && !won)
            cout << "Game has not completed" << endl;

    }
}
