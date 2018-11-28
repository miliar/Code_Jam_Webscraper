#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

typedef unsigned long long int u64;
int N, M;

vector<string> dict;

string solve(string list){
//    cout << "list " << list << endl;
    int maxp = -1;
    string res;
    for(int i = 0; i<dict.size();i++){ // try each word

        string word = dict[i];

        // Remove the ones having different length
        bool valid[dict.size()];
        for(int j = 0; j < dict.size(); j++){
            if(dict[j].size() == word.size()){
                valid[j] = true;
            }else{
                valid[j] = false;
            }
        }
        int left = word.size();
        int penalty = 0;
        int pos = 0;
        int invalid = 0;
        for(; left > 0; ){ // round
            char c = list[pos];
//            cout << "Next char is " << c << endl;
            // See if there is a word with this letter
            for(int j = 0; j < dict.size(); j++){
                if(valid[j] and dict[j].find(c) != string::npos){ // decided for the letter
                    // call for this letter
//                    cout << "call " << c << endl;
                    // Update dict accordingly
                    bool found = false;
                    for(int k = 0; k < word.size(); k++){
                        if(word[k] == c){ // found letter
                            found = true;
                            left--;
                            // remove inconsistent words
                            for(int j2 = 0; j2 < dict.size(); j2++){
                                if(dict[j2][k] != c){
                                    valid[j2] = false;
                                }
                            }
                        }else{
                            // remove inconsistent words
                            for(int j2 = 0; j2 < dict.size(); j2++){
                                if(dict[j2][k] == c){
                                    valid[j2] = false;
                                }
                            }
                        }
                    }
                    if(!found){
                        penalty++;
                    }
                    break;
                }
            }
            pos++;
        }
//        cout << "word " << word << endl;
//        cout << "penalty " << penalty <<endl;
//        break;
        if(maxp < penalty){
            maxp = penalty;
            res = word;
        }
    }
//    exit(0);
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        cin >> N >> M;
        string tmp;
        dict.clear();
        for(int j = 0; j < N; j++){
            cin >> tmp;
            dict.push_back(tmp);
        }
        cout << "Case #" << (i+1) << ": ";
        for(int j = 0; j < M; j++){
            cin >> tmp;
            cout << solve(tmp);
            if(j < M-1){
                cout << " ";
            }
        }
        cout << endl;
//        break;
    }
}

