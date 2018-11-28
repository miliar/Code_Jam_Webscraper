#include<stdio.h>
#include<string.h>

int L, d, n, ans;
char dic[5000][20];
char str[1000];
bool wrd[20][30];

void input()
{
    int i;
    scanf("%d%d%d", &L, &d, &n);
    for(i=0; i<d; i++) scanf("%s", &dic[i]);
}

bool check(char *str)
{
    int i;
    for(i=0; i<L; i++)
        if(!wrd[i][str[i]-'a']) return 0;
    return 1;
}

void solve()
{
    int m, i, j, t;
    
    scanf("%s", &str);
    m=strlen(str);
    
    memset(wrd, 0, sizeof(wrd));
    i=0;
    t=0;
    while(i<m){
        if(str[i]=='('){
            for(j=i+1; str[j]!=')'; j++) wrd[t][str[j]-'a']=1;
            i=j+1;
        }
        else{
            wrd[t][str[i]-'a']=1;
            i++;
        }
        t++;
    }
    
    ans=0;
    for(i=0; i<d; i++)
        if(check(dic[i])) ans++;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
 
    int cc;
 
    input();
    for(cc=1; cc<=n; cc++){
        solve();
        printf("Case #%d: %d\n", cc, ans);
    }
    
    return 0;
}
