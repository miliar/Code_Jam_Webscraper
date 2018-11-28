//#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

//FILE* in = fopen("in.txt", "r");
//FILE* out = fopen("out.txt", "w");
ifstream in("A-large.in");
ofstream out("alargeout.txt");

int n, s, q;

map<string, int> nameRef;
int quer[1001];

int cache[101][1001];

int dp(int eng, int at){
    if(at == q) return 0;
    int &c = cache[eng][at];
    if(c != -1) return c;
    c = q + s;
    if(quer[at] != eng) return c = dp(eng, at + 1);
    for(int i = 0; i < s; i++) if(i != eng){
        int nxt = 1 + dp(i, at + 1);
        if(nxt < c) c = nxt;
    }
    return c;
}

int solve(){
    nameRef.clear();
    in >> s;
    string tmp; 
    getline(in, tmp);
    for(int i = 0; i < s; i++){
        getline(in, tmp);
        nameRef[tmp] = i;
    }
    in >> q;
    getline(in, tmp);
    for(int i = 0; i < q; i++){
        getline(in, tmp);
        quer[i] = nameRef[tmp];
    }
    for(int i = 0; i < s; i++)
        for(int j = 0; j < q; j++)
            cache[i][j] = -1;
    int ans = dp(0, 0);
    for(int i = 1; i < s; i++){
        int nxt = dp(i, 0);
        if(ans > nxt) ans = nxt;
    }
    return ans;   
}


int main(){
    in >> n;
    for(int c = 1; c <= n; c++)
        out << "Case #" << c << ": " << solve() << endl;
    return 0;
}

