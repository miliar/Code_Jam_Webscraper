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

#define QX "B"

char V[501][501];

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        cl(V,0);
        int r,l,D;
        cin>>r>>l>>D;
        rep(i,r){
            rep(j,l){
                cin>>V[i][j];
            }
        }
        int mk1=0;
        For(i,1,r-1){
            For(j,1,l-1){
                For(k,mk1+1,250){
                    ll sx=0;
                    ll sy=0;
                    int x1=j-k;
                    int x2=j+k;
                    int y1=i-k;
                    int y2=i+k;
                    if (x1<0 ||x2>=l||y1<0||y2>=r) break;
                    For(x,x1,x2+1){
                        For(y,y1,y2+1){
                            if (x==x1&&y==y1) continue;
                            if (x==x1&&y==y2) continue;
                            if (x==x2&&y==y1) continue;
                            if (x==x2&&y==y2) continue;
                            sx+=V[y][x]*(x-j);
                            sy+=V[y][x]*(y-i);
                        }
                    }
                    if (sx==0&&sy==0) mk1=k;
                }
            }
        }
        int mk2=mk1>0?mk1:1;
        For(i,1,r-2){
            For(j,1,l-2){
                For(k,mk2+1,250){
                    double sx=0;
                    double sy=0;
                    int x1=j-k+1;
                    int x2=j+k;
                    int y1=i-k+1;
                    int y2=i+k;
                    if (x1<0 ||x2>=l||y1<0||y2>=r) break;
                    For(x,x1,x2+1){
                        For(y,y1,y2+1){
                            if (x==x1&&y==y1) continue;
                            if (x==x1&&y==y2) continue;
                            if (x==x2&&y==y1) continue;
                            if (x==x2&&y==y2) continue;
                            sx+=((double)V[y][x])*(((double)x-(double)j-0.5));
                            sy+=((double)V[y][x])*(((double)y-(double)i-0.5));
                        }
                    }
                    if (sx==0&&sy==0) mk2=k;
                }
            }
        }
        int mk=max(mk1*2+1,mk2*2);
        // output
        if (mk<3)
            cout << "Case #"<<caseId<<": "<<"IMPOSSIBLE"<<"\n";
        else
            cout << "Case #"<<caseId<<": "<<mk<<"\n";


	}
    return 0;
}