#include <iostream>
#include <vector>
#include <string>

using namespace std;

int L,D,N;

int main(){
    cin >> L >> D >> N;
    vector<string> vs;
    for (int i = 0; i < D; i++){
        string s; cin >> s; vs.push_back(s);
    }
    for (int i = 1; i <= N; i++){
        int pattern[26][L];
        memset(pattern,0,sizeof(pattern));
        string s; cin >> s;
        int j = 0;
        int t = 0;
        while (j < s.size()){
              if (s[j] == '('){
                 j++;
                 while (s[j] != ')'){
                       char c = s[j];
                       pattern[c-'a'][t] = 1;
                       j++;
                 }
                 t++;
              }
              else {
                 char c = s[j];
                 pattern[c-'a'][t] = 1;
                 t++;  
              }
              j++;
        }
            int cnt = 0;
        for (int j = 0; j < vs.size();j++){
            for (int k = 0; k < vs[j].size(); k++){
                if (!pattern[vs[j][k]-'a'][k]) goto b;
            }
            cnt++;
            b:;
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}
