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

#define QX "C"

bool mk[2000001];
int main()
{
//	freopen("" QX ".txt","r",stdin);
	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int A,B;
    int CC[8];

    int T=0;
	scanf("%d",&T);
    int v[7];
    CC[0]=0;CC[1]=1;CC[2]=3;CC[3]=6;CC[4]=10;CC[5]=15;CC[6]=21;CC[7]=28;
    int bk[8];
    for (int caseId=1;caseId<=T;caseId++)
	{
        cl(mk,0);
        // input
        cin>>A>>B;
        int m=A;
        int D=0,C=0;
        while(m>0){
            m/=10;
            D++;
        }
        For(i,A,B+1){
            if (mk[i]) continue;
            cl(bk,0);
            int k=i;
            rep(j,D) {
                v[j]=k%10;
                k/=10;
            }
            int c=0;
            rep(j,D-1) {
                if (v[j]==0) continue;
                int q=1;
                int V=0;
                For(k,j+1,D) {
                    V+=v[k]*q;
                    q*=10;
                }
                For(k,0,j+1) {
                    V+=v[k]*q;
                    q*=10;
                }
                mk[V]=true;
                if (V>=A && V<=B && V!=i) {
                    bool dup=false;
                    rep(k,c){
                        if (bk[k]==V){dup=true;break;}
                    }
                    if (!dup){
                    bk[c++]=V;
                    //cout<<V<<" ";
                    }
                }
            }
            C+=CC[c];
            if (c>0){
                int r=CC[c];
                //cout<<i<<endl;
            }
        }

        cout << "Case #"<<caseId<<": "<<C<<endl;
	}
    return 0;
}