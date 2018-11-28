#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back

int main()
{
    string ex[4], sol[4];
    ex[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    ex[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    ex[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    ex[3] = "y qee";
    
    sol[0] = "our language is impossible to understand";
    sol[1] = "there are twenty six factorial possibilities";
    sol[2] = "so it is okay if you want to just give up";
    sol[3] = "a zoo";
    
    string map = "";
    REP(i, 26) map += "?";
    REP(i, 4) REP(j, SZ(ex[i])) {
        if(ex[i][j] != ' ') map[ex[i][j]-'a'] = sol[i][j];
    }
    
    REP(i, 26) {
        bool found = 0;
        REP(j, SZ(map)-1) {
            if(map[j] == (char)(i+'a')) {
                found = 1;
                break;
            }
        }
        if(!found) {
            map[25] = (char)(i+'a');
            break;
        }
    }
    
    
    int T;
    string line;
    scanf("%d", &T);
    while(getchar() != '\n');
    REP(caso, T) {
        line = "";
        while(1) {
            char c = getchar();
            if(c == '\n' || c == EOF) break;
            line += c;
        }
        
        REP(i, SZ(line)) {
            if(line[i] != ' ') line[i] = map[line[i]-'a'];
        }
        
        cout << "Case #" << caso+1 << ": " << line << endl; 
    }
    
    
}