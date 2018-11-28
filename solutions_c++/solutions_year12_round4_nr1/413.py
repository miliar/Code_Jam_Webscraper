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
int d[10002];
int l[10002];
int r[10002];

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        cl(d,0);
        cl(l,0);
        cl(r,0);
        // input
		int N,D;
        cin>>N;
        rep(i,N){
           cin>>d[i]>>l[i];
        }
        cin>>D;

        // output
        d[N]=D;
        /*int r=d[0];
        bool work=true;
        int c=r;
        int ii=0;
        For(i,1,N+1) {
            if (d[i]-c <= r) {
                ii = i;
            } else if (ii > 0) {
                r=min(l[ii],d[ii]-c);
                c=d[ii];
                ii=0;
                if (d[i]-c <= r) {
                    ii = i;
                }
            } else {
                work=false;
                break;
            }

        }*/
        bool work=false;
        r[0]=d[0];
        int p=0;
        while(p<N){
            int q=p+1;
            while(q<=N){
                if (d[p]+r[p]>=d[q]) {
                    if (q==N) {
                        work=true;
                        break;
                    }
                    int nr=min(l[q],d[q]-d[p]);
                    if (nr>r[q])
                        r[q]=nr;
                } else {
                    break;
                }
                q++;
            }
            if (work)
                break;
            p++;
        }
        //work=(ii==N);
        std::string final=(work?"YES":"NO");
        cout << "Case #"<<caseId<<": "<<final<<"\n";

	}
    return 0;
}