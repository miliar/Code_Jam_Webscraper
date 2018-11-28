#include <cstdio>
#include <cstring>
using namespace std;

int f[11][1050];
int bin[30];
char g[20][20];
int n,m,cases;
bool ok[1050][1050];
bool cp[1050];
int v[1050];

bool can_place(int r,int stat) {
    for (int i=1;i<=m-1;i++) {
        if (((stat&bin[i])!=0) && ((stat&bin[i+1])!=0)) return false;
    }    
    for (int i=1;i<=m;i++) {
        if (((stat&bin[i])!=0) && (g[r][i]=='x')) return false;
    }    
    return true;
}    

bool satisfy(int s1,int s2) {
    for (int i=1;i<=m;i++) {
        if ((s2&bin[i])!=0) {
            if (i>1) {
                if ((s1&bin[i-1])!=0) return false;
            }    
            if (i<m) {
                if ((s1&bin[i+1])!=0) return false;
            }    
        }    
    }        
    return true;
}    

int get_v(int x) {
    int tmp=0;
    for (int i=1;i<=m;i++) 
        if ((x&bin[i])!=0) tmp++;
    return tmp;
}    

void update(int &a,int k) {
    if (k>a) a=k;
}    

int main() {
    char s[1000];
    bin[1]=1;
    for (int i=2;i<=20;i++) bin[i]=bin[i-1]*2;
    scanf("%d",&cases);
    for (int kase=1;kase<=cases;kase++) {
        scanf("%d%d",&n,&m);
        gets(s);
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++) scanf("%c",&g[i][j]);
            gets(s);
        }
        memset(f,-1,sizeof(f));
        int maxm=bin[m+1]-1;
        for (int i=0;i<=maxm;i++) {
            v[i]=get_v(i);
            if (can_place(1,i)) f[1][i]=v[i];
        }
        memset(ok,0,sizeof(ok));
        for (int i=0;i<=maxm;i++)
            for (int j=0;j<=maxm;j++)
                if (satisfy(i,j)) ok[i][j]=1;    
        for (int i=2;i<=n;i++) {
            memset(cp,0,sizeof(cp));
            for (int x=0;x<=maxm;x++)
               if (can_place(i,x)) cp[x]=true;
            for (int last=0;last<=maxm;last++) {
                if (f[i-1][last]==-1) continue;
                for (int now=0;now<=maxm;now++) {
                    if (cp[now] && ok[last][now]) update(f[i][now],f[i-1][last]+v[now]);
                }    
            }    
        }    
        int xmax=-1;
        for (int i=0;i<=maxm;i++) 
            if (f[n][i]>xmax) xmax=f[n][i];
        printf("Case #%d: %d\n",kase,xmax);    
    }    
}    
