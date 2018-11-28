#include <iostream>
#include <vector>
using namespace std;
vector < bool > a[50];
vector < bool > tmp;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int N,n;
    char x;
    cin >> N;
    for(int I = 1;I <= N;++I){
        cin >> n;
        for(int i = 0;i < n;++i) a[i].clear();
        for(int i = 0;i < n;++i)
            for(int j = 0;j < n;++j){
                cin >> x;
                a[i].push_back(x-'0');
            }
        int f[50];
        memset(f,-1,sizeof(f));
        for(int i = 0;i < n;++i)
            for(int j = n-1;j >= 0;--j)
                if(a[i][j]){
                    f[i] = j;
                    break;
                }
        int j,ans(0);
        for(int i = 0; i < n; ++i) {
            for(j = i; j < n && f[j] > i; ++j);
            for(; j > i; --j) {
                swap(f[j], f[j-1]);
                ++ans;
            }
        }
        cout << "Case #" << I << ": " << ans << endl;
    }
}
