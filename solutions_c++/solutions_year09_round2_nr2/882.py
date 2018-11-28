#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <sstream>
#include <stack>
using namespace std;

void opens(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
}

void openb(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
}

int tes,n,ans,cnt[11],wlen,mini,pos;
char w[30],t[30];
string tmp;

bool ok(int a){
    int cnt2[11];
    memset(cnt2,0,sizeof(cnt2));
    while (a){
        cnt2[a%10]++;
        a/=10;
    }
    for (int i=1;i<=9;i++) if (cnt[i]!=cnt2[i]) return 0;
    return 1;
}

bool same(char a[],char b[]){
    for (int i=0;i<wlen;i++){
        if (a[i]!=b[i]) return 0;
    }
    return 1;
}

bool check(string a){
    string b=a;
    sort(b.begin(),b.end(),greater<char>());
    if (a<b) return 1;
    return 0;
}

int main(){
    //opens();
    openb();
    scanf("%d",&tes);
    for (int i=1;i<=tes;i++){
        scanf("%s",w);
        wlen=strlen(w);
        memcpy(t,w,sizeof(w));
        sort(t,t+wlen,greater<char>());
        if (same(t,w)){
            sort(t,t+wlen);
            printf("Case #%d: ",i);
            mini=100000000;
            for (int j=0;j<strlen(t);j++){
                if (t[j]!='0'){
                    if (mini>(int)t[j]){
                        mini=min(mini,(int)(t[j]));
                        pos=j;
                    }
                }
            }
            printf("%c",mini);
            printf("0");
            for (int j=0;j<strlen(t);j++){
                if (j==pos) continue;
                printf("%c",t[j]);
            }
            printf("\n");
        }
        else {
            for (int j=wlen-1;j>=0;j--){
                tmp="";
                for (int k=j;k<wlen;k++){
                    tmp+=(char)w[k];
                }
                if (check(tmp)){
                    printf("Case #%d: ",i);
                    for (int k=0;k<j;k++){
                        printf("%c",w[k]);
                    }
                    for (int k=j;k<wlen;k++){
                        if (w[k]>w[j]){
                            pos=k;
                        }
                    }
                    printf("%c",w[pos]);
                    w[pos]=-1;
                    sort(w+j,w+wlen);
                    for (int k=j;k<wlen;k++){
                        if (w[k]==-1) continue;
                        printf("%c",w[k]);
                    }
                    printf("\n");
                    break;
                }
            }

        }
    }
    return 0;
}
