using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <iostream>
#include <memory.h>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define ABS(a) ((a)<0?(-(a)):(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

char combine[200][200];
bool opposed[200][200];
int hasLetter[200];
char bases[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

void clearHasLetter() {
    FOR(i, 8) { hasLetter[bases[i]] = 0; }
}

int main() {
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;cin>>t;
    FOR1(cno, t) {
        ms0(combine);
        ms0(opposed);
        int n;
        cin>>n;
        while(n--) {
            char ccc[5];
            scanf("%s", ccc);
            combine[ccc[0]][ccc[1]] = ccc[2];
            combine[ccc[1]][ccc[0]] = ccc[2];
            //cout<<"Combine "<<ccc[0]<<", "<<ccc[1]<<" = "<<ccc[2]<<endl;
        }
        cin>>n;
        while(n--) {
            char ccc[5];
            scanf("%s", ccc);
            opposed[ccc[0]][ccc[1]] = true;
            opposed[ccc[1]][ccc[0]] = true;
            //cout<<"Opposed "<<ccc[0]<<", "<<ccc[1]<<" = "<<true<<endl;
        }
        cin>>n;
        char word[n+1];
        char ans[n+1];
        int ap=-1;
        clearHasLetter();
        scanf("%s", word);
        FOR(i, n) {
            char &nl = word[i];
            if(ap < 0) {
                ans[ap=0] = nl;
                hasLetter[nl]++;
                continue;
            }
            if(combine[ans[ap]][nl]) {
                hasLetter[ans[ap]]--;
                ans[ap] = combine[ans[ap]][nl];
                continue;
            }
            int j;
            for(j=0;j<8;j++) {
                if(opposed[nl][bases[j]] && hasLetter[bases[j]]) {break;}
            }
            if(j<8) {
                ap=-1;
                clearHasLetter();
                continue;
            }
            hasLetter[nl]++;
            ans[++ap] = nl;
        }
        cout<<"Case #"<<cno<<": [";
        FOR(i, ap+1) {
            if(!i) cout<<ans[i];
            else cout<<", "<<ans[i];
        }
        cout<<']'<<endl;
    }
    return 0;
}
