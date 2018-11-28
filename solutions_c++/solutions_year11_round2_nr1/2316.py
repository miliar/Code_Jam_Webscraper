#include<cstdio>
char t[102][102];
double wp[101];
double owp[101];
double oowp[101];
int n;
int caso;
void f(int x){
    double aux=0;
    int ct=0;
    for(int i=0;i<n;i++){
        if(t[x][i]!='.'){
            aux+=owp[i];
            ct++;
            }
        }
    oowp[x]=aux/ct;
    printf("%lf\n",0.25*wp[x]+0.5*owp[x]+0.25*oowp[x]);
    }
void pci(int x){
    int ct=0,w=0;
    double aux=0;
    for(int i=0;i<n;i++){
        if(t[x][i]!='.'){
            ct++;
            if(t[x][i]=='1')w++;
            int ct2=0,w2=0;
            for(int j=0;j<n;j++){
                if(x!=j && t[i][j]!='.'){
                    ct2++;
                    if(t[i][j]=='1')w2++;
                    }
                }
            aux+=(w2*1.0/ct2);
            }
        }
    owp[x]=aux/ct;
    wp[x]=w*1.0/ct;
    }
void doit(){
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%s",t[i]);
    for(int i=0;i<n;i++)pci(i);
    printf("Case #%d:\n",++caso);
    for(int i=0;i<n;i++)f(i);
    }
int main(){
    int C;
    caso=0;
    scanf("%d",&C);
    for(int i=0;i<C;i++)doit();
    }
