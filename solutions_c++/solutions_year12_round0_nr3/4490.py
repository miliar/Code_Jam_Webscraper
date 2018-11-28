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

char* ssh(char sip[10],int sh,int len)
{
	int i;
	char sop[10];
	sop[len]='\0';

	fi(sh)
	//for(i=0;i<sh;i++)
	{
		sop[i] = sip[ len - sh + i ];
	}

	fo(i,sh,len)
	//for( i=sh; i<len; ++i)
	{
		sop[i] = sip[ i - sh ];
	}
	return sop;
}

int main()
{
	int i, j, k, t, tt;
	int len, T, A, B, cnt;
     	char si[10],sj[10],shs[10];

     	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

     	scanf( "%d\n", &tt );
     	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d %d", &A, &B);
		cnt = 0;
		for( i=A; i<=B; ++i)
		{
			sprintf( si, "%d", i);
			len = strlen(si);
			for( j = A; j <= B; ++j)
			{
				sprintf( sj, "%d", j);
				if( len != strlen(sj) || i == j )
					continue;
				for( k = 1; k < len; ++k)
				{
					strcpy( shs, ssh( sj, k, len ) );
					if( strcmp( si, shs ) == 0)
					{
						cnt++;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, cnt/2);
	}
}
