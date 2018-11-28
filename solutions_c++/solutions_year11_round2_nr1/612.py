#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <set>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t; scanf("%d",&t); t;})
#define sz size()
#define pb push_back




int main() {
    int kases=GI+1;
    FOR(kase,1,kases) {
        printf("Case #%d:\n", kase);
        int n = GI, mp[n][n],sc[n][n];
        char buf[110];
        REP(i,n) REP(j,n) sc[i][j] = -1;
        
        int tot[n], win[n];
        REP(i,n) tot[i] = n, win[i] = 0;
        REP(i,n) {
            scanf("%s", buf);
            REP(j,n) 
            if(buf[j] == '.') mp[i][j] = -1, tot[i]--;
            else if(buf[j] == '1') mp[i][j] = 1, win[i]++;
            else mp[i][j] = 0;
        }
        double opp[n], opp2[n];
        REP(i,n) {
            double s2 = 0, v;
            int c=0;
            REP(j,n) if(mp[i][j] != -1) {
                if(mp[i][j] == 1) {
                    v = (double)win[j] / (tot[j]-1);
                }
                else {
                    v = (double)(win[j]-1) / (tot[j]-1);
                }
                s2 += v;
                c++;
            }
            opp[i] = s2 / c;
        
        }
        REP(i,n) {
            double s3 = 0;
            int c=0;            
            REP(j,n) if(mp[i][j] != -1) {
                s3 += opp[j];            
                c++;
            }
            opp2[i] = s3 / c;
            double score = ((double)win[i] / tot[i] + 2 * opp[i] + opp2[i]) / 4.0;
            printf("%.10lf\n", score);
            
        }

        
        
        
    
    }



}

