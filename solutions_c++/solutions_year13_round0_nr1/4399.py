#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <utility>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <complex>
#include <string>
#include <sstream>

using namespace std;

#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define rep(i,n) for(int i=0;i<(n);i++)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); \
                                                  it != container.end(); ++it)
#define mp(a,b) make_pair((a),(b))
#define eq ==

typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> pii;

// →↑←↓
const int dx[] = {1,0,-1,0};
const int dy[] = {0,-1,0,1};


const double EPS = 1e-9;

enum Game{
    XWIN,OWIN,DRAW,ING
};
int main(){
    int T;
    cin >> T;

    for(int i=1;i<=T;i++){
        Game G = DRAW;
        vector<string> field(4);
        for(int j=0;j<4;j++){
            cin >> field[j];
        }
        for(int isO=false;isO<=true;isO++){
            char c = isO ? 'O':'X';
            for(int row=0;row<4;row++){
                int OXCount=0,TCount=0;
                for(int column=0;column<4;column++){
                    if(field[row][column] == c) OXCount++;
                    else if(field[row][column] == 'T') TCount++;
                }
                if(OXCount == 4 or (OXCount == 3 and TCount == 1)){
                    if(isO){
                        G = OWIN;
                    }else{
                        G = XWIN;
                    }
                    goto end;
                }
            }

            for(int row=0;row<4;row++){
                int OXCount=0,TCount=0;
                for(int column=0;column<4;column++){
                    if(field[column][row] == c) OXCount++;
                    else if(field[column][row] == 'T') TCount++;
                }
                if(OXCount == 4 or (OXCount == 3 and TCount == 1)){
                    if(isO){
                        G = OWIN;
                    }else{
                        G = XWIN;
                    }
                    goto end;
                }
            }
            {
                int OXCount=0,TCount=0;
                for(int rc=0;rc<4;rc++){
                    if(field[rc][rc] == c) OXCount++;
                    else if(field[rc][rc] == 'T') TCount++;
                }
                if(OXCount == 4 or (OXCount == 3 and TCount == 1)){
                    if(isO){
                        G = OWIN;
                    }else{
                        G = XWIN;
                    }
                    goto end;
                }
            }
            {
                int OXCount=0,TCount=0;
                for(int rc=0;rc<4;rc++){
                    if(field[3-rc][rc] == c) OXCount++;
                    else if(field[3-rc][rc] == 'T') TCount++;
                }
                if(OXCount == 4 or (OXCount == 3 and TCount == 1)){
                    if(isO){
                        G = OWIN;
                    }else{
                        G = XWIN;
                    }
                    goto end;
                }
            }
        }
    end:
        if(G == DRAW){
            for(int j=0;j<4;j++){
                for(int k=0;k<4;k++){
                    if(field[j][k] == '.') G = ING;
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(G == OWIN){
            cout << "O won" << endl;
        }else if(G == XWIN){
            cout << "X won" << endl;
        }else if(G == DRAW){
            cout << "Draw" << endl;
        }else{
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}
