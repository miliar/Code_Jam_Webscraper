#include <iostream>
#include <vector>
#include <string>
using namespace std;

int L, D, N;

vector<string> words;


int main() {

    ios_base::sync_with_stdio(false);

    cin>>L>>D>>N;
    for (int i=0; i<D; i++) {
        string s; cin>>s;
        words.push_back(s);
    }
    
    for (int n=0; n<N; n++) {
    
        vector<bool> ok(words.size(), true);
        string pattern; cin>>pattern;
        int ix=0;

        for (int l=0; l<L; l++) {
            unsigned lets = 0;
            if (pattern[ix]!='(') {
                lets = 1<<(pattern[ix]-'a');
                ix++;
            }
            else {
                ix++;
                while (pattern[ix]!=')') {
                    lets = lets | (1<<(pattern[ix]-'a'));
                    ix++;
                }
                ix++;
            }
            
            for (int i=0; i<int(words.size()); i++)
                ok[i] = ok[i] && ((1<<(words[i][l]-'a'))&lets) != 0;
        }
        
        int result = 0;
        for (int i=0; i<int(words.size()); i++)
            if (ok[i])
                result++;
        cout<<"Case #"<<(n+1)<<": "<<result<<"\n";
    }

    return 0;
}
