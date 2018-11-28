#include <iostream>
#include <string>
using namespace std;
string a[100];
int n;
inline bool ok(int x,int y){
    return x >= 0 && x < n && y >= 0 && y < n;
}
bool check(int x,int y,int len,char c){
    int k;
    for(k = 1;k < len;++k)
        if(!ok(x,y+k) || a[x][y+k] != c) break;
    if(k == len) return 1;
    for(k = 1;k < len;++k)
        if(!ok(x+k,y) || a[x+k][y] != c) break;
    if(k == len) return 1;
    for(k = 1;k < len;++k)
        if(!ok(x+k,y+k) || a[x+k][y+k] != c) break;
    if(k == len) return 1;
    for(k = 1;k < len;++k)
        if(!ok(x+k,y-k) || a[x+k][y-k] != c) break;
    if(k == len) return 1;
    for(k = 1;k < len;++k)
        if(!ok(x-k,y+k) || a[x-k][y+k] != c) break;
    if(k == len) return 1;
    for(k = 1;k < len;++k)
        if(!ok(x-k,y-k) || a[x-k][y-k] != c) break;
    if(k == len) return 1;
    return 0;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,len;
    cin >> T;
    for(int I = 1;I <= T;++I){
        cin >> n >> len;
        int a1(n),a2(0),b1(n),b2(0);
        for(int i = 0;i < n;++i) cin >> a[i];
        for(int i = 0;i < n;++i)
            for(int j = 0;j < n;++j)
                if(a[i][j] != '.'){
                    a1 = min(a1,i);
                    a2 = max(a2,i);
                    b1 = min(b1,j);
                    b2 = max(b2,j);
                }
//        cout << a1 << " " << a2 << " " << b1 << " " << b2 << endl;
        for(int j = a1;j <= a2;++j)
            for(int i = b2;i >= b1;--i){
                if(a[j][i] == '.'){
                    int k = i - 1;
                    while(k >= b1){
                        if(a[j][k] != '.'){
                            swap(a[j][k],a[j][i]);
                            break;
                        }
                        --k;
                    }
                }
            }
/*        for(int i = 0;i < n;++i)
            cout << a[i] << endl;
        puts("");*/
        bool red(0),blue(0),k;
        for(int i = a1;i <= a2;++i)
            for(int j = b1;j <= b2;++j){
                if(a[i][j] == 'R'){
                    if(check(i,j,len,'R')) red = 1;
                }
                if(a[i][j] == 'B'){
                    if(check(i,j,len,'B')) blue = 1;
                }
            }
        cout << "Case #" << I << ": ";
        if(red && blue) cout << "Both" << endl;
        else if(red) cout << "Red" << endl;
        else if(blue) cout << "Blue" << endl;
        else if(!red && !blue) cout << "Neither" << endl;
    }
}
