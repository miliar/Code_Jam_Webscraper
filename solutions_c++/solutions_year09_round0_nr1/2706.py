#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

#define MAX 5001

vector<string> dictionary;
vector<string> patterns;
vector<int> idx;
int valid[MAX];
int used[MAX];
int total;

void backtrack(int start, vector<char> &s, int n, int L, vector<vector<char> > &VVC, int loc){
    if(s.size() == L){
        /*string str = "";
        bool used = false;
        for(int j=0; j<s.size(); j++) str += s[j];
        for(int m=0; m < patterns.size(); m++){
            if(str == patterns[m]) {
                used = true;
                break;
            }
        }*/
        if(!used[loc]){
            total++;
            used[loc] = 1;
        }
        
        return;
    }
    else {
        for(int i=0; i < VVC[n].size(); i++){
            for(int j=0; j < dictionary.size(); j++){
                if(valid[j] == n && dictionary[j][start] == VVC[n][i]) valid[j]++;
            }

            for(int j=0; j < dictionary.size(); j++){
                if(valid[j] == n+1){
                    s.push_back(VVC[n][i]);
                    backtrack(start+1, s, n+1, L, VVC, j);
                    s.pop_back();        
                }
            }

            for(int j=0; j < dictionary.size(); j++){
                if(valid[j] == n+1) valid[j]--;
            }
            
        }
    }
    return;
}

int getMatches(string str, int L){
    int k=0;
    vector<vector<char> > P(L);

    for(int i=0; i < str.size(); i++){
        if(str[i]=='('){
            i++;
            while(str[i] != ')'){
                P[k].push_back(str[i]);
                i++;
            }
        }
        else {
            P[k].push_back(str[i]);
        }
        k++;
    }

    vector<char> S;
    memset(valid, 0, sizeof(valid));
    memset(used, 0, sizeof(used));
    total = 0;
    backtrack(0, S, 0, L, P, 0);

    
    return total;
}

int main(){
    ifstream fin("A-small-attempt3.in");
    ofstream fout("A.out");

    int L, D, N;
    string tmp;

    fin >> L >> D >> N;
    
    for(int i=0; i < D; i++){
        fin >> tmp;
        dictionary.push_back(tmp);
    } 

    for(int i=1; i <= N; i++){
        total = 0;
        fin >> tmp;
        patterns.clear();
        fout << "Case #" << i << ": " << getMatches(tmp, L) << endl;
    }

    return 0;
}