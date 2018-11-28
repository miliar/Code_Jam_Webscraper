#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int gen[27][27], opp[27][27];

int ctoi(char c) { if(c<'A' || c>'Z') return 0; else return c-'A'+1;}
char itoc(int i) { if(i<1 || i>26) return (char)0; else return i-1+'A';}

void solve() {
    int n;
    string str, tmp;

    memset(gen, 0, sizeof(gen));
    memset(opp, 0, sizeof(opp));

    cin >> n;
    for(int i=0; i<n; ++i) {
        cin >> str;
        gen[ctoi(str[0])][ctoi(str[1])]=gen[ctoi(str[1])][ctoi(str[0])]=ctoi(str[2]);
    }

    cin >> n;
    for(int i=0; i<n; ++i) {
        cin >> str;
        opp[ctoi(str[0])][ctoi(str[1])]=opp[ctoi(str[1])][ctoi(str[0])]=1;
    }

    cin >> n >> str;
    tmp="";
    for(int i=0; i<n; ++i) {
        int end = ctoi(tmp[tmp.length()-1]);
        int cur = ctoi(str[i]);

        if(gen[end][cur]) tmp[tmp.length()-1]=itoc(gen[end][cur]), str[i]='a';
        else {
            for(int j=1; j<27; ++j) if(opp[cur][j] && tmp.find(itoc(j))!=string::npos) {tmp="";str[i]='a';break;}
        }
        if(str[i]!='a') tmp+=str[i];
    }
    cout << "[";
    for(int i=0; i<tmp.length(); ++i) {
        if(i!=0) cout << ", ";cout << tmp[i];
    }
    cout << "]" << endl;
}

int main(){

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int cases, cid;
    cin >> cases;

    for(cid=1; cid<=cases; ++cid) {
        cout << "Case #" << cid << ": ";
        solve();
    }

    return 0;
}
