#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
#define MAX 20000
#define min(a,b) ((a)<(b)?(a):(b))

long long ans = 0;
int n, cases;
int x,changeable[MAX],state[MAX],value[MAX],nodes,desired;
int m;
int mm;
int masiv[MAX][2];

#define check(a,b) (masiv[a][b] == -1 ? rec(a,b) : masiv[a][b])

int rec(int x, int desired)
{
    if(x>=mm)
    {
        masiv[x][value[x]]=0;
        masiv[x][1-value[x]]=9999999;
        return masiv[x][desired];
        /*
        if(value[x]==desired)
        {
            masiv[x][desired]=0;
            return 0;
        }
        else
        {
            masiv[x][desired]=9999999;
            return 9999999;
        }
        */
    }
    check(x*2, 0);
    check(x*2+1, 0);
    check(x*2, 1);
    check(x*2+1, 1);

    if(changeable[x] == 0)
    {
        //1 = AND, 0 = OR
        if(state[x]==1)
        {
            masiv[x][1] = masiv[x*2][1] + masiv[x*2+1][1];            
            masiv[x][0] = min(masiv[x*2][0],masiv[x*2+1][0]);            
        }
        if(state[x]==0)
        {
            masiv[x][1] = min(masiv[x*2][1],masiv[x*2+1][1]);
            masiv[x][0] = masiv[x*2][0] + masiv[x*2+1][0];            
        }
    }

    if(changeable[x]==1)
    {
        if(state[x]==1)
        {
            masiv[x][1] = masiv[x*2][1] + masiv[x*2+1][1];  
            masiv[x][1] = min(masiv[x][1],min(masiv[x*2][1],masiv[x*2+1][1]) + 1);
            
            masiv[x][0] = min(masiv[x*2][0],masiv[x*2+1][0]);
            masiv[x][0] = min(masiv[x][0],masiv[x*2][0] + masiv[x*2+1][0] +1);
        }

        if(state[x]==0)
        {
            masiv[x][1] = min(masiv[x*2][1], masiv[x*2+1][1]);
            masiv[x][1] = min(masiv[x][1], masiv[x*2][1] + masiv[x*2+1][1]+1);
            
            masiv[x][0] = masiv[x*2][0] + masiv[x*2+1][0];            
            masiv[x][0] = min(masiv[x][0], min(masiv[x*2][0],masiv[x*2+1][0])+1);
        }
    }

    return masiv[x][desired];
}

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("3.out", "wt", stdout);
    scanf("%d",&cases);
    for(int t=0; t<cases; t++)
    {
        scanf("%d%d",&m,&desired);
        for(x=0;x<=m;x++)
        {
            masiv[x][0]=-1;
            masiv[x][1]=-1;
        }
        //interior
        for(x=1;x<=(m-1)/2;x++)
        {
            //printf("%d\n",x);
            scanf("%d%d",&state[x],&changeable[x]);
        }
        mm=(m+1)/2;
        for(x=0;x<(m+1)/2;x++)
        {
            //printf("%d\n",x+mm);
            scanf("%d",&value[x+mm]);
        }
        ans = 0;
        ans = rec(1,desired);
        /*
        for(x=0;x<10;x++)
        {
            printf("Node %d - %d %d\n",x,masiv[x][0],masiv[x][1]);
        }
        */
        if(ans<9999999)
            cout<<"Case #"<<t+1<<": "<<ans<<endl;
        else cout<<"Case #"<<t+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
