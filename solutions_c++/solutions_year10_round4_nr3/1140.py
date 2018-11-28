#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1)<<(x))
#define biti(a,i) (((a)>>(i)) & 1)
#define foreach(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n) for(int i=0;i<n;i++)
#define SIZE(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)
#define rint(x) scanf("%d",&x)
#define rdbl(x) scanf("%lf",&x)
#define OUT(x) (cout << #x << " = " << x << endl)
#define  pi  acos(-1)

typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template <class T> void out(T x, int n){  for(int i = 1; i <= n; ++i)  cout <<setw(3)<< x[i] << ' ';    cout << endl;    }
template <class T> void out(T x, int n, int m){  for(int i = 1; i <= n; ++i)    out(x[i], m);    cout << endl;    }
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

const int INF=1000000000;

const int AMAX=505;
int M[AMAX][AMAX];
int D[AMAX][AMAX];

void init(){
    mem(M,0);
}

void append(int x1,int y1,int x2,int y2){
    foreach(i,x1,x2){
        foreach(j,y1,y2){
            M[i][j]=1;
        }
    }
}

void input(){
    int R;
    rint(R);
    while(R--){
        int x1,y1,x2,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        append(x1,y1,x2,y2);
    }
}


int val(int x,int y){
    if(x>=0 && y>=0){
        return M[x][y];
    }
    return 0;
}


int val(int x,int y,int M[AMAX][AMAX]){
    if(x>=0 && y>=0){
        return M[x][y];
    }
    return 0;
}


int calLife2(int (*M)[AMAX],int m,int n){
//    rep(i,10){rep(j,10)cout<<M[i][j]<<" ";cout<<endl;}

    int up(0),left(0);
    int maxLife=0;
    rep(i,m){
        rep(j,n){
            up=val(i-1,j);
            left=val(i,j-1);
            if(M[i][j]){
                if(up || left){
                    M[i][j]=max(up,left)+1;
                }
            }else{
                if(up && left){
                    M[i][j]=max(up,left)+1;
                }
            }
            checkmax(maxLife,M[i][j]);
        }
    }
//    rep(i,10){rep(j,10)cout<<M[i][j]<<" ";cout<<endl;}
    return maxLife;
}
//
int mem[2][AMAX][AMAX];
int calLife(int (*M)[AMAX],int m,int n){
    int (*a)[AMAX],(*b)[AMAX];
    a=mem[0];
    b=mem[1];
    rep(i,m)rep(j,n)a[i][j]=M[i][j];
    int find=0;
    int ret(0);
    find=0;
    rep(i,m)rep(j,n){
        if(a[i][j])find=1;
    }

    if(find==0)return 0;

    do{
        find=0;
        rep(i,m)rep(j,n){
            b[i][j]=a[i][j];
            int up=val(i,j-1,a);
            int left=val(i-1,j,a);
            if(up && left){
                b[i][j]=1;
            }
            if(!up && !left){
                b[i][j]=0;
            }
            if(b[i][j])find=1;
        }

        swap(a,b);
        ret++;
    }while(find);
    return ret;
}


int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
    int go(0);
    cin>>go;
    foreach(i,1,go){
        init();
        input();
        int ans=calLife(M,140,140);
//        int ans=calLife2(M,140,140);
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
	return 0;
}
