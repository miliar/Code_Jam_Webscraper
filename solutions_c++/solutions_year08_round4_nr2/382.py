#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
#define MAX 20000
#define min(a,b) ((a)<(b)?(a):(b))

long long ans = 0;
int cases;
int x,changeable[MAX],state[MAX],value[MAX],nodes,desired;
long long m,n,a;
int mm;
int masiv[MAX][2];

#define check(a,b) (masiv[a][b] == -1 ? rec(a,b) : masiv[a][b])

int x1,x2,x3,y1,y2,y3;
int done;
#define abs(a) ((a)>=0? (a): -1*(a))

int main()
{
    freopen("B-small-attempt0.in", "rt", stdin);
    ///freopen("3.out", "wt", stdout);
    FILE * f = fopen("3.out","wt");
    scanf("%d",&cases);
    for(int t=0; t<cases; t++)
    {
        ans = 0;
        cin>>n>>m>>a;
        x1=0;
        x2=0;
        x3=0;
        y1=0;
        y2=0;
        y3=0;
        done=0;
        for(x1=0;x1<=n;x1++)
        {
            for(x3=0;x3<=n;x3++)
            {
                for(y2=0;y2<=m;y2++)
                {
                    for(y3=0;y3<=m;y3++)
                    {
                        if(abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) == a)
                        {
                            cout<<"Case #"<<t+1<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
                            fprintf(f,"Case #%d: %d %d %d %d %d %d\n",t+1,x1,y1,x2,y2,x3,y3);
                            x1=n+1;
                            x2=n+1;
                            x3=n+1;
                            y1=m+1;
                            y2=m+1;
                            y3=m+1;
                            done=1;
                        }
                    }
                }
            }
        }
        if(done==0)
        {
            cout<<"Case #"<<t+1<<": "<<"IMPOSSIBLE"<<endl;
            fprintf(f,"Case #%d: IMPOSSIBLE\n",t+1);
        }
    }
    return 0;
}
