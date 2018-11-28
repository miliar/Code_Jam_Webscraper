#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int T, N, M;
const int MAXN = 10100;
char dict[MAXN][14];
int where[MAXN][32];
char al[27];
int sol[120];
vector<int> loc[27];
const bool dbg = 0;

int solve(){
    int pos = 0;
    int ans = -1; int best = -1;
if (dbg)    cout<<"\n solving for "<<al<<"\n";
    for (int i = 0; i < N; i++) {
        int ret = 0;
        vector<int> cur, next;
        char *word = dict[i];
        int n = strlen(word);
        char pat[n + 1];
        for (int j = 0; j < n; j++) pat[j] = '_';
        int cnt[28];
        memset(cnt, 0, sizeof(cnt));
        for (int j = 0; j < N; j++)
            if (strlen(dict[j]) == n) {
               cur.push_back(j);
               for (int k = 0; k < n; k++)
                   cnt[dict[j][k] - 'a']++;
            }
        for (int j = 0; j < 26; j++) loc[j].clear();
        for (int j = 0; j < n; j++)
            loc[word[j] - 'a'].push_back(j);
if (dbg)        cout<<"   test "<<word<<"\n";
        for (int j = 0; j < 26; j++) {
            char c = al[j];
            next.clear();
if (dbg){            cout<<"    at "<<c<<": "; for (int k = 0; k < cur.size(); k++) cout<<dict[cur[k]]<<" "; cout<<"\n";}
/*if (dbg) {
          for (int j = 0; j < 26; j++)
              if (cnt[j]) cout<<"  cnt "<<(char)(j  +'a')<<" : "<<cnt[j]<<"\n";
         }
         */
            if (cnt[c - 'a'] > 0) {
               // guess 
if (dbg)               cout<<"              guess "<<c<<"\n";
               if (loc[c - 'a'].size() == 0) {
                           ret ++ ;
if (dbg)                           cout<<"                             fail...\n";
               }
               for (int k = 0; k < cur.size(); k++) {
                           int x = cur[k];
                           if (where[x][c - 'a'] == where[i][c - 'a']) {
                                          next.push_back(x);
                           }
                           else {
                                for (int k = 0; dict[x][k]; k++) {
                                    cnt[dict[x][k] - 'a'] --;
                                }
                           }
               }
               cur = next;
            }
            if (cur.size() == 1) {
                           break;
            }
        }
if (dbg)        cout<<"   score: "<<ret<<"\n";
        if (ret > best) {
                best = ret;
                ans = i;
                }
    }
    return ans;
}

int main()
{
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)  {
        scanf("%d%d", &N, &M);
if (dbg)        cout<<"\n\n--- CASE "<<tt<<"\n\n";
memset(where, 0, sizeof(where));
        for (int i = 0; i < N; i++) {
            scanf("%s", dict[i]);
            for (int k = 0; k < strlen(dict[i]); k++) {
                    where[i][dict[i][k] - 'a'] |= 1<<k;
            }
if (dbg)            cout<<dict[i]<<"\n";
        }
        for (int j = 0; j < M; j++) {
            scanf("%s", al);
            sol[j] = solve();
        }
        printf("Case #%d: ", tt+1);
        for (int j = 0; j < M; j++)
        {
         printf("%s", dict[sol[j]]);
         if (j + 1 == M) printf("\n");
         else printf(" ");
        }
    }
    return 0;
}
