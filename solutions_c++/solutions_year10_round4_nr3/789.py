#include <iostream>
using namespace std;
#define  N  1100
struct node{
    int x,y;
};    
bool v[2][N][N];
node a,b;
int n,minx,miny,maxx,maxy;
int cnt,ans;

void init(){
    cnt = 0;
    cin >> n;
    memset(v,0,sizeof(v));
    for(int i = 0;i < n;++i){
        cin >> a.x >> a.y >> b.x >> b.y;
        if(i){
            minx = min(minx,a.x);
            maxx = max(maxx,b.x);
            miny = min(miny,a.y);
            maxy = max(maxy,b.y);
        }
        else{
            minx = a.x;
            maxx = b.x;
            miny = a.y;
            maxy = b.y;
        }
        for(int x = a.x;x <= b.x;++x)
            for(int y = a.y;y <= b.y;++y)
                if(!v[0][x][y]){
                    ++cnt;
                    v[0][x][y] = 1;
                }
    }
}
    
void work(){
	ans = 0;
	while(cnt){
        cnt = 0;
        for(int x = minx-1;x <= maxx;++x){
            for(int y = miny-1;y <= maxy;++y){
                if(v[ans%2][x][y]){
                    if(v[ans%2][x-1][y] || v[ans%2][x][y-1]){
                        v[1-ans%2][x][y] = 1;
                        ++cnt;
                        minx = min(minx,x);
                        miny = min(miny,y);
                    }
                    else v[1-ans%2][x][y] = 0;
                }
                else{
                    if(v[ans%2][x-1][y] && v[ans%2][x][y-1]){
                        v[1-ans%2][x][y] = 1;
                        ++cnt;
                        minx = min(minx,x);
                        miny = min(miny,y);
                    }
                    else v[1-ans%2][x][y] = 0;
            	}
         }   	
     }    
     if(cnt) ++ans;
    }
}
    
int main(){
    int T;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin >> T;
    for(int index = 1;index <= T;++index){
        init();
        work();
        printf("Case #%d: %d\n",index,ans+1);
    }
}

