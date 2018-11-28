#include<iostream>
#include<vector>
#include<set>
#include<fstream>

using namespace std;

typedef pair<char,char> pcc;

int main(){
    ofstream fout ("out2.out");
    int t;
    cin >> t;
    for (int caso = 1; caso<=t; caso++){
        int c,d,n;
        cin >> c;
        vector<vector<pcc > > transf (100);
        vector<set<char> > opp (100);
        vector<set<char> > tr (100);
        for (int i = 0; i < c; i++){
            string s;
            cin >> s;
            transf[s[0]].push_back(pcc(s[1],s[2]));
            transf[s[1]].push_back(pcc(s[0],s[2]));
            tr[s[0]].insert(s[1]);
            tr[s[1]].insert(s[0]);
        }
        cin >> d;
        for (int i = 0; i < d; i++){
            string s;
            cin >> s;
            opp[s[0]].insert(s[1]);
            opp[s[1]].insert(s[0]);
        }
        cin >> n;
        string s;
        cin >> s;
        for (int i = 0; i < s.size(); i++){
            if (i != 0 and tr[s[i]].find(s[i-1]) != tr[s[i]].end()){
                char x = s[i], x2 = s[i-1];
                bool enc = false;
                for (int j = 0; j < transf[x].size() and !enc; j++){
                    if (transf[x][j].first == x2){
                        enc = true;
                        s.erase(s.begin()+i);
                        s[i-1] = transf[x][j].second;
                        i--;
                    }
                }
            }
            else {
                bool enc = false;
                char x = s[i];
                for (int j = i-1; j >= 0 and !enc; j--){
                    char x2 = s[j];
                    if (opp[x].find(x2) == opp[x].end()){ 
                        continue;
                    }
                    enc = true;
                    string final = "";
                    if (i < s.size()-1) final = s.substr(i+1, s.size()-i-1);
                    s = final;
                    i=-1;
                }
            }
        }
        fout << "Case #" << caso << ": [";
        for (int i = 0; i < s.size(); i++){
            if (i != 0) fout << ", ";
            fout << s[i];
        }
        fout << "]" << endl;
    }
}
