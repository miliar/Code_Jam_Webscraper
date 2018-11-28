#include<iostream>
#include<map>
#include<set>

using namespace std;

int main() {
    int T; 
    cin >> T;
    for(int t = 1; t<= T; t++ ) {
        cout << "Case #" << t<<": ";
        int C,D,N;
        cin >> C;
        map<string,char> CMap;
        for(int i = 0; i< C; i++) {
            string Cstr; cin >> Cstr;
            CMap[Cstr.substr(0,2)] = Cstr[2];
            string sub2;
            sub2 += Cstr[1];
            sub2 += Cstr[0];
            CMap[sub2] = Cstr[2];
        }
        cin >> D;
        set<string> DSet;
        for(int i = 0; i< D; i++) {
            string Dstr; cin >> Dstr; 
            DSet.insert(Dstr);
            string Dstr2;
            Dstr2 += Dstr[1];
            Dstr2 += Dstr[0];
            DSet.insert(Dstr2);
        }
        cin >> N;
        string str,res;
        cin >> str;
        for(int i = 0; i<N; i++) {
            res += str[i];            
            while(res.length() > 1) {
                int len = res.length();
                string last2 = res.substr(len-2);
                if(CMap.find(last2) != CMap.end()) {
                    res.erase(len-2);
                    res += CMap[last2];
                } else {
                    break;
                }
            }
            int len = res.length();
            for(int j = 0; j< len-1; j++) {
                string comb;
                comb += res[j];
                comb += res[len-1];
                if(DSet.count(comb)) {
                    res = "";
                    break;
                }
            }
        }
        cout << '[';
        for(int i = 0;i < res.length(); i++) {
            cout << res[i]; 
            if(i +1 != res.length() ) cout << ", ";
        }
        cout << ']';
        cout << endl;
    }
}
