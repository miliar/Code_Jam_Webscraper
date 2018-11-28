#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc,n;
    int pos1,pos2;
    scanf("%d",&tc);
    FOR(c,1,tc+1) {
        int num,c1 = 0,c2 = 0;
        int t = 0;
        scanf("%d",&n);
        char arr[101];
        VI v(n);
        pos1 = 1;
        pos2 = 1;
        FOR(i,0,n) {
            scanf("%*c%c%d",&arr[i],&v[i]);
        }
        FOR(i,0,n) {
            if(arr[i] == 'O') {
                int d = abs(v[i] - pos1);
                if(d > c1) {
                     t = t + d + 1 - c1;
                     c2 = c2 + d + 1 - c1;
                }
                else {
                    t++;
                    c2++;
                }
                pos1 = v[i];
                c1 = 0;
            }
            else {
                int d = abs(v[i] - pos2);
                if(d > c2) {
                     t = t + d + 1 - c2;
                     c1 = c1 + d + 1 - c2;
                }
                else {
                    t++;
                    c1++;
                }
                pos2 = v[i];
                c2 = 0;
            }
        }
        printf("Case #%d: %d\n",c,t);
    }
    return (0);
}
