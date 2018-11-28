#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<utility>
using namespace std;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ll long long
#define MAX_SIZE 200005
#define MOD 1000000007
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define SC(x) scanf("%c",&x)
#define SS(x) scanf("%s",x)
#define SZ(x) x.size()
#define IT iterator
#define PI pair<int,int>
#define PL pair<ll,ll>
#define VI vector<int>
#define VL vector<ll>
#define VVI vector< VI >
#define VVL vector< VL >
#define VVP vector< PI >
#define READ() freopen("C:\\Users\\Tarun Sapra\\Desktop\\input.txt","r",stdin)
#define WRITE() freopen("C:\\Users\\Tarun Sapra\\Desktop\\output.txt","w",stdout)
#define dump() SC(dump_char)
int dump_char;

int main()
{
    char bd[4][4],start;
    int T,t,i,j,flag,blank;
    READ();
    WRITE();
    S(T);dump();
    for(t=1;t<=T;t++)
    {
        flag=0;blank=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                bd[i][j]=getchar();
                //printf("input is %c\t",bd[i][j]);
                if(bd[i][j]=='.')
                    blank=1;
            }
            //printf("\n");
            dump();
        }
        dump();
        flag=0;
        for(i=0;i<4;i++)
        {
            start=bd[i][0];
            if(start=='T')
                start=bd[i][1];
            for(j=1;j<4;j++)
            {
                if(bd[i][j]=='.'||(bd[i][j]!='T' && bd[i][j]!=start))
                    break;
            }
            if(j==4)
            {
                flag=1;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %c won\n",t,start);
            continue;
        }
        for(i=0;i<4;i++)
        {
            start=bd[0][i];
            if(start=='T')
                start=bd[1][i];
            for(j=1;j<4;j++)
            {
                if(bd[j][i]=='.' || (bd[j][i]!='T' && bd[j][i]!=start))
                    break;
            }
            if(j==4)
            {
                flag=1;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %c won\n",t,start);
            continue;
        }
        start=bd[0][0];
        if(bd[0][0]=='T')
            start=bd[1][1];
        if(start!='.' && (bd[1][1]==start||bd[1][1]=='T') && (bd[2][2]==start||bd[2][2]=='T') && (bd[3][3]==start||bd[3][3]=='T'))
        {
            printf("Case #%d: %c won\n",t,start);
            continue;
        }
        start=bd[0][3];
        if(bd[0][3]=='T')
            start=bd[1][2];
        if(start!='.' && (bd[1][2]==start||bd[1][2]=='T') && (bd[2][1]==start||bd[2][1]=='T') && (bd[3][0]==start||bd[3][0]=='T'))
        {
            printf("Case #%d: %c won\n",t,start);
            continue;
        }
        if(blank)
        {
            printf("Case #%d: Game has not completed\n",t);
            continue;
        }
        printf("Case #%d: Draw\n",t);
    }
    return 0;

}
