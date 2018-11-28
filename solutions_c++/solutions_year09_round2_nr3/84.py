#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

const int dx[4]={0,0,1,-1};
const int dy[4]={1,-1,0,0};
const int maxw=20;
char w[maxw][maxw];
const int maxq=350;
const int dq=50;
int n,m,aim;
bool f[2][maxq][maxw][maxw];
string s[2][maxq][maxw][maxw];
int mask;

void gs(){
    char a[10];
    gets(a);
}

void init(){
    int i,j;
    for (i=0;i<n;++i){
        for (j=0;j<n;++j){
            scanf("%c",&w[i][j]);
        }
    gs();
    }
    if (w[0][0]=='+'||w[0][0]=='-') mask=1;
    else mask=0;
}

void cls(int now){
    int i,j,k;
    for (i=0;i<n;++i)
        for (j=0;j<n;++j)
            for (k=0;k<maxq;++k) f[now][k][i][j]=false;
}

inline int calc(int k,int tx1,int ty1,int tx2,int ty2){
    if (w[tx1][ty1]=='+') return k+w[tx2][ty2]-48;
    else return k-w[tx2][ty2]+48;
}

void work(){
    int i,j,now=0,last,k,k1,k2,tx1,tx2,ty1,ty2,t;
    string ts;
    bool found=false;
    cls(0);
    for (i=0;i<n;++i){
        for (j=0;j<n;++j) if ((i+j)%2==mask){
            f[0][w[i][j]-48+dq][i][j]=true;
            s[0][w[i][j]-48+dq][i][j]=string(1,w[i][j]);
            if (w[i][j]-48+dq==aim) found=true;
        }
    }
    while (!found){
        last=now; now=1-now;
        cls(now);
        for (i=0;i<n;++i){
            for (j=0;j<n;++j) if ((i+j)%2==mask){
                for (k=0;k<maxq;++k) if (f[last][k][i][j]){
                    for (k1=0;k1<4;++k1){
                        tx1=i+dx[k1]; ty1=j+dy[k1];
                        if (tx1<0||tx1>=n||ty1<0||ty1>=n) continue;
                        for (k2=0;k2<4;++k2){
                            tx2=tx1+dx[k2]; ty2=ty1+dy[k2];
                            if (tx2<0||tx2>=n||ty2<0||ty2>=n) continue;
                            t=calc(k,tx1,ty1,tx2,ty2);
                            if (t<0||t>=maxq) continue;
                            if (!f[now][t][tx2][ty2]){
                                f[now][t][tx2][ty2]=true;
                                s[now][t][tx2][ty2]=s[last][k][i][j]+w[tx1][ty1]+w[tx2][ty2];
                            }else{
                                ts=s[last][k][i][j]+w[tx1][ty1]+w[tx2][ty2];
                                if (ts<s[now][t][tx2][ty2]) s[now][t][tx2][ty2]=ts;
                            }
                            if (t==aim) found=true;
                        }
                    }
                }
            }
        }
    }
    for (i=0;i<n;++i){
        for (j=0;j<n;++j) if (f[now][aim][i][j]){
            if (found){
                ts=s[now][aim][i][j];
                found=false;
            }
            else if (ts>s[now][aim][i][j]) ts=s[now][aim][i][j];
        }
    }
    cout<<ts<<endl;
}

int main(){
    int Ncase,Ci;
    scanf("%d",&Ncase);
    for (Ci=1;Ci<=Ncase;++Ci){
        printf("Case #%d:\n",Ci);
        scanf("%d%d",&n,&m);
        gs();
        init();
        while (m--){
            scanf("%d",&aim);
            aim+=dq;
            work();
        }
        gs();
    }
    return 0;
}
