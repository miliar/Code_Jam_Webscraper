//La Ilaha Illallahhu Muhammadur Rasulullah (Sm)


#pragma comment(linker,"/STACK:16777216")
#pragma  warning ( disable: 4786)
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
#include<stack>
#include<cassert>
#include<list>
#include<utility>
#include<bitset>
#include<cstdlib>
#define ll long long ///for code_blocks
//#define ll int ///for vcc
#define filer() freopen("A-large (1).in","r",stdin)
#define filew() freopen("outA.txt","w",stdout)
#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)<(b)?(b):(a))
#define inf 1<<29
#define MAXS 100007
using namespace std;



double wp[107],wop[107],woop[107];
char adj[107][107];
int win[107],los[107];

int main()
{
    int T,N,i,j,ks=0;
    filer();
        filew();
    scanf("%d",&T);
    while(T--)
    {
		memset(wp,0,sizeof(wp));
		memset(wop,0,sizeof(wop));
		memset(woop,0,sizeof(woop));
        memset(adj,0,sizeof(adj));
		memset(win,0,sizeof(win));
		memset(los,0,sizeof(los));
        ks++;
        char ch;
        scanf("%d",&N);

        for(i=0;i<N;i++)
        {
			//V[i].clear();
            for(j=0;j<N;j++)
            {
                cin>>adj[i][j];
                if(adj[i][j]=='1')win[i]++;
                if(adj[i][j]=='0')los[i]++;
            }
            if((win[i]+los[i])<=0)continue;

            wp[i]=(double)win[i]/(win[i]+los[i]);
        }

        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++)
            {
                if(adj[i][j]=='.')continue;
                if((win[i]+los[i])<=1)continue;
                wop[i]+=(double)(win[j]-(adj[j][i]-'0'))/(win[j]+los[j]-1);
            }
            if((win[i]+los[i])<=0)continue;
            wop[i]/=(double)(win[i]+los[i]);
        }


        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++)
            {
                if(adj[i][j]=='.')continue;
                woop[i]+=wop[j];
            }
            if((win[i]+los[i])<=0)continue;
            woop[i]/=(win[i]+los[i]);
        }

        printf("Case #%d:\n",ks);

        for(i=0;i<N;i++)
        {
            printf("%.12lf\n",0.25*wp[i]+ 0.50 *wop[i] + 0.25*woop[i]);
        }

    }
    return 0;
}

