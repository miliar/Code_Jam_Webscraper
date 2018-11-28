#include <iostream>
#include <cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<queue>


using namespace std;

int N;

vector<int> map[1010];
bool visit[1010];
bool bfs()
{
    queue<int> que;
    for(int i=1;i<=N;i++)
    {
        for(int k=1;k<=N;k++)visit[k]=false;
        //cout<<i<<endl;
        que.push(i);
        visit[i]=true;
        while(!que.empty())
        {
            int now=que.front();
            //cout<<"now="<<now<<endl;
            que.pop();
            for(int j=0;j<map[now].size();j++)
            {
                int t=map[now][j];
                //cout<<t<<endl;
                if(visit[t])
                {
                    return true;
                }
                else
                {
                    visit[t]=true;
                    que.push(t);
                }
            }
        }
    }
    return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,tmp;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&N);

        for(int n=1;n<=N;n++)
        {
            int count;
            map[n].clear();
            scanf("%d",&count);

            for(int i=1;i<=count;i++)
            {
                scanf("%d",&tmp);
                map[n].push_back(tmp);
            }
        }
        printf("Case #%d: ",t);
        if(bfs())
        {
            printf("Yes\n");
        }
        else printf("No\n");
    }

}
