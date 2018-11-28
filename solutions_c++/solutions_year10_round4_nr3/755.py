#include <iostream>
#include <vector>
using namespace std;
const int MAXN = 1010;
bool vi[2][MAXN][MAXN];
int T,x1,x2,y1,y2,n,minx,miny,maxx,maxy;
int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        int cnt(0);
        cin >> n;
        memset(vi,0,sizeof(vi));
        for(int i = 0;i < n;++i){
            cin >> x1 >> y1 >> x2 >> y2;
            if(i){
                minx = min(minx,x1);
                maxx = max(maxx,x2);
                miny = min(miny,y1);
                maxy = max(maxy,y2);
            }
            else{
                minx = x1;
                maxx = x2;
                miny = y1;
                maxy = y2;
            }
            for(int x = x1;x <= x2;++x)
                for(int y = y1;y <= y2;++y)
                    if(!vi[0][x][y]){
                        ++cnt;
                        vi[0][x][y] = 1;
                    }
        }
        int ans(0);
/*        for(int x = 0;x <= maxx;++x){
            for(int y = 0;y <= maxy;++y)
                cout << vi[0][x][y];
            puts("");
        }*/
        while(cnt){
            cnt = 0;
            for(int x = minx-1;x <= maxx;++x)
                for(int y = miny-1;y <= maxy;++y)
                    if(vi[ans%2][x][y]){
                        if(vi[ans%2][x-1][y] || vi[ans%2][x][y-1]){
                            vi[1-ans%2][x][y] = 1;
                            ++cnt;
                            minx = min(minx,x);
                            miny = min(miny,y);
                        }
                        else vi[1-ans%2][x][y] = 0;
                    }
                    else{
                        if(vi[ans%2][x-1][y] && vi[ans%2][x][y-1]){
                            vi[1-ans%2][x][y] = 1;
                            ++cnt;
                            minx = min(minx,x);
                            miny = min(miny,y);
                        }
                        else vi[1-ans%2][x][y] = 0;
                    }
/*            for(int x = 0;x <= maxx;++x){
                for(int y = 0;y <= maxy;++y)
                    cout << vi[1-ans%2][x][y];
                puts("");
            }
            puts("");*/
            if(cnt) ++ans;
        }
        printf("Case #%d: %d\n",I,ans+1);
    }
}
