#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;
//#define ONLINE_JUDGE
#define PB push_back
#define MP make_pair
#define CLR(x,y) memset((x),y,sizeof(x))
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)

char comb[256][256];
bool oppo[256][256];
int has[256];
char in_str[1000];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    #endif

    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        int n, comb_n, oppo_n;
        char str[10];
        
        scanf("%d",&comb_n);
        CLR(comb,0);
        CLR(oppo,0);
        
        rep(i,comb_n) {
            scanf("%s", str);
            comb[str[0]][str[1]]=str[2];
            comb[str[1]][str[0]]=str[2];
        }
        scanf("%d",&oppo_n);
        rep(i,oppo_n) {
            scanf("%s", str);
            oppo[str[0]][str[1]]=1;
            oppo[str[1]][str[0]]=1;
        }
        scanf("%d",&n);
        scanf("%s", in_str);
        int loc=0;
        char out_str[1000];
        CLR(has,0);
        rep(i,n) {
            if(i==0) {
                has[in_str[i]]++;
                out_str[loc++]=in_str[i];
            }
            else if(comb[out_str[loc-1]][in_str[i]]) {
                has[out_str[loc-1]]--;
                has[in_str[i]]--;
                out_str[loc-1]=comb[out_str[loc-1]][in_str[i]];
                has[comb[out_str[loc-1]][in_str[i]]]++;
            }
            else {
                bool fin=false;
                rep(j,256) {
                    if(oppo[in_str[i]][j] && has[j]>0) {
                        loc=0;
                        CLR(has,0);   
                        fin=true;                        
                        break;
                    }   
                }
                if(!fin) {
                    has[in_str[i]]++;
                    out_str[loc++]=in_str[i];   
                }   
            }
        }
        printf("Case #%d: [", cas);
        for(int k=0; k<loc-1; k++)
            printf("%c, ",out_str[k]);
        if(loc>0) printf("%c",out_str[loc-1]);
        printf("]\n");
        
    }
    //system("pause");
    return 0;
}
