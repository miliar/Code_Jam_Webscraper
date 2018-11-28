#include <iostream>
#include <string>
#include <set>
#define len(a) int((a).size())
using namespace std;

int L, D, N;
set<string> st, st2;

int solve(string pre, string w){
    if (st2.find(pre) == st2.end()) return 0;
    if (w.empty()){
        //cout << pre << endl;
        if (st.find(pre) != st.end()) return 1;
        return 0;    
    }
    
    if (w[0] == '('){
        int res = 0, p=1;
        while (w[p] != ')') p++;
        
        for (int i = 1; i < len(w); i++){
            if (w[i] == ')') break;
            res += solve(pre+w[i], w.substr(p+1));   
        }
        //cout <<  "   " << w << "  ...  " << w.substr(p+1) << endl; 
        return res;
    } else {
        return solve(pre+w[0], w.substr(1,len(w)-1));    
    }
}

int main(){
    cin >> L >> D >> N;
    
    st2.insert("");
    for (int i = 0; i < D; i++){
        string w;
        cin >> w;
        st.insert(w);    
        for (int j = 1; j <= len(w); j++){
            st2.insert(w.substr(0,j));    
        }
    }
    
    for (int i = 0; i < N; i++){
        string w;
        cin >> w;
        cout << "Case #" << i+1 << ": " << solve("", w) << endl; 
        cerr << "CASE: " << i << endl;   
    }
    
    return 0;    
}
