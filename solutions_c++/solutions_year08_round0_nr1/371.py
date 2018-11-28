
#include <iostream>
#include <fstream>
using namespace std;
const int INF = 10000;
bool mark[1000][100];
int f[1000][100];
bool same[1000][100];
string engine[100], query;
int S, Q;
int calc(int q, int s){
    if (!mark[q][s]){
        mark[q][s] = true;
        if (same[q - 1][s]){
            f[q][s] = INF;
            for(int i = 0; i < S; ++ i)
                if (i != s) f[q][s] <?= calc(q - 1, i) + 1;
        }
        else f[q][s] = calc(q - 1, s);
    }
    return f[q][s];
}
int main(){
    //ifstream cin("A-large.in");
    //ofstream cout("out.txt");
    int ncase;
    cin >> ncase;
    for(int tcase = 1; tcase <= ncase; ++ tcase){
        cin >> S;
        getline(cin, engine[0]);
        for(int i = 0; i < S; ++ i) getline(cin, engine[i]);
        cin >> Q;
        getline(cin, query);
        memset(same, false, 1000*100);
        memset(mark, false, 1000*100);
        memset(mark[0], true, 100);
        for(int i = 0; i < Q; ++ i){
            getline(cin, query);
            for(int j = 0; j < S; ++ j)
                if (query == engine[j]){
                    same[i][j] = true;
                    mark[i][j] = true;
                    f[i][j] = INF;
                }
                else same[i][j] = false;
        }/*
        for(int i = 0; i < Q; ++ i)
        {
            for(int j = 0; j < S; ++ j)
                cout << same[i][j] << ' ';
            cout << endl;
        }*/
        cout << "Case #" << tcase << ": ";
        if (Q == 0) {
            cout << 0 << endl;
            continue;
        }
        for(int i = 0; i < S; ++ i)
            if (!same[0][i]) f[0][i] = 0; else f[0][i] = INF;
        int mini = INF;
        for(int i = 0; i < S; ++ i)
            mini <?= calc(Q - 1, i);/*
        for(int i = 0; i < Q; ++ i){
            for(int j = 0; j < S; ++ j)
                printf("f[%d][%d] = %d\n", i, j, calc(i, j));
        }*/
        cout << mini << endl;
    }
    return 0;
}
