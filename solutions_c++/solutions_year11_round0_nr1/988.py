#include<assert.h>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<set>
#include<vector>
#include<queue>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

typedef long long LL;
typedef pair<int,int> pii;

#define MAX_N 105

int N, ROB[MAX_N], POS[MAX_N];
int dist[MAX_N][MAX_N][MAX_N];
bool seen[MAX_N][MAX_N][MAX_N];

int calc()
{
    typedef pair<pii,int> State;

    CLR(seen,0);

    queue<State> Q;
    Q.push(State(pii(1,1),0));
    seen[1][1][0] = 1;
    dist[1][1][0] = 0;

    while(Q.empty()==false)
    {
        State u = Q.front();
        int O = u.first.first, R = u.first.second, k = u.second;
        Q.pop();

        if(k == N){ //cout<<"O "<<O<<" R "<<R<<" k "<<k<<" dist "<<dist[O][R][k]<<"\n";
            return dist[O][R][k];
        }

        REP(DO,-1,1)REP(DR,-1,1) if(DO!=0 || DR!=0)
        {
            int O2 = O+DO, R2 = R+DR;
            if(O2>=1&&O2<=100 && R2>=1&&R2<=100)
            {
                State v(pii(O2,R2),k);
                if(!seen[O2][R2][k])
                {
                    seen[O2][R2][k] = 1;
                    dist[O2][R2][k] = dist[O][R][k]+1;
                    Q.push(v);
                }
            }
        }

        if(ROB[k] == 0 && O == POS[k])
        {
            int DR[] = {0,-1,1};
            // switch press by O
            FOR(i,3)
            {
                int R2 = R+DR[i];
                if(R2>=1&&R2<=100)
                {
                    State v(pii(O,R2),k+1);
                    if(!seen[O][R2][k+1])
                    {
                        seen[O][R2][k+1] = 1;
                        dist[O][R2][k+1] = dist[O][R][k]+1;
                        Q.push(v);
                    }
                }
            }
        }

        if(ROB[k] == 1 && R == POS[k])
        {
            int DO[] = {0,-1,1};
            FOR(i,3)
            {
                int O2 = O+DO[i];
                if(O2>=1&&O2<=100)
                {
                    State v(pii(O2,R),k+1);
                    if(!seen[O2][R][k+1])
                    {
                        seen[O2][R][k+1]=1;
                        dist[O2][R][k+1]=dist[O][R][k]+1;
                        Q.push(v);
                    }
                }
            }
        }
    }

    assert(0); // this point shouldn't be reached
    return -1;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);

    int T; scanf("%d",&T);

    REP(kase,1,T)
    {
        scanf("%d",&N);

        FOR(i,N)
        {
            char rob[5];
            int pos;
            scanf("%s%d",rob,&pos);

            if(rob[0]=='O') ROB[i] = 0;
            else ROB[i] = 1;

            POS[i] = pos;
        }

        printf("Case #%d: %d\n",kase,calc());
    }

    return 0;
}
