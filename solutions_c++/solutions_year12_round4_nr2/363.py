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
#include <assert.h>

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

#define QX "B"

double x[1002];
double y[1002];
double r[1002];

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-small-attempt2.in","r",stdin);freopen("" QX "-small-attempt2.out","w",stdout);
//	freopen("" QX "-small-attempt3.in","r",stdin);freopen("" QX "-small-attempt3.out","w",stdout);
	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        cl(x,0);
        cl(y,0);
        cl(r,0);
        // input
        int N,W,L;
        cin>>N>>W>>L;
        rep(k,N){
            cin>>r[k];
		}
        double w=0,l=0,yx=0;
        int i=0;
        while(i<N){
            int i0=i++;
            w=r[i0];
            double ml=r[i0];
            x[i0]=0;
            while(i<N && w<W){
                if (w+r[i]>W)
                    break;
                x[i]=w+r[i];
                if (ml<r[i]) ml=r[i];
                w+=2*r[i];
                i++;
            }
            For(j,i0,i) {
                if(i0==0)
                    y[j]=0;
                else
                    y[j]=l+ml;
            }
            yx=y[i0];
            l=y[i0]+ml;
        }
        assert(yx<=L);
        // output
        cout << "Case #"<<caseId<<": ";
        {
        rep(i,N) {
            if (i!=0) cout<<" ";
            printf("%.1f %.1f",x[i], y[i]);
            //cout<<x[i]<<" "<<y[i];
        }
        }
        cout<<endl;
	}
    return 0;
}
