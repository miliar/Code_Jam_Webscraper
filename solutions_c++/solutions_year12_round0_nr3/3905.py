
#include <vector>
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
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <ctime>
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;++i)
#define rep(i,n) FOR(i,0,n)
#define IT(c) __typeof((c).begin())
#define FORIT(i,c) for(IT(c) i=(c).begin();i != (c).end();++i)
#define all(c) (c).begin() , (c).end()
#define __(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define mp make_pair
#define sz(a) (a).size()
#define tc int tt;scanf("%d",&tt);while(tt--)
#define INF ((1<<31)-1)
#define dbg(e) cout <<(#e)<<" : "<<e<<'\n'
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("out.out","w",stdout);
    int cas=1;
    tc
    {
        int A,B,no,no2,tem,temp,ans=0;
        cin >> A >> B;
        bool marked[B+1];
           set<pair<int,int> > S;
           map<pair<int,int>,int > M;
        rep(i,B)
         marked[i]=0;
        for(int i=A;i<=B;i++)
        {
            int no =(int) log10(i);
            no2=no;
            temp=i;

            while(no2 >0)
            {
                tem = temp / ( (int)pow(10.0,no));
                temp= temp % ( (int)pow(10.0,no));
                temp = (temp*10) + (tem);
                no2--;
                if((temp>A && temp<B) && i != temp)
                {
                    pair<int,int> c = mp(min(i,temp),max(i,temp));
                  if(M[c]==0)
                   M[c]=1;
                }

            }
        }
        cout<<"Case #"<<cas<<": " << M.size() <<"\n";
    cas++;
    }
}
