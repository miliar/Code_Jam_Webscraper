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

template<class T> void In(T& x){cin>>x;}
template<class T> void In(T arr[], int n){for(int i=0;i<n;i++)cin>>arr[i];}
template<class T> void Out(T arr[], int n){ if(n>0) { cout<<arr[0]; for(int i=1;i<n;i++)cout<<" "<<arr[i];  cout<<endl;} }
ll gcd(ll a,ll b){ll r;while(b){r=a%b;a=b;b=r;}return a;}

int R,C;
char Tiles[52][52];

void Init()
{

}

bool Do()
{
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            if(Tiles[i][j]=='#')
            {
                Tiles[i][j] = '/';
                if(j+1<C && Tiles[i][j+1]=='#') Tiles[i][j+1] = '\\';
                else return false;
                if(i+1<R && Tiles[i+1][j]=='#') Tiles[i+1][j] = '\\';
                else return false;
                if(Tiles[i+1][j+1]=='#')        Tiles[i+1][j+1] = '/';
                else return false;
            }
        }
    }
    return true;
}

int main()
{
    int T;
    In(T);
    for(int kCase=1;kCase<=T;kCase++)
    {
        Init();
        In(R);
        In(C);
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                scanf(" %c", &Tiles[i][j]);
            }
        }

        printf("Case #%d:\n", kCase);
        if(Do())
        {
            for(int i=0;i<R;i++)
            {
                for(int j=0;j<C;j++)
                {
                    putchar(Tiles[i][j]);
                }
                putchar('\n');
            }
        }
        else
        {
            printf("Impossible\n");
        }
    }
}

namespace{
    struct Test
    {
        Test()
        {
            freopen("D:/GCJ/A-large.in","r",stdin);
            freopen("D:/GCJ/A-large.out","w",stdout);
        }

        ~Test()
        {
            //scanf("%*s");
        }
    }g_Test;
}

