#include <vector>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define F(i,n) for (int i=0;i<n;i++)
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;

const int MAXN=12;

int R,C;
char g[30][30];

int encode(const PI &A,const PI &B)
{
    return (((A.x)*12 + A.y) * 12 + B.x)*12 + B.y;
}

void decode(int ret,PI &A,PI &B)
{
    B.y=ret%12;
    ret/=12;
    B.x=ret%12;
    ret/=12;
    A.y=ret%12;
    ret/=12;
    A.x=ret%12;
}

PI tA,tB,A,B;

const int MAX=12*12*12*12+3;
int q[MAX];
int ans[MAX];

int mv[4][2]=
{
    {1,0},
    {0,1},
    {-1,0},
    {0,-1}
};

inline bool stable(const PI &A,const PI &B)
{
    if (A.x==B.x && abs(A.y-B.y)==1) return 1;
    if (A.y==B.y && abs(A.x-B.x)==1) return 1;
    return 0;
}

inline bool isvalid(const PI &P)
{
    if (P.x < 0 || P.x >= R || P.y < 0 || P.y >= C || g[P.x][P.y]=='#') return 0;
    return 1;
}

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
            scanf("%d%d",&R,&C);
            A.x=-1; tA.x=-1;
            B.x=-1;
            Repi(R)
             {
               scanf("%s",g[i]);
               Repj(C)
                {
                 if (g[i][j]=='w' || g[i][j]=='o')
                  {
                         if (A.x==-1) A=MP(i,j);
                         else B=MP(i,j);
                  }
                 if (g[i][j]=='w' || g[i][j]=='x')
                  {
                         if (tA.x==-1) tA=MP(i,j);
                         else tB=MP(i,j);
                  }
                }
             }

            if (B.x==-1)
             {
                    B=MP(0,0);
                    int at=encode(A,B);
            memset(ans,-1,sizeof(ans));
            ans[at]=0;
            q[0]=at;
            int answ=-1;
            for (int st=0,en=1;st<en;st++)
             {
                    decode(q[st],A,B);
                    int cur=ans[q[st]];

                    if ( (A==tA) )
                     {
                            answ=cur;
                            break;
                         }

                //    cout<<" at "<<A.x<<" "<<A.y<<" ; "<<B.x<<" "<<B.y<<" with "<<cur<<" stable "<<stable(A,B)<<"\n";

                    PI P;
                    Repi(4)
                     {
                            P=A; P.x-=mv[i][0]; P.y-=mv[i][1];
                            if (isvalid(P))
                             {
                                    P=A;
                                    P.x+=mv[i][0]; P.y+=mv[i][1];
                                    if (!isvalid(P)) continue;
                                  //  cout<<"         move A to "<<P.x<<" "<<P.y<<"\n";
                                    int next=encode(P,B);
                                    if (ans[next]>-1) continue;
                                    ans[next]=cur+1;
                                    q[en++]=next;
                             }
                      }
                 }
                  cout<<"Case #"<<xx+1<<": "<<answ<<"\n";

             }
            else
            {

            int at=encode(A,B);
            memset(ans,-1,sizeof(ans));
            ans[at]=0;
            q[0]=at;
            int answ=-1;
            for (int st=0,en=1;st<en;st++)
             {
                    decode(q[st],A,B);
                    int cur=ans[q[st]];

                    if ( (A==tA && B==tB ) || (A==tB && B==tA) )
                     {
                            answ=cur;
                            break;
                         }

                //    cout<<" at "<<A.x<<" "<<A.y<<" ; "<<B.x<<" "<<B.y<<" with "<<cur<<" stable "<<stable(A,B)<<"\n";

                    PI P;
                    Repi(4)
                     {
                            P=A; P.x-=mv[i][0]; P.y-=mv[i][1];
                            if (isvalid(P) && P!=B)
                             {
                                    P=A;
                                    P.x+=mv[i][0]; P.y+=mv[i][1];
                                    if (!isvalid(P) || P==B) continue;
                                    if (stable(P,B)==stable(A,B)) continue;
                                  //  cout<<"         move A to "<<P.x<<" "<<P.y<<"\n";
                                    int next=encode(P,B);
                                    if (ans[next]>-1) continue;
                                    ans[next]=cur+1;
                                    q[en++]=next;
                             }
                      }

                    Repi(4)
                     {
                            P=B; P.x-=mv[i][0]; P.y-=mv[i][1];
                            if (isvalid(P) && P!=A)
                             {
                                    P=B;
                                    P.x+=mv[i][0]; P.y+=mv[i][1];
                                   // cout<<"                     stable? b to "<<P.x<<" "<<P.y<<"\n";
                                    if (!isvalid(P) || P==A) continue;
                                    if (stable(A,P)==stable(A,B)) continue;
                                    //cout<<"         move B to "<<P.x<<" "<<P.y<<"\n";
                                    int next=encode(A,P);
                                    if (ans[next]>-1) continue;
                                    ans[next]=cur+1;
                                    q[en++]=next;
                             }
                     }
             }
            cout<<"Case #"<<xx+1<<": "<<answ<<"\n";
           }
     }
    return 0;
}
