#include <stdio.h>
#include <iostream>
#include <vector>
#define MAX 2005
#define INF 0xfffffff
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOREACH(it,c) for(__typeof(c.begin())it=c.begin();it!=c.end();it++)
typedef pair<int, int> PII;

int C, N, M;
vector<PII> person[MAX];

int score(int b) {
    int res = 0; 
    while(b) res += b%2, b /= 2;
    return res;
}

int main() {
    FILE *fin = fopen("milk.in", "r"), *fout = fopen("milkslow.out", "w");
    fscanf(fin, "%d", &C); REP(c, C) {
        fscanf(fin, "%d %d", &N, &M);
        REP(i, M) {
            int T; fscanf(fin, "%d", &T);
            person[i].clear();
            REP(t, T) {
                PII like; fscanf(fin, "%d %d", &like.first, &like.second);
                like.first--;
                person[i].push_back(like);
            }
        }

        int res = INF; REP(b, 1<<N) {
            bool bad = false; REP(p, M) {
                bool happy = false; FOREACH(like, person[p])
                    if ((b>>like->first)%2 == like->second) happy = true;
                if (!happy) bad = true;
            }
            if (!bad && score(b) < score(res)) res = b;
        }

        if (res == INF) fprintf(fout, "Case #%d: IMPOSSIBLE\n", c+1);
        else {
            fprintf(fout, "Case #%d: ", c+1); 
            REP(i, N) fprintf(fout, "%d ", res%2), res /= 2;
            fprintf(fout, "\n");
        }
    }
    return 0;
}
