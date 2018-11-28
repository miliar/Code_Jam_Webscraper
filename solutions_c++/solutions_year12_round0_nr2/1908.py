#include <iostream>
using namespace std;
int main(){
int test, cas;
cin>>test;
for (cas=1; cas<=test; ++cas){
    int n, s, p;
    cin >> n >> s >> p;
    int cnt = 0, x, y;
    for (int i=0; i<n; ++i){
        cin >> x;
        if (x%3 == 0) y = x / 3; else y = x / 3 + 1;
        if (y >= p) cnt ++;
        else if (s > 0 && x > 0){
            if (x%3 == 2) y = x / 3 + 2; else y = x / 3 + 1;
            if (y >= p) cnt++, s--;
        }
    }
    cout << "Case #" << cas << ": " << cnt << endl;
}
return 0;
}
