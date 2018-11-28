#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)
        
vector<string> words;
char discovered[15];
char proib[30];
char guessed[30];

bool hasLetter(string s, char c)
{
    FOR(i, 0, SZ(s)) if(s[i] == c) return true;
    return false;
}

bool consistent(string s)
{
    FOR(i, 0, SZ(s)) 
        if(discovered[i] != -1 && discovered[i] != s[i]) return false;
        else if(discovered[i] == -1 && guessed[s[i] - 'a']) return false;
   
    return true;
}

bool prohibited(string s)
{
    FOR(i, 0, SZ(s)) if(proib[s[i] - 'a']) return true;
    return false;
}

string solve(string list)
{
    int score = -1;
    string best;
    FOR(i, 0, SZ(words)){
        int errors = 0;
        memset(discovered, -1, sizeof(discovered));
        memset(proib, 0, sizeof(proib));
        memset(guessed, 0, sizeof(guessed));
        FOR(j, 0, SZ(list)){
            bool tryit = false;
            FOR(k, 0, SZ(words)) if(SZ(words[k]) == SZ(words[i])){
                if(consistent(words[k]) && hasLetter(words[k], list[j]) && !prohibited(words[k])){
                    tryit = true;
                }
            }
            if(tryit){
                bool correct = false;
                FOR(kk, 0, SZ(words[i])){
                    if(words[i][kk] == list[j]){
                        correct = true;
                        discovered[kk] = list[j];
                        guessed[list[j] - 'a'] = 1;
                    }
                }
                if(!correct) {
                    errors++;
                    proib[list[j] - 'a'] = 1;
                }
            }
        }
        if(errors > score){
            score = errors;
            best = words[i];
        }
    }
    return best;    
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(testcase, 0, t){
        int n, m;
        words.clear();
        
        printf("Case #%d:", testcase + 1);

        cin >> n >> m;

        FOR(i, 0, n){
            string s;
            cin >> s;
            words.pb(s);
        }

        FOR(i, 0, m){
            string list;
            cin >> list;
            cout << " " << solve(list);
        }
        cout << endl;
    }
    return 0;
}

