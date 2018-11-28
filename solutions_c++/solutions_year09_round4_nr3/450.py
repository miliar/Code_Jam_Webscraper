#include<stdio.h>
#include<string.h>

int n, k;
int pr[100][30];
bool g[100][100], found;
int c[100], max;
bool flag[100];

//*******************************
void maxc(bool flag[100], int size)
{
    int i, j, k=0;
    bool mark[100];
    for(i=0; i<n; i++) if(!flag[i]) k++;
    if(!k){
        if(size>max) max=size, found=true;
        return;
    }
    for(i=0; i<n; i++) if(!flag[i]){
        if(size+k<=max) return;
        if(size+c[i]<=max) return;
        flag[i]=1, k--;
        for(j=0; j<n; j++) mark[j]=flag[j];
        for(j=0; j<n; j++) if(!g[i][j]) mark[j]=1;
        maxc(mark, size+1);
        if(found) return;
    }
}

//*******************************


bool con(int i, int j)
{
    int t;
    
    for(t=0; t<k-1; t++)
        if(!((pr[i][t]<pr[j][t] && pr[i][t+1]<pr[j][t+1]) || (pr[i][t]>pr[j][t] && pr[i][t+1]>pr[j][t+1])))
            return 1;
    return 0;
}

void input()
{
    int i, j;
    
    scanf("%d%d", &n, &k);
    for(i=0; i<n; i++)
        for(j=0; j<k; j++) scanf("%d", &pr[i][j]);

    memset(g, 0, sizeof(g));
    for(i=0; i<n; i++)
        for(j=i+1; j<n; j++)
            if(con(i, j)) g[i][j]=g[j][i]=1;    
            
    max=0;
    
    for(i=n-1; i>=0; i--){
        for(j=0; j<=i; j++) flag[j]=1;
        for(j=i+1; j<=n; j++){
            if(g[i][j]) flag[j]=0;
            else flag[j]=1;
        }
        found=false;
        maxc(flag, 1);
        c[i]=max;
    }
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    int cc, ct;
    
    scanf("%d", &ct);
    for(cc=1; cc<=ct; cc++){
        input();
        printf("Case #%d: %d\n", cc, max);
    }
    
    return 0;
}
