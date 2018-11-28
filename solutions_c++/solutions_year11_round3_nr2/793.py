#include <iostream>
using namespace std;
int T;
long long l,t,n,c;
int a[1010];
int dis[1010];
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ": ";
        cin >> l >> t >> n >> c;
        for(int i = 0;i < c;++i)
            cin >> a[i];
        int build(0);
        long long tim(0);
        memset(dis,0,sizeof(dis));
        for(int i = 0;i < n;++i){
            tim += a[i%c] * 2;
            if(build){
                if(dis[0] <= a[i%c]){
                    dis[1] = dis[0];
                    dis[0] = a[i%c];
                }
                else if(dis[1] <= a[i%c])
                    dis[1] = a[i%c];
            }
            else{
                if(tim >= t){
                    if(dis[0] <= (tim - t) / 2){
                        dis[1] = dis[0];
                        dis[0] = (tim-t) / 2;
                    }
                    build = 1;
                }
            }
        }
//        cout << l << " " << t << " " << n << " " << c << endl;
        for(int i = 0;i < l;++i){
//            cout << dis[i] << " ";
            tim -= dis[i];
        }
        cout << tim << endl;
    }
}
