#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>


#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

#define deb(a)      cout<<" -> "<<#a<<"  "<<a<<endl;
#define oo          (1<<30)
#define ERR         1e-5
#define PRE         1e-8
#define popcount(a) (__builtin_popcount(a))
#define SZ(a)       ((int)a.size())
#define X           first
#define Y           second
#define PB          push_back
#define LL          long long
#define MP          make_pair
#define ISS         istringstream
#define OSS         ostringstream
#define SS          stringstream
#define VS          vector<string>
#define VI          vector<int>
#define VD          vector<double>
#define VLL         vector<long long>
#define IT          ::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))
#define accu(a,b,c) accumulate((a),(b),(c))
#define fi(i,a,b)   for(i=a;i<b;i++)
#define fd(i,a,b)   for(i=a;i>b;i--)
#define fii(a,b)    for(i=a;i<b;i++)
#define fdi(a,b)    for(i=a;i>b;i--)
#define fij(a,b)    for(j=a;j<b;j++)
#define fdj(a,b)    for(j=a;j>b;j--)
#define fik(a,b)    for(k=a;k<b;k++)
#define fdk(a,b)    for(k=a;k>b;k--)
#define fil(a,b)    for(l=a;l<b;l++)
#define fdl(a,b)    for(l=a;l>b;l--)
#define ri(i,a)     for(i=0;i<a;i++)
#define rd(i,a)     for(i=a;i>-1;i--)
#define rii(a)      for(i=0;i<a;i++)
#define rdi(a)      for(i=a;i>-1;i--)
#define rij(a)      for(j=0;j<a;j++)
#define rdj(a)      for(j=a;j>-1;j--)
#define rik(a)      for(k=0;k<a;k++)
#define rdk(a)      for(k=a;k>-1;k--)
#define ril(a)      for(l=0;l<a;l++)
#define rdl(a)      for(l=a;i>-1;l--)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a)      (a).begin(),(a).end()
#define CROSS(a,b,c,d)  ((b.x-a.x)*(d.y-c.y)-(d.x-c.x)*(b.y-a.y))
#define sqr(a)      ((a)*(a))
#define p2(a)       (1LL<<a)
#define INC(a,b,c)   (b<=a&&a<=c)

//const double pi=2*acos(0.);

template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
template<class ZZ>ZZ max(ZZ a,ZZ b,ZZ c){return max(a,max(b,c));}
template<class ZZ>ZZ min(ZZ a,ZZ b,ZZ c){return min(a,min(b,c));}

//typedef pair< , > pi;
//typedef struct {int x,y;    void print(){printf("%d %d\n",x,y);}}P;
//bool operator < (const P &a,const P &b){return true;}
//bool com(P a,P b){return;}
//struct pq{int n,w;  bool operator<(const pq &b)const{return w>b.w;}};

int co[100][100];
VI v[100];
char bs[] = "QWERASDF";


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    //ios_base::sync_with_stdio(false);

    int i,j,tks,ks=1,n,m,f;
    char a[200],b[200];

    map<char,int>M;

    scanf("%d",&tks);

    while(tks--)
    {
        mem(co,0);
        rii(8)  v[bs[i]].clear();
        M.clear();

        scanf("%d",&n);

        while(n--)
        {
            scanf("%s",a);
            co[a[0]][a[1]] = co[a[1]][a[0]] = a[2];
        }


        scanf("%d",&n);

        while(n--)
        {
            scanf("%s",a);
            v[a[0]].PB(a[1]);
            v[a[1]].PB(a[0]);
        }


        scanf("%d",&n);
        scanf("%s",a);

        f=0;

        rii(n)
        {
            if(f)
            {
                if(co[b[f-1]][a[i]])
                {
                    M[b[f-1]]--;
                    b[f-1] = co[b[f-1]][a[i]];
                    M[b[f-1]]++;
                }
                else
                {

                    for(m=1,j=0;j<SZ(v[a[i]])&&m;j++)
                        if(M[ v[a[i]][j] ]) m=0;

                    if(!m)
                    {
                        f=0;
                        M.clear();
                        continue;
                    }
                    b[f++] = a[i];
                    M[a[i]]++;
                }
            }
            else
            {
                b[f++]=a[i];
                M[a[i]]++;
            }
        }



        printf("Case #%d: [",ks++);

        rii(f)
        {
            if(i)   printf(", ");
            printf("%c",b[i]);
        }
        printf("]\n");
    }


    return 0;
}


