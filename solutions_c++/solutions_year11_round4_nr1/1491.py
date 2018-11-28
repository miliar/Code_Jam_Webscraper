#include <fstream>
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
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "A"

int L[1001];
int W[1001];
char done[1001];

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
	freopen("" QX "-small-attempt3.in","r",stdin);freopen("" QX "-small-attempt3.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int x,s,r,t,n;
        cin>>x>>s>>r>>t>>n;
        cl(L,0);
        cl(W,0);
        cl(done,0);
        int tb,te;
        int tl=0;
        rep(i,n){
            cin>>tb>>te>>W[i+1];
            W[i+1]+=s;
            L[i+1]=te-tb;
            tl+=L[i+1];
        }
        L[0]=x-tl;
        W[0]=s;
        double tot=0;
        double lt=t;
        int D=r-s;
        while(true){
            int minW=10001;
            int minJ=-1;
            rep(j,n+1){
                if (done[j]) continue;
                if (W[j]<minW){minW=W[j];minJ=j;};
            }
            if (minJ<0) break;
            int i=minJ;
            done[i]=1;
            if (L[i]>0) {
               /* if (lt<0.0000001){
                    lt=0;
                    tot+=((double)L[i])/((double)(W[i]));
                }else*/{
                    double ti=((double)L[i])/((double)(W[i]+D));
                    if (ti<=lt){
                        lt-=ti;
                        tot+=ti;
                    }else{
                        tot+=lt;
                        double ld=((double)L[i])-lt*((double)(W[i]+D));
                        lt=0;
                        tot+=ld/((double)W[i]);
                    }
                }
            }
        }

        // output
        printf("Case #%d: %.6f\n",caseId,tot);
	}
    return 0;
}