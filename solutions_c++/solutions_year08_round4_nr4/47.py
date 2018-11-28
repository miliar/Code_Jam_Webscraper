#include <cstdio>
#include <queue>
#include <string>
#include <vector>
using namespace std;

struct arr{
    int state,start,finish;
};
queue <arr> q;
vector <int> list[65540];
int opt[65540][17][17],tot,n;
int delta[17][17],last[17][17];
char str[50010];

int main(){
    while (!q.empty()) q.pop();
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%s",&n,&str);
        int len=strlen(str);
        memset(delta,0,sizeof(delta));
        memset(last,0,sizeof(last));
        for (int i=0;i<(1<<n);++i){
            list[i].clear();
            for (int j=0;j<n;++j) if (((i>>j)&1)==0) list[i].push_back(j);
        }
        for (int i=0;i<n;++i)
            for (int j=0;j<n;++j){
                if (i==j) continue;
                for (int k=0;k*n<len;++k){
                    if (str[k*n+i]==str[k*n+j])
                        ++delta[i][j];
                    if ((k!=0)&&(str[k*n-n+i]==str[k*n+j]))
                        ++last[i][j];
                }
            }
        for (int i=0;i<(1<<n);++i)
            for (int j=0;j<n;++j)
                for (int k=0;k<n;++k)
                    opt[i][j][k]=-1;
        for (int i=0;i<n;++i){
            arr temp;
            temp.state=1<<i;
            temp.start=i;
            temp.finish=i;
            opt[1<<i][i][i]=0;
            q.push(temp);
        }
        int ans=0;
        while (!q.empty()){
            arr cur=q.front(),now;
            now.start=cur.start;
            q.pop();
            if ((cur.state==(1<<n)-1)&&(opt[cur.state][cur.start][cur.finish]+last[cur.finish][cur.start]>ans))
                ans=opt[cur.state][cur.start][cur.finish]+last[cur.finish][cur.start];
            for (int i=0;i<list[cur.state].size();++i){
                int j=list[cur.state][i];
                now.state=cur.state|(1<<j);
                now.finish=j;
                if (opt[now.state][now.start][now.finish]==-1) q.push(now);
                if (opt[cur.state][cur.start][cur.finish]+delta[cur.finish][j]>opt[now.state][now.start][now.finish])
                    opt[now.state][now.start][now.finish]=opt[cur.state][cur.start][cur.finish]+delta[cur.finish][j];
            }
        }
        printf("Case #%d: %d\n",cases+1,len-ans);
    }
    return 0;
}
