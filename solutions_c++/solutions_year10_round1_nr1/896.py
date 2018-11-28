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

const int AMAX=55;
char A[AMAX][AMAX];
char B[AMAX][AMAX];
char C[AMAX][AMAX];
int N;
int K;

const char EMPTY='.';
const char RED='R';
const char BLUE='B';

void init(){
    mem(A,0);
    mem(B,0);
    mem(C,0);
}

void rotate(char A[AMAX][AMAX],char B[AMAX][AMAX],int n){
    rep(i,n){
        rep(j,n){
            B[j][n-i-1]=A[i][j];
        }
    }
}

void fall(char A[AMAX][AMAX],char B[AMAX][AMAX],int n){
    rep(c,n){
        int rr=n-1;
        for(int r=n-1;r>=0;r--){
            if(A[r][c]!=EMPTY){
                B[rr--][c]=A[r][c];
            }
        }
    }
    rep(i,n)rep(j,n){
        if(B[i][j]!=RED && B[i][j]!=BLUE)B[i][j]=EMPTY;
    }
}

int valid(int x,int y,int n){
    if(x>=0 && x<n && y>=0 && y<n)return 1;
    return 0;
}

int isK(char A[AMAX][AMAX],int n,char c,int k){

    rep(ii,n){
        rep(jj,n){
            int cnt(0);
            int i=ii;
            int j=jj;
            rep(kk,k){

                if(!valid(i,j,n))break;
                if(A[i][j]==c){
                    cnt++;
                }else{
                    break;
                }

                i=i;
                j=j+1;
            }
            if(cnt==k){
                return 1;
            }
        }
    }


    rep(ii,n){
        rep(jj,n){
            int cnt(0);
            int i=ii;
            int j=jj;
            rep(kk,k){

                if(!valid(i,j,n))break;
                if(A[i][j]==c){
                    cnt++;
                }else{
                    break;
                }

                i=i+1;
                j=j;
            }
            if(cnt==k){
                return 1;
            }
        }
    }

    rep(ii,n){
        rep(jj,n){
            int cnt(0);
            int i=ii;
            int j=jj;
            rep(kk,k){

                if(!valid(i,j,n))break;
                if(A[i][j]==c){
                    cnt++;
                }else{
                    break;
                }

                i=i+1;
                j=j+1;
            }
            if(cnt==k){
                return 1;
            }
        }
    }

    rep(ii,n){
        rep(jj,n){
            int cnt(0);
            int i=ii;
            int j=jj;
            rep(kk,k){

                if(!valid(i,j,n))break;
                if(A[i][j]==c){
                    cnt++;
                }else{
                    break;
                }

                i=i+1;
                j=j-1;
            }
            if(cnt==k){
                return 1;
            }
        }
    }
    return 0;
}



int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);

    int go;
    rint(go);
    for(int gg=1;gg<=go;gg++){
        init();
        rint(N);
        rint(K);
        getchar();
        rep(i,N){
            rep(j,N){
                char c;
                c=getchar();
                A[i][j]=c;
            }
            getchar();
        }

        rotate(A,B,N);
        fall(B,C,N);
//        rep(i,N){
//            rep(j,N){
//                cout<<C[i][j]<<' ';
//            }
//            cout<<endl;
//        }
        int red=isK(C,N,RED,K);
        int blue=isK(C,N,BLUE,K);
        string ans="Neither";
        if(red==1 && blue==1){
            ans="Both";
        }else if(red==1){
            ans="Red";
        }else if(blue==1){
            ans="Blue";
        }else{
            ans="Neither";
        }

        cout<<"Case #"<<gg<<": "<<ans<<endl;
    }

	return 0;
}
