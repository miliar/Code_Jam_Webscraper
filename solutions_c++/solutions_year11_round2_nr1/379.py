/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;
char str[200][200];
int win[200],loss[200];
double WP[200],OWP[200],AWP[200],OOWP[200];
int games[200];

int main(int argc,char **argv){
    int no,row,col;
    scanf(" %d",&no);
    int tc,j;
    for(tc=1;tc<=no;tc++)
    {
        int n;
        scanf(" %d",&n);
        int i;

        for(i=0;i<n;i++) scanf(" %s",str[i]);

        memset(WP,0,sizeof(WP));
        memset(win,0,sizeof(win));
        memset(loss,0,sizeof(loss));
        memset(games,0,sizeof(games));
        memset(OWP,0,sizeof(OWP));
        memset(AWP,0,sizeof(AWP));
        memset(OOWP,0,sizeof(OOWP));

        for(j=0;j<n;j++){

            for(i=0;str[j][i];i++) {
             if(str[j][i]!='.') games[j]++;
             if(str[j][i]=='1') win[j]++;
             if(str[j][i]=='0') loss[j]++;
            }
            if(games[j]>0)
            WP[j]=win[j]*1./games[j];
            //printf("WP:%.2f\n",WP[j]);
        }

        for(j=0;j<n;j++)
        {
            for(row=0;row<n;row++)
            {
              int x,y,z;
              x=y=z=0;
              for(col=0;col<n;col++)
              {
                if(col == j) continue;
                if(str[row][col]!='.') x++;
                if(str[row][col]=='1') y++;
                if(str[row][col]=='0') z++;
              }
              if(x>0)
              AWP[row]=y*1./x;
             // printf("DWP:%.2f\n",AWP[row]);
            }
            int cnt=0;
            for(row=0;row<n;row++){
                if(str[row][j]!='.')
                OWP[j]+=AWP[row],cnt++;
            }
            if(cnt>0)
            OWP[j]/=cnt;
            //printf("OWP:%.2f\n",OWP[j]);
        }

        for(j=0;j<n;j++)
        {
            int x=0;
            for(col=0;col<n;col++){
                   if(str[j][col]!='.') OOWP[j]+=OWP[col],x++;
            }
            if(x>0)
            OOWP[j]*=1./x;
            //printf("OOWP:%.2f\n",OOWP[j]);
        }
        printf("Case #%d:\n",tc);
        for(i=0;i<n;i++) printf("%.6f\n", (0.25*WP[i]) + (0.5*OWP[i]) +(0.25*OOWP[i]));
    }
    return 0;
}


