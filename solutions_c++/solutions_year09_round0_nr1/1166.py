#include <iostream>
#include <vector>
#include <string>



using namespace std;

int main(){
    int L, D, N;
    cin >> L >> D >> N;
    vector<string> words (D);
    string temp;
    
    for(int i=0;i<D;i++){
        cin >> words[i];
    }
    
    bool letters[15][26];
    
    for(int i=1;i<=N;i++){
        cin >> temp;
        int shift = 0;
        for(int j=0;j<L;j++){
            for(int k=0;k<26;k++) letters[j][k] = false;
            if(temp[j+shift]=='('){
                shift++;
                while(temp[j+shift]!=')'){
                    letters[j][temp[j+shift]-'a'] = true;
                    shift++;
                }
            } else letters[j][temp[j+shift]-'a'] = true;
        }
        int ans = 0;
        for(int j=0;j<D;j++){
            int k;
            for(k=0;k<L;k++)
                if(!letters[k][words[j][k]-'a']) break;
            if(k==L) ans++;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
