#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main(){
    int T; cin >> T;
    for(int i = 1; i <= T; ++i){
        vector<int> a, b, ap, bp;
        a.push_back(0);
        b.push_back(0);
        ap.push_back(1);
        bp.push_back(1);
        int prev = -1;
        int N; cin >> N;
        while(N--){
            string r;
            int btn;
            cin >> r >> btn;
            if(r == "O"){
                if(prev == -1 || prev == 0){
                    a.push_back(a.back() + abs(btn-ap.back()) + 1);
                }
                else{
                    a.push_back(max(b.back()+1, a.back() + abs(btn-ap.back()) + 1));
                }
                ap.push_back(btn);
                prev = 0;
            }
            else{
                if(prev == -1 || prev == 1){
                    b.push_back(b.back() + abs(btn-bp.back()) + 1);
                }
                else{
                    b.push_back(max(a.back()+1, b.back() + abs(btn-bp.back()) + 1));
                }
                bp.push_back(btn);
                prev = 1;
            }
        }
        printf("Case #%d: %d\n", i, max(a.back(), b.back()));
    }

}
