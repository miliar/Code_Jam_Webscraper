/// BIS-MILLAHIR RAHMANIR RAHIM

#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>

using namespace std;

#define all(a) a.begin(),a.end()
#define I1(n) scanf("%d",&n)
#define I2(n1,n2) scanf("%d%d",&n1,&n2)
#define I3(n1,n2,n3) scanf("%d%d%d",&n1,&n2,&n3)
#define F(i, a, b) for(  i = (a); i <= (b); i++ )
#define FR(i, a, b) for(  i = (a); i < (b); i++ )
#define FRR(i, a, b) for(  i = (a); i >b; i-- )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Pr(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) cout << *it << " "; cout << endl;
#define pb push_back
#define pi acos(-1.0)
#define MEM(a,val) memset(a,val,sizeof(a))
#define eps 1e-9
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define sz(a) ((int)(a).size())
#define IN  freopen("input.txt","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define CLR(n) n.clear()
#define SQR(n) (n*n)
#define LEFT (idx<<1)
#define RIGHT (LEFT+1)

template<typename T> T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}



char grid[5][5];

int rx[5],cx[5],rt[5],ct[5],ro[5],co[5];

void init()
{
    for(int i=0;i<4;i++)
    {
        rx[i] = cx[i] = rt[i] = ct[i] = ro[i] = co[i] = 0;
    }
}


int main()
{

  //  OUT;
  freopen("A-large.in","r",stdin);
  OUT;

    int tc,cas=1,ans,i,j,k;

  bool flag;

    I1(tc);

    while(tc--)
    {
        init();
        flag = false;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin >> grid[i][j];

                if(grid[i][j]=='X')
                {
                    rx[i]++;
                    cx[j]++;
                }
                else if(grid[i][j]=='O')
                {
                    ro[i]++;
                    co[j]++;
                }
                else if(grid[i][j]=='T')
                {
                    rt[i]++;
                    ct[j]++;
                }
                else
                {
                    flag = true;
                }
            }
        }

        int xx =0,oo = 0;

        for(i=0;i<4;i++)
        {
            if((rx[i]==4) || (rx[i]==3 && rt[i]==1) ) xx++;
            if(ro[i]==4 || (ro[i]==3 && rt[i]==1) ) oo++;

            if(cx[i]==4 || (cx[i]==3 && ct[i]==1) ) xx++;
            if(co[i]==4 || (co[i]==3 && ct[i]==1) ) oo++;
        }


        int dx =0, dc = 0,dt =  0;

        for(i=0;i<4;i++)
        {
            if(grid[i][i]=='X') dx++;
            else if(grid[i][i]=='T') dt++;
            else if(grid[i][i]=='O') dc++;
        }

        if( dx==4 || (dx==3&&dt==1)) xx++;
        if(dc==4 || (dc==3&&dt==1))  oo++;


        dx = dc = dt =  0;

        for(i=0;i<4;i++)
        {
            if(grid[3-i][i]=='X') dx++;
            else if(grid[3-i][i]=='T') dt++;
            else if(grid[3-i][i]=='O') dc++;
        }

        if( dx==4 || (dx==3&&dt==1)) xx++;
        if(dc==4 || (dc==3&&dt==1))  oo++;


        //cout << xx << " asd " << oo << endl;

//        if( (xx&&oo) || (!xx&&!oo) )
//        {
//            if(ans) printf("Case #%d: Game has not completed\n",cas++);
//            else printf("Case #%d: Draw\n",cas++);
//        }
//        else
        {
            if(xx!=0 && oo==0) printf("Case #%d: X won\n",cas++);
            else if(xx==0 && oo!=0) printf("Case #%d: O won\n",cas++);
            else if(flag) printf("Case #%d: Game has not completed\n",cas++);
            else printf("Case #%d: Draw\n",cas++);
        }



    }

    return 0;
}
