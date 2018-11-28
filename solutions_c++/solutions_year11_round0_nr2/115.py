#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <stack>
using namespace std;

const int K=8;
const char BASE[K+1]="QWERASDF";

int Ind(char c)
{
    for(int i=0;BASE[i];i++)
        if(BASE[i]==c)
            return i;
    return K;
}

char turn[K+1][K+1];
bool opps[K][K];
int a[K];
stack<char> res;
char s[200];

void clear_res()
{
    while(!res.empty())
        res.pop();
}

void print_res()
{
    vector<int> vres;
    while(!res.empty())
    {
        vres.push_back(res.top());
        res.pop();
    }
    printf("[");
    for(int i=vres.size()-1;i>=0;i--)
    {
        if(i<vres.size()-1)
            printf(", ");
        printf("%c",vres[i]);
    }
    printf("]");
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        memset(turn,0,sizeof(turn));
        memset(opps,0,sizeof(opps));
        memset(a,0,sizeof(a));
        int c;
        scanf("%d",&c);
        for(int i=0;i<c;i++)
        {
            scanf("%s",s);
            int u=Ind(s[0]),v=Ind(s[1]);
            turn[u][v]=turn[v][u]=s[2];
        }
        int d;
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%s",s);
            int u=Ind(s[0]),v=Ind(s[1]);
            opps[u][v]=opps[v][u]=true;
        }
        int n;
        scanf("%d%s",&n,s);
        for(int i=0;i<n;i++)
        {
            int u=Ind(s[i]);
            bool add=true;
            if(!res.empty())
            {
                int v=Ind(res.top());
                if(turn[v][u]!=0)
                {
                    add=false;
                    a[v]--;
                    res.pop();
                    res.push(turn[u][v]);
                }
            }
            if(add)
            {
                for(int j=0;j<K;j++)
                    if(a[j]>0 && opps[j][u])
                    {
                        add=false;
                        clear_res();
                        memset(a,0,sizeof(a));
                        break;
                    }
            }
            if(add)
            {
                res.push(s[i]);
                a[u]++;
            }
        }
        print_res();
        printf("\n");
    }
    //
    return 0;
}
