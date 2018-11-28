#include<iostream>
#include<cstdio>
using namespace std;

string base = "QWERASDF";
char a[128][128], b[128][128];
char ans[200];
int main()
{
    freopen("1.txt", "r", stdin);
    freopen("jam.txt", "w", stdout);

    int T; cin>>T;
    for(int t=1; t<=T;t++){
        for(int i=0;i<8;i++) for(int j=0;j<8;j++) a[base[i]][base[j]] = b[base[i]][base[j]] = 0;
        int C; cin>>C;
        for(int i=0;i<C;i++){
            string s; cin>>s;
            a[s[0]][s[1]] = s[2];
            a[s[1]][s[0]] = s[2];
        }
        int D; cin>>D;
        for(int i=0;i<D;i++){
            string s; cin>>s;
            b[s[0]][s[1]] = b[s[1]][s[0]] = 1;
        }
        int N; cin>>N;
        string s;
        cin>>s;
        int c = -1;
        for(int i=0; i<N; i++){
            if (c==-1){
                ans[++c] = s[i];
            }
            else if (a[ans[c]][s[i]]){
                ans[c] = a[ans[c]][s[i]];
            }
            else {
                for(int j=0;j<=c;j++){
                    if (b[ans[j]][s[i]]){
                        c=-1;
                        break;
                    }
                }
                if (c==-1) continue;
                else{
                    ans[++c]= s[i];
                }
            }
        }
        printf("Case #%d: [", t);
        for(int i=0;i<=c;i++){
            printf("%c", ans[i]);
            if (i!=c) printf(", ");
        }
        puts("]");
    }
    return 0;
}
