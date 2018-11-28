#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<set>
using namespace std;

set<int> v;
int low,high;
int solve() {
    int ans = 0;
    char s[10],stemp[10];
    //if(high <= 20) {
        //ans = 0;
    //} else {
        for(int i = low; i < high; ++i) {
            v.clear();
            if(i <= 11) {
                continue;
            }
            itoa(i,s,10);
            int len = strlen(s);
            for(int k = 1; k != len; ++k) {
                for(int j = 0; j != len; ++j) {
                    if(j < k) {
                        stemp[j] = s[j + len -k];
                    } else {
                        stemp[j] = s[j - k];
                    }
                    stemp[len] = '\0';
                }
                if(stemp[0] == '0') {
                    continue;
                }
                int rev = atoi(stemp);
                if(rev <= high && rev > i) {
                    //++ans;
                    //printf("(%d,%d)\n",i,rev);
                    v.insert(rev);
                }
            }
            ans += v.size();
        }
    //}
    return ans;
}
    
int main() {
    //cout<<atoi("0123")<<endl;
    freopen("cc.in","r",stdin);
    freopen("cc.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    for(int i = 1; i <= ca; ++i) {
        scanf("%d%d",&low,&high);
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}
