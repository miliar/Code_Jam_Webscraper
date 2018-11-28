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
#define rvs(c) reverse(ALL(c))
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
int main( )
{
	int i, j, k, t, tt;
	/*
	our language is impossible to understand
	ejp mysljylc kd kxveddknmc re jsicpdrysi


	there are twenty six factorial possibilities
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd



	so it is okay if you want to just give up
	de kr kd eoya kw aej tysr re ujdr lkgc jv

	aoz
	yeq


	abcdefghijklmnopqrstuvwxyz
	ynficwlbkuomxsevzpdrjgthaq
	*/
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	string english ("abcdefghijklmnopqrstuvwxyz");
	string googlerese ("ynficwlbkuomxsevzpdrjgthaq");
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
		char randomtext[500];
		cin.getline(randomtext,500,'\n');
		string sss(randomtext);
		fi(sss.length()){
			if(sss[i]==' '){
				printf(" ");
				continue;
			}
			fj(googlerese.length()){
				if(sss[i]==googlerese[j]){
					printf("%c",english[j]);
					break;
				}
			}
		}
		printf( "\n");
	}

		/*
		int n1 = ni();
		int n2 = ni();
		int n=n1;
		
		while(n1>0)
		{
			m *= 10;
			m += n%10;
			n1 /= 10;
		}
		cout<<"\nRevesed No:"<<m;
		int n1 = ni();
		fi(tc.size()){
			fj(cs1.size()){
				if(tc[i]==cs1[j]){
					printf("%a",cs11[j]);
					break;
				}
			}
				if(tc[i]==cs2[j]){
					printf("%a",cs21[j]);
					break;
				}
				if(tc[i]==cs3[j]){
					printf("%a",cs31[j]);
					break;
				}
			}	
		}
	}
	
	

	int nums[]={23,2323,23,23,23,232,32,3232,32,3,22,323,2,323,233,23,23,2};
	vi vii(nums,nums+ sizeof(nums) / sizeof(int));
	uniq(vii);
	fi(vii.size()){
		printf("%d \n",vii[i]);
	}
	int d;
	scanf("%d",&d);*/
	return 0;
}
