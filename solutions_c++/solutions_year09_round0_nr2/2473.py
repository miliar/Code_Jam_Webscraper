#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

#define sz(a) (int)a.size()
#define all(a) a.begin(),a.end()
#define pb push_back

using namespace std;

vector<string> mat, ans;
int h,w;

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

char label;


void rec(int y, int x){
    int mmm=(int)1e8;
    int d=-1;
    ans[y][x] = label;
    
    for(int i=0; i<4; ++i){
        int Y = y+dy[i], X = x+dx[i];
        if(Y<0||Y>=h||X<0||X>=w) continue;
           if(mat[Y][X]<mmm && mat[Y][X]<mat[y][x]){
               mmm = mat[Y][X];
               d = i;
           }
           }
        if(d > -1){
            int Y = y+dy[d], X = x+dx[d];
            if(ans[Y][X]>'9'){
                ans[y][x] = ans[Y][X];
                return;
            }
            rec(Y, X);
            ans[y][x] = ans[Y][X];
        }
    }

    int main(){
        int n; cin>>n;
        for(int fase=0;fase<n;++fase){
            mat.clear();
            label = 'a';
            cin >> h >> w;
            for(int y=0;y<h;++y){
                string tmp;
                for(int x=0;x<w;++x){
                    string tmp2; cin >> tmp2;
                    tmp += tmp2;
                }
                mat.pb(tmp);
            }
            ans = mat;
            for(int y=0;y<h;++y){
                for(int x=0;x<w;++x){
                    if(ans[y][x]<'a'){
                        rec(y, x);
                        char lgt='a';
                        for(int i=0; i<sz(ans); ++i){
                            for(int j=0; j<sz(ans[i]); ++j){
                                lgt = max(lgt, ans[i][j]);
                            }
                        }
                        label = lgt+1;
                    }
                }
            }
            cout << "Case #"<<fase+1<<":"<< endl;
            for(int y=0;y<h;++y){
                for(int x=0;x<w;++x){
                    cout << ans[y][x]  << " ";
                }
                cout <<  endl;
            }
        }
        return 0;
    }
