#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
using namespace std;

int mas[101][101];
double WP[101];
double OWP[101];
double OOWP[101];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    int n;
    int cur;
    char in;
    scanf("%d",&cases);
    for(int ic=1;ic<cases+1;ic++)
    {
        cur=0;
        scanf("%d",&n);
        scanf("%c",&in);
        int nu;
        for(int i=0;i<n;i++)
        {
            nu=0;
            cur=0;
            for(int j=0;j<n;j++)
            {
                scanf("%c",&in);
                if(j==i)continue;
                if(in=='1')
                {
                    cur++;
                    mas[i][j]=1;
                    nu++;
                }
                else if(in=='0')
                {
                    mas[i][j]=2;
                    nu++;
                }
                else if(in=='.')
                {
                    mas[i][j]=0;
                }
            }
            scanf("%c",&in);
            WP[i]=double(cur)/(nu);
        }
        cur = 0;
        double tmp;
        int ne;
        for(int i=0;i<n;i++)
        {
            ne=0;
            tmp=0;
            for(int j=0;j<n;j++)
            {
                if(mas[i][j])
                {
                    ne++;
                    nu=0;
                    cur=0;
                    for(int c=0;c<n;c++)
                    {
                        if(i!=c)
                        {
                            if(mas[j][c])
                            {
                                nu++;
                                if(mas[j][c]==1)cur++;
                            }
                        }
                    }
                    tmp+=(double(cur)/nu);
                }
            }
            OWP[i]=tmp/ne;
        }
        for(int i=0;i<n;i++)
        {
            tmp=0;
            nu=0;
            for(int j=0;j<n;j++)
            {
                if(mas[i][j]){tmp+=OWP[j];nu++;}
            }
            OOWP[i]=tmp/nu;
        }
        printf("Case #%d:\n",ic);
        for(int i=0;i<n;i++)
        {
            printf("%.9lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
            //printf("%.6lf %.6lf %.6lf\n",WP[i],OWP[i],OOWP[i]);
        }
    }
    return 0;
}
