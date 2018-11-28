#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

int arr[200][200];
double WP[200];
double OWP[200];
double OOWP[200];
int cnt[200];

int solve()
{
    int i,j,k;
    
    int N = ni();
    
    fi(N)
    {
        string s = ns();
        fj(N)
        {
            if(s[j]=='1')
                arr[i][j]=1;
            else if(s[j]=='0')
                arr[i][j]=0;        
            else
                arr[i][j]=-1;
        }
    }
    

    fi(N)
    {
        WP[i]=0;
        cnt[i]=0;
        fj(N)
        {
            if(arr[i][j]>=0)
            {
                cnt[i]++;
                WP[i]+=arr[i][j];    
            }
        } 
        WP[i]/=cnt[i];
    }
    
    fi(N)
    {
        OWP[i]=0;
        fj(N)
        {
            if(arr[i][j]>=0)
            {
                if(arr[i][j]==1)
                    OWP[i] += (WP[j]*cnt[j])/(cnt[j]-1);
                else
                    OWP[i] += (WP[j]*cnt[j]-1)/(cnt[j]-1);
            }
        } 
        OWP[i]/=cnt[i];
    }
    
    fi(N)
    {
        OOWP[i]=0;
        fj(N)
        {
            if(arr[i][j]>=0)
            {
                OOWP[i] += OWP[j];
            }
        } 
        OOWP[i]/=cnt[i];
    }
    
    printf("\n");
    fi(N)
    {
        //printf("%lf\n", WP[i]);
        //printf("%lf\n", OWP[i]);
        //printf("%lf\n", OOWP[i]);
        printf("%lf\n", WP[i]*0.25 + OWP[i]*0.5 + OOWP[i]*0.25);    
        //printf("\n");
        
    }
}

int main( )
{
	int t, tt;

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
        solve();
	}

	return 0;
}
