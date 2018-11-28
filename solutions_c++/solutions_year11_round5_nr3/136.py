#include<stdio.h>
#include<vector>
using namespace std;
char s[101][104];
int R,C,N;
int To(int x,int y){
    if(x<0)x+=R;
    if(y<0)y+=C;
    x%=R;
    y%=C;
    return x*C+y;
}
struct data{
    int x,y;
};
vector<int>Map[20000],revMap[20000],v[10000],newMap[20000];
int group[20000],rank[20000],cnt,used[20000],M;
void dfs0(int x,int n){
    int i;
    used[x]=cnt;
    for(i=0;i<Map[x].size();i++)
        if(used[Map[x][i]]!=cnt)dfs0(Map[x][i],n);
    rank[--M]=x;
}
int pow(int x,int y){
    int an=1;
    while(y){
        if(y&1){
            an*=x;
        }
        x*=x;
        y>>=1;
    }
    return an;
}
void dfs(int x,int n){
    int i;
    group[x]=M;
    used[x]=cnt;
    for(i=0;i<revMap[x].size();i++){
        if(used[revMap[x][i]]!=cnt){
            dfs(revMap[x][i],n);
        }
        else if(group[revMap[x][i]]!=M){
            newMap[group[revMap[x][i]]].push_back(M);
            newMap[M].push_back(group[revMap[x][i]]);
        }
    }
}
void dfs1(int x){
    int i;
    used[x]=cnt;
    for(i=0;i<newMap[x].size();i++){
        if(used[newMap[x][i]]!=cnt){
            dfs1(newMap[x][i]);
        }
    }
}
void SCC(){
    int i,N2=N<<1;
    cnt++;
    M=N2;
    for(i=0;i<N2;i++){
        if(used[i]!=cnt){
            dfs0(i,N2);
        }
    }
    cnt++;
    for(i=0;i<N2;i++){
        if(used[rank[i]]!=cnt){
            newMap[M].clear();
            dfs(rank[i],N2);
            M++;
        }
    }
    for(i=0;i<N2;i+=2)
        if(group[i]==group[i+1]){
            break;
        }
        else{
            newMap[group[i]].push_back(group[i+1]);
            newMap[group[i+1]].push_back(group[i]);
        }
    if(i<N2){
        puts("0");
        return;
    }
    cnt++;
    int an=0;
    for(i=0;i<M;i++){
        if(used[i]!=cnt){
            dfs1(i);
            an++;
        }
    }
    printf("%d\n",pow(2,an));
}
main(){
    int T,i,j,k,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d%d",&R,&C);
        for(i=0;i<R;i++)scanf("%s",s[i]);
        for(i=0;i<R;i++)
            for(j=0;j<C;j++){
                if(s[i][j]=='|'){
                    v[To(i-1,j)].push_back(To(i,j)*2);
                    v[To(i+1,j)].push_back(To(i,j)*2+1);
                }
                else if(s[i][j]=='/'){
                    v[To(i-1,j+1)].push_back(To(i,j)*2);
                    v[To(i+1,j-1)].push_back(To(i,j)*2+1);
                }
                else if(s[i][j]=='-'){
                    v[To(i,j+1)].push_back(To(i,j)*2);
                    v[To(i,j-1)].push_back(To(i,j)*2+1);
                }
                else{
                    v[To(i-1,j-1)].push_back(To(i,j)*2);
                    v[To(i+1,j+1)].push_back(To(i,j)*2+1);
                }
            }
        N=R*C;
        for(i=0;i<N;i++){
            for(j=0;j<v[i].size();j++)
                for(k=j+1;k<v[i].size();k++){
                    Map[v[i][j]].push_back(v[i][k]^1);
                    Map[v[i][k]].push_back(v[i][j]^1);
                    revMap[v[i][k]^1].push_back(v[i][j]);
                    revMap[v[i][j]^1].push_back(v[i][k]);
                }
        }
        printf("Case #%d: ",t);
        SCC();
        for(i=0;i<N+N;i++)Map[i].clear(),revMap[i].clear();
        for(i=0;i<N;i++)v[i].clear();
    }
}
