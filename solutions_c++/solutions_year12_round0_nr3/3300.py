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
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define st(v) sort(all( (v) ))
#define rvs(c) reverse(all( (c) ))
#define uniq(c) st(c),(c).resize(unique(all(c))-(c).begin())

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
template<typename T>
void removeDuplicates(vector<T>& vec)
{
    st(vec);
	vec.erase(unique(all(vec)));
}
int zerocount(int p){
//get number of digits
			int p2 =p,nd=0;
			while(p2>0){
				
				if(p2>0)
				{
					nd++;
				}
				else{
					break;
				}
				p2= p2/10;
				
			}
			return nd;
}
int main( )
{
	int i, j, k, t, tt;
	
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
		int a = ni(),b = ni(),p=a,ans=0,nd=0,sm,p2,p3,p4;
		while(p<b){
			if(p<10){
				p+=10;
				continue;
			}
			//reverse p

			
			//get number of digits
			p2 =p;
			nd=0;
			while(p2>0){
				
				if(p2>0)
				{
					nd++;
				}
				else{
					break;
				}
				p2= p2/10;
				
			}
			
			
			if(p==0) nd=1;


			p3 =p;
			int kd=0,mj,kj=p,bn;
			mj=p;
			fj((nd-1)){
				//get last digit
				
				kd=p3%10;
				p3/=10;
				bn = (int)(pow((double)10,(double)(nd-1))*kd);
				//add digit to end of number
				sm = p3+bn;
				if(sm>a&&sm<=b&&sm>p&&zerocount(sm)==zerocount(p)) ans++;
				
				p3=sm;
			}
			
			
			/*
			if(p==(a+3)){
				printf( "mj :%d p :%d p3 :%d sm: %d nd: %d ld: %d bn: %d\n",mj,p,p3,sm,nd,kd,bn);
				break;
			}
			*/
			
			
			p=p+1;
		}
			
		

		printf( "%d\n",ans);
	}

		
	return 0;
}
