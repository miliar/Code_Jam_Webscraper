#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <set>
#include <stack>
#define pb push_back
#define fs first
#define sc second

using namespace std;

int combine[300][300];
vector<char> opposite[300];
char buf[150];

int main(void){
    int test;
    scanf("%d", &test);

    for (int t=0;t<test;++t){
        int c, d;
        stack<char> S;
        for (int i=0;i<300;++i) opposite[i].clear();

        for (int i=0;i<250;++i)
            for (int j=0;j<250;++j) combine[i][j] = 0;

        scanf("%d", &c);
        for (int i=0;i<c;++i){
            scanf("%s", buf);
            combine[buf[0]][buf[1]] = buf[2];
            combine[buf[1]][buf[0]] = buf[2];
        }

        scanf("%d", &d);
        for (int i=0;i<d;++i){
            scanf("%s", buf);
            opposite[buf[0]].pb(buf[1]);
            opposite[buf[1]].pb(buf[0]);
        }
        int n;
        scanf("%d", &n);
        scanf("%s", buf);
        vector<int> elemCnt(30, 0);
        for (int i=0;i<n;++i){
            if ( S.empty()) {
                S.push(buf[i]);
                ++elemCnt[buf[i]-'A'];
                continue;
            }

            if ( combine[buf[i]][S.top()] > 0 ){
                char tmpelem = S.top();
                S.pop();
                S.push(combine[buf[i]][tmpelem]);
                --elemCnt[tmpelem-'A'];
                ++elemCnt[combine[buf[i]][tmpelem]-'A'];
                continue;
            }

            bool foundOpposite = false;
            for (int j=0;j<opposite[buf[i]].size();++j){
                if ( elemCnt[opposite[buf[i]][j]-'A']>0){
                    foundOpposite = true;
                    while ( !S.empty())S.pop();
                    for (int k=0;k<30;++k) elemCnt[k] = 0;
                    break;
                }
            }

            if ( !foundOpposite ){
                S.push(buf[i]);
                ++elemCnt[buf[i]-'A'];
            }
        }

        vector <char> res;
        while ( !S.empty()){res.pb(S.top());S.pop();}
        printf("Case #%d: [", t+1);
        bool fs = true;
        for (int i=(int)res.size()-1;i>=0;--i){
            if ( !fs ) printf (", ");
            printf ("%c", res[i]);
            S.pop();
            fs = false;
        }
        printf("]\n");
    }
    return 0;
}
