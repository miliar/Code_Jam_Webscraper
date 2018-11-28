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

const ll INF=0x3C3C3C3C3C3C3C3C;
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

ll GCD[10002];
ll LCM[10002];

int N;
ll L,H;
ll arr[10002];

ll lcm(ll a, ll b)
{
    if(a>=INF || b>=INF) return INF;
    if(a/gcd(a,b)*b > H)
    {
        return INF;
    }
    else
    {
        return a/gcd(a,b)*b;
    }
}

void Init()
{

}

//给定下(不确)界，返回[b,e)上满足v<*p的最小的p，如果不存在则返回的p不属于[b,e)，事实上是e
template<typename T>
const T* LB(const T* const b, const T* const e, const T& v)
{
    if(b>=e) return e;

    const T* bb = b;
    const T* ee = e;
    while(ee-bb>2)
    {
        const T* mm = bb+(ee-bb)/2;
        if(*mm<=v)
        {
            bb = mm + 1;
        }
        else // v<*p
        {
            ee = mm + 1;
        }
    }

    for(const T* p = bb; p<ee;p++)
    {
        if(v<*p)
        {
            return p;
        }
    }
    return e;
}

int main()
{
    int T;
    In(T);
    for(int kCase = 1; kCase<=T; kCase++)
    {
        Init();
        In(N);
        In(L);In(H);
        In(arr+1,N);

        sort(arr+1,arr+1+N);

        LCM[0] = 1;
        for(int i=1;i<=N;i++)
        {
            LCM[i] = lcm(LCM[i-1],arr[i]);
        }

        GCD[N] = arr[N];
        for(int i=N-1;i>0;i--)
        {
            GCD[i] = gcd(GCD[i+1],arr[i]);
        }


        ll minRes = -1;
        //for(int i=0; i<=N; i++)
        //{
        //    ll l = LCM[i];
        //    if(l>=INF)
        //    {
        //        break;                
        //    }
        //    ll r = (L + l -1) / l * l;
        //    if(r<=H)
        //    {
        //        if(i==N || GCD[i+1]%r==0)
        //        {
        //            if(minRes==-1 || r<minRes)
        //            {
        //                minRes = r;
        //            }
        //        }
        //    }
        //}
        for(ll i=L;i<=H;i++)
        {
            const ll* p = LB(arr+1,arr+1+N, i);
            
            if(p<arr+1+N)
            {
                int idx = p-arr;
                if(i % LCM[idx-1] == 0 && GCD[idx] %i ==0)
                {
                    minRes = i;
                    break;
                }
            }
            else
            {
                int idx = p-arr;
                if(i % LCM[idx-1] == 0)
                {
                    minRes = i;
                    break;
                }
            }
        }

        if(minRes != -1)
        {
            cout<<"Case #"<<kCase<<": "<<minRes<<endl;
        }
        else
        {
            cout<<"Case #"<<kCase<<": NO"<<endl;
        }       
    }
}

namespace{
    struct Test
    {
        Test()
        {
            freopen("D:/GCJ/C-small-attempt3.in","r",stdin);
            freopen("D:/GCJ/C-small-attempt3.out","w",stdout);
        }

        ~Test()
        {
            //scanf("%*s");
        }
    }g_Test;
}

