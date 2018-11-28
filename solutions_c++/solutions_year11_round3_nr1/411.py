#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

namespace
{
    int R, C;
}

bool checkFill(vector<vector<char> > &v, int x, int y)
{
    if(x+1<R && y+1<C){
        return v[x][y]=='#' && v[x+1][y]=='#' && v[x][y+1]=='#' && v[x+1][y+1]=='#';
    }else{
        return false;
    }
}
void Fill(vector<vector<char> > &v, int x, int y)
{
    v[x][y]='/';
    v[x+1][y]='\\';
    v[x][y+1]='\\';
    v[x+1][y+1]='/';
}

int main()
{
    int T;
    cin >> T;
    REP(i, T){
        cin >> R >> C;

        vector<vector<char> > m(R);
        int blues=0;
        REP(j, R){
            m[j]=vector<char>(C);
            REP(k, C){
                cin >> m[j][k];
                if(m[j][k]=='#'){
                    blues++;
                }
            }
            cin.ignore();
        }
/*
        REP(j, R){
            REP(k, C){
                cout << m[j][k];
            }
            cout << endl;
        }
*/
        if(blues%4!=0){
            cout << "Case #" << (i+1) << ":" << endl;
            cout << "Impossible" << endl;
            continue;
        }
        bool success=true;
        REP(j, R){
            REP(k, C){
/*
                cout << j << ", " << k << "------" << endl;
                REP(p, R){
                    REP(q, C){
                        cout << m[p][q];
                    }
                    cout << endl;
                }
*/
                if(m[j][k]=='#'){
                    if(checkFill(m, j, k)==false){
                        success=false;
                        break;
                    }else{
                        Fill(m, j, k);
                    }
                }
            }
            if(success==false){
                break;
            }
        }
        if(success){
            cout << "Case #" << (i+1) << ":" << endl;
            REP(j, R){
                REP(k, C){
                    cout << m[j][k];
                }
                cout << endl;
            }
        }else{
            cout << "Case #" << (i+1) << ":" << endl;
            cout << "Impossible" << endl;
        }
    }
    return 0;
}
