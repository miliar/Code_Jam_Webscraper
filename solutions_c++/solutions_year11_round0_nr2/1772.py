#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   ALL(x) 	x.begin(),x.end()
#define   mabs(a)     ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     116
#define  eps      1e-6
int N,C,D;
map<pair<char,char>,char> msi;
set<pair<char,char> > si;
char as[MAXN];
int main()
{
    int T;scanf("%d",&T);
    REP(roud,T)
    {
        printf("Case #%d: ",roud+1);
        string s="";
        msi.clear();si.clear();
        scanf("%d",&C);
        REP(i,C)
        {
            char cs[10];scanf("%s",cs);
            msi[make_pair(cs[0],cs[1])]=cs[2];
            msi[make_pair(cs[1],cs[0])]=cs[2];
        }
        scanf("%d",&D);
        REP(i,D)
        {
            char cs[10];scanf("%s",cs);
            si.insert(make_pair(cs[0],cs[1]));
            si.insert(make_pair(cs[1],cs[0]));
        }
        scanf("%d",&N);scanf("%s",as);
        vector<char> res;
        REP(i,N)
        {
            if(SZ(res)==0) res.push_back(as[i]);
            else
            {
                char lchar=res[SZ(res)-1];
                if(msi.count(make_pair(lchar,as[i]))) res[SZ(res)-1]=msi[make_pair(lchar,as[i])];
                else
                {
                    res.push_back(as[i]);
                    REP(j,SZ(res)-1)
                    {
                        if(si.count(make_pair(res[j],as[i])))
                        {
                            res.clear();
                            break;
                        }
                    }
                }
            }
        }
        printf("[");
        if(SZ(res)>0)
        {
            REP(i,SZ(res)-1) printf("%c, ",res[i]);
            printf("%c",res[SZ(res)-1]);
        }
        printf("]\n");
    }
    return 0;
}
