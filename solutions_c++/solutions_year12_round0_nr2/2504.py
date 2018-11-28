#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(){
    int ans, T, N, S, p, cand;
    vector<int> t, amari;
    cin >> T;
    for(int i=0; i<T;i++){
        ans = 0;cand =0;
        t.clear();
        amari.clear();
        cin >> N >> S >> p;
        for(int j=0; j<N; j++){
            int tmp;
            cin >> tmp;
            t.push_back(tmp);
            amari.push_back(tmp%N);
        }
        vector<int>::iterator it = t.begin();
        vector<int>::iterator it_end = t.end();
        for(; it!=it_end; ++it){
            if(*it >= (p-1>=0?p-1:0) * 2 + p)
                ans++;
            else if(*it >= (p-2>=0?p-2:0) * 2 + p)
                    cand++;
        }
        //cout << "ans: " << ans << ",cand:" <<cand << endl;
        if(cand > S)ans += S;
        else ans += cand;
        
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
}
