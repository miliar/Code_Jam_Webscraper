#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long

int l,r;
int lena,lenb,pa,pb;
int sa[100010];
int sb[100010];
    
bool checkanswer(int a, int b) {
    lena=lenb=0;
    pa=pb=0;
    int tmp;
    tmp=a;
    while (tmp) {
        lena++; 
        sa[pa++]=tmp%10;
        tmp/=10;
    }
    tmp=b;
    while (tmp) {
        lenb++; 
        sb[pb++]=tmp%10;
        tmp/=10;
    }
    if (lena!=lenb) return false;
    string aa,bb;
    for (int i=0; i<2*pa; i++) aa+=(sa[i%pa]+'0');
    for (int i=0; i<pb; i++) bb+=(sb[i]+'0');
    if (aa.find(bb)!=string::npos) return true;
    return false;
}

int main() {
    int T, Cas=0;
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);
    cin >> T;
    while(T--) {
        cin >> l >> r;
        int ans=0;
        for (int i=l; i<=r; i++) {
            for (int j=i+1; j<=r; j++) {
                 if(checkanswer(i,j)) ans++;
            }
        }
        Cas++;
        printf("Case #%d: %d\n",Cas,ans);
    }
    return 0;
}

