#include <iostream>
#include <string>
using namespace std;
string s[110];
int T;
int r,c;
int cover(int i,int j){
    if(i >= r-1) return 0;
    if(j >= c-1) return 0;
    if(s[i][j+1] == '#' && s[i+1][j] == '#' && s[i+1][j+1] == '#'){
        s[i][j] = '/';
        s[i][j+1] = '\\';
        s[i+1][j] = '\\';
        s[i+1][j+1] = '/';
        return 1;
    }
    return 0;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ":" << endl;
        cin >> r >> c;
        for(int i = 0;i < r;++i)
            cin >> s[i];
        int ans(1);
        for(int i = 0;i < r && ans;++i)
            for(int j = 0;j < c;++j)
                if(s[i][j] == '#')
                    if(!cover(i,j)){
                        ans = 0;
                        break;
                    }
        if(ans){
            for(int i = 0;i < r;++i)
                cout << s[i] << endl;
        }
        else cout << "Impossible" << endl;
    }
}
