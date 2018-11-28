#include <iostream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <complex>
#include <cmath>
#include <deque>
#include <stack>
#include <queue>
#include <ctime>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

const int INF=0x3C3C3C3C;
#define mset(a,x) memset(a,x,sizeof(a))
#define Abs(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define For(I,N) for(int I=0;I<(N);I++)
#define For2(I,A,B) for(int I=(A); (A)<=(B)?(I<=(B)):(I>=(B)); (A)<=(B)?(I++):(I--))
#define ArrSize(x) (sizeof(x)/sizeof(x[0]))

template<class T> void In(T& x){cin>>x;}
template<class T> void In(T arr[], int n){for(int i=0;i<n;i++)cin>>arr[i];}
template<class T> void Out(T arr[], int n){ if(n>0) { cout<<arr[0]; for(int i=1;i<n;i++)cout<<" "<<arr[i];  cout<<endl;} }
ll gcd(ll a,ll b){ll r;while(b){r=a%b;a=b;b=r;}return a;}

const int MaxSize = 10005;

class UFSets {
private:
    int parent[MaxSize+1];
    int size;
public:
    UFSets (int s =MaxSize  ){
        size = s;
        memset(parent,-1,sizeof(parent));
    }

    void clear()
    {
        memset(parent,-1,sizeof(parent));
    }

    int Find (int x){
        if ( parent[x] <0 ) return x;
        else return parent[x]=Find (parent[x]);
    }

    void   Union (int v1, int v2){
        int s1=Find(v1),s2=Find(v2);
        if(s1==s2)return;
        int t = parent[s1] + parent[s2];
        if ( parent[s2] < parent[s1] ) {
            parent[s1] = s2;
            parent[s2] = t;
        }
        else { 
            parent[s2] = s1;
            parent[s1] = t;
        }
    }

    int Count (int x){
        return -parent[Find(x)];
    }
};


int H,W;
int arr[105][105];

int Index(int i,int j)
{
    return i*W+j;
}

UFSets ufset;
char Label[10005];

void Init()
{
    ufset.clear();
    memset(Label,0,sizeof(Label));
    memset(arr,0,sizeof(arr));
}

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

int main()
{
    int kcase = 0;
    int T;
    scanf("%d",&T);
    while(T--)
    {
        Init();
        scanf("%d%d",&H,&W);
        for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }

        for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                int minV=INF,minIndex;
                for(int k=0;k<4;k++)
                {
                    int nx = i+dx[k];
                    int ny = j+dy[k];
                    if(0<=nx && nx<H && 0<=ny && ny<W)
                    {
                        if(arr[nx][ny]<arr[i][j] && arr[nx][ny]<minV)
                        {
                            minV=arr[nx][ny];
                            minIndex = Index(nx,ny);
                        }
                    }
                }
                if(minV!=INF)
                {
                    ufset.Union(minIndex,Index(i,j));
                }
            }
        }

        char lab = 'a';

        for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                if(Label[ufset.Find(Index(i,j))] == 0)
                {
                    Label[ufset.Find(Index(i,j))] = lab++;
                }
            }
        }

        printf("Case #%d:\n",++kcase);

        for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                putchar(Label[ufset.Find(Index(i,j))]);
                if(j!=W-1)
                {
                    putchar(' ');
                }
            }
            putchar('\n');
        }
    }
}
