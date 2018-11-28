#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
double RPI[101];
double WP[101];
double OWP[101];
double OOWP[101];
char Map[101][101];
struct Point
{
    int sum;
    int win;
};
Point p[101];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T;
	int case_num=0;
	scanf("%d",&T);
	while(case_num<T)
	{
	    //RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	    case_num++;
        memset(RPI,0,sizeof(RPI));
        memset(p,0,sizeof(p));
        memset(WP,0,sizeof(WP));
        memset(OWP,0,sizeof(WP));
        memset(OOWP,0,sizeof(WP));
        memset(Map,0,sizeof(Map));
        int N;
        int i,j,k;
        scanf("%d",&N);
        for(i=0;i<N;i++)
        {
            scanf("%s",&Map[i]);
        }
        for(i=0;i<N;i++)
        {
            WP[i]=0;
            p[i].sum=0;
            p[i].win=0;
            for(j=0;j<N;j++)
            {
                if(Map[i][j]!='.')
                {
                    p[i].sum++;
                    if(Map[i][j]=='1')
                    {
                        p[i].win++;
                    }
                }
            }
            if(p[i].sum!=0) WP[i]=p[i].win*1.0/p[i].sum;
        }
        for(i=0;i<N;i++)
        {
            double tempsum=0;
            int fightnum=0;
            for(j=0;j<N;j++)
            {
                if(i!=j && Map[i][j]!='.')
                {
                    int sum=p[j].sum;
                    int win=p[j].win;
                    if(Map[i][j]!='.')
                    fightnum++;
                    if(Map[j][i]!='.')
                    {
                        sum--;
                        if(Map[j][i]=='1')
                        win--;
                    }
                    if(sum!=0)
                    {
                        tempsum+=(win*1.0)/sum;
                    }
                   // cout<<i<<"-->"<<j<<":   "<<win*1.0/sum<<endl;
                }
            }
            if(fightnum==0)
            {
                OWP[i]=0;
            }
            else
            {
                OWP[i]=tempsum/fightnum;
            }
            //cout<<fightnum<<" "<<OWP[i]<<endl;
        }
        for(i=0;i<N;i++)
        {
            double tempsum=0;
            int fightnum=0;
            for(j=0;j<N;j++)
            {
                if(i!=j)
                {
                    if(Map[i][j]!='.')
                    {
                        fightnum++;
                        tempsum+=OWP[j];
                    }
                }
            }
             if(fightnum==0)
            {
                OOWP[i]=0;
            }
            else
            {
                OOWP[i]=tempsum/fightnum;
            }
        }
        printf("Case #%d:\n",case_num);

        for(i=0;i<N;i++)
        {
            RPI[i]=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            printf("%.10lf\n",RPI[i]);
        }

	}

	return 0;
}

