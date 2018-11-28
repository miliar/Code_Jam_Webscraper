#include <cstdio>

const int maxn = 2000000 + 1;
int cnt[maxn];
int get(char *s,int i)
{
    char t[10],k = 0;
    int num;
    for(int j = i; s[j]; j++,k++)
        t[k] = s[j];
    for(int j = 0; j < i; j++,k++)
        t[k] = s[j];
    t[k] = 0;
    sscanf(t,"%d",&num);
    return num;
}
int solve(int A,int B)
{
    char s[10];
    int cnt = 0;
    for(int i = A + 1; i <= B; i++){
        sprintf(s,"%d",i);
        for(int j = 1; s[j]; j++){
            if(s[j] == '0') continue;
            int num = get(s,j);
            if(num < i && num >= A)
                cnt++;
        }
    //    printf("%d %d\n",i,cnt);
    }
    return cnt;
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int ncase = 0,T;
    int A,B;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&A,&B);
        int ans = solve(A,B);
        printf("Case #%d: %d\n",++ncase,ans);
    }
    return 0;
}
