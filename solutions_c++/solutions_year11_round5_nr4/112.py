#include <math.h>
#include <stdio.h>
#include <string.h>

char s[64];

int ok(long long v){
    long long t,tt,z;
    t = (long long) sqrt(v);
    for (tt=t;tt<t+10;tt++){
        z = tt*tt-v;
        if (z==0) return 1;
        if (z<0) return 0;
    }
    return 0;
}

void solve(int cas){
    int i,j,k,l,c,r;
    long long v;
    scanf("%s",s);
    l=strlen(s);
    c=0;
    for (i=0;i<l;i++){
        if (s[i]=='?') c++;
    }
    r = 0;
    for (k=(1<<c)-1;k>=0;k--){
        j=k;
        v = 0;
        for (i=0;i<l;i++){
            v*=2;
            if (s[i]=='1') v++;
            else if (s[i]=='?'){
                if (j%2) v++;
                j/=2;
            }
        }
        if (ok(v)){
            r = k;
            break;
        }
    }
    for (i=0;i<l;i++){
        if (s[i]=='?'){
            if (r%2) s[i]='1';
            else s[i]='0';
            r/=2;
        }
    }
    printf("Case #%d: %s\n",cas,s);
}

int main(){
    int t,cas;
    scanf("%d",&t);
    cas = 1;
    while (t--) solve(cas++);
    return 0;
}

