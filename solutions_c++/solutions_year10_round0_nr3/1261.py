#include<stdio.h>
#include<string.h>

int g[1024], mark[1024], sum[1024][1024], st[1024];
long long s[1024];

int main()
{
    freopen("c.in", "r", stdin);
    freopen("cL.out", "w", stdout);

    int cc, ct, i, j, L, C;
    int n, r, k, a;
    long long ans;
    
    scanf("%d", &ct);
    for(cc=1; cc<=ct; cc++){
        scanf("%d%d%d", &r, &k, &n);  //printf("%d %d %d\n", r, k, n);
        for(i=0; i<n; i++) scanf("%d", &g[i]);
        
        memset(sum, 0, sizeof(sum));
        memset(mark, 0, sizeof(mark));
        for(i=0; i<n; i++){
            sum[i][i]=g[i];
            for(j=1; j<n; j++) sum[i][(i+j)%n]=sum[i][(i+j-1)%n]+g[(i+j)%n];
        }

        st[0]=0;
        L=1;
        while(1){
            i=st[L-1];
            j=0;
            mark[st[L-1]]=L-1;
            while(j<n && sum[i][(i+j)%n]<=k) j++;
            st[L]=(i+j)%n;
            if(st[L]==0 || mark[st[L]]){
                a=mark[st[L]];
                break;
            }
            L++;
        }

//                   printf("a\n");
        
        for(i=0; i<L; i++) s[i]=sum[st[i]][(st[i+1]-1+n)%n];
        
//        for(i=0; i<L; i++) printf("%d %d %d %I64d\n", i, st[i], (st[i+1]-1+n)%n, s[i]);
//        printf("a=%d\n", a);
        
        for(i=1; i<a; i++) s[i]+=s[i-1];
        for(i=a+1; i<L; i++) s[i]+=s[i-1];
        C=L-a;
        
//        for(i=0; i<L; i++) printf("%d %d\n", i, s[i]);
//        printf("C=%d\n", C);
        
        if(r<=a) ans=s[r-1];
        else{
            ans=s[a-1];
            r-=a;
            ans+=(long long)r/C*s[L-1];
            r%=C;
            if(r>0) ans+=s[a+r-1];
        }
        
        printf("Case #%d: %I64d\n", cc, ans);
    }
    
    return 0;
}
