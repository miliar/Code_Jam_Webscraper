#include<cstdio>
#include<iostream>
#include<string>
#include<map>

using namespace std;

const int maxN=100000+1;

map<string,int> Name;

int data,N,M,S,K,ans;
int F[maxN],G[maxN];
int E[maxN*10][2];

void edge(int x,int y) {
    E[++K][0]=F[x];
    E[K][1]=y;
    F[x]=K;
}

int findname(string s) {
    if (Name.find(s)!=Name.end()) return Name[s];
    return Name[s]=++K;
}

int findpoint(int x,int opt) {
    for (int i=F[x]; i; i=E[i][0])
        if (G[E[i][1]]==opt) return E[i][1];
    return 0;
}
void solve(int plus) {
    char s[10000];
    string ss;
    memset(s,0,sizeof(0));
    gets(s);
    int l=strlen(s);
    s[l]='/';
    int i=0,j=0;
    while (i<=l) {
        if (s[i]=='/') {
            i++; 
            if (i>1) {
                int k=findname(ss);
                int t=findpoint(j,k);
                if (t) j=t; else {
                    ans+=plus;
                    edge(j,++S);
                    j=S;
                    G[j]=k;
                    //cout<<ss<<endl;
                }
            }
            ss="";
        }
        ss+=s[i++];
    }
}

int main() {
    freopen("al.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d\n",&data);
    for (int T=1; T<=data; T++) {
        
        Name.clear();
        S=K=ans=0;
        memset(F,0,sizeof(F));
        
        printf("Case #%d: ",T);
        scanf("%d%d\n",&N,&M);
        for (int i=0; i<N; i++) solve(0);
        for (int i=0; i<M; i++) 
            solve(1);
        
        printf("%d\n",ans);
        
    }
}
