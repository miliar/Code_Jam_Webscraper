#include<stdio.h>
#include<math.h>
#include<stdlib.h>

const int maxn=100000000;

int D, I, M, n;
int s[200];
int f[200][300];

void input()
{
    int i;
    scanf("%d%d%d%d", &D, &I, &M, &n);
    for(i=0; i<n; i++) scanf("%d", &s[i]);
}

void solve()
{
    int i, j, a, b, del, tmp, best;
    
    for(i=n-1; i>=0; i--)
        for(a=0; a<=255; a++){
            del=abs(s[i]-a);
            best=maxn;
            for(j=i+1; j<=i+1; j++)
                for(b=0; b<=255; b++){
                    tmp=del+(j-i-1)*D+f[j][b];
                    if(M==0 && a!=b) tmp=maxn;
                    else if(M==0 && a==b){}
                    else{
                        tmp+=abs(a-b)/M*I;
                        if(M>0 && a!=b && abs(a-b)%M==0) tmp-=I; 
                    }
                    if(tmp<best) best=tmp;
                }
            del+=(n-(i+1))*D;
            if(del<best) best=del;
            f[i][a]=best;
            if(i<n-1 && f[i+1][a]+D<f[i][a]) f[i][a]=f[i+1][a]+D;
        }
        
    //printf("%d\n", f[1][3]);
}

void ans()
{
    int ret, tmp, i, a;
    
    ret=D*n;
    for(i=0; i<n; i++)
        for(a=0; a<=255; a++){
            tmp=i*D+f[i][a];
            if(tmp<ret) ret=tmp;
        }
        
    printf("%d\n", ret);
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int T, tt;
    
    scanf("%d", &T);
    for(tt=1; tt<=T; tt++){
        printf("Case #%d: ", tt);
        input();
        solve();
        ans();
    }
    
    return 0;
}
