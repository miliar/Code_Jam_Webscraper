#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;

char st[10000];
map< string, int > r;
struct Tree
{
   double num;
   char name[100];
   bool b;
}t[10000];

int mark_tree( int l , int mark )
{
     t[mark].b=false;
     while( st[l]==' ' ) l++;
     t[mark].num=0;
     while( st[l]<='9'&&st[l]>='0' )
     {
          t[mark].num=t[mark].num*10+st[l]-'0';
          l++;
     }
     double q=0.1;
     if( st[l]=='.' ){
       l++;
	   while( st[l]<='9'&&st[l]>='0' )
       {
            t[mark].num=t[mark].num+(st[l]-'0')*q;
            l++;q=q*0.1;
       }
	 }
     while( st[l]==' ' ) l++;
     int k=0;
     while( st[l]>='a'&&st[l]<='z' ) t[mark].name[k++]=st[l++];
     t[mark].name[k]='\0';
     while( st[l]==' ' ) l++;
     if( st[l]==')' ) { t[mark].b=true; l++; while(st[l]==' ') l++; return( l ); }
     if( st[l]=='(' )
       l=mark_tree( l+1 , 2*mark );
     if( st[l]==')' ) {l++; while(st[l]==' ') l++;return( l );}
     if( st[l]=='(' )
       l=mark_tree( l+1 , 2*mark+1 );
     if( st[l]==')' ) {l++; while(st[l]==' ') l++;return( l );}
}

void init()
{
    int i, n;
    char tmp[100];
    scanf( "%d", &n );gets( tmp );
    for( i = 0; i < n; i++ ){
        gets( tmp );
        if( i == 0 ) strcpy( st, tmp );
        else strcat( st, tmp );
    }
}

double dfs( int m, double p ){
    if( t[m].b == true ) return p * t[m].num;
    if( r[t[m].name] == 1 ) return dfs( 2 * m, p * t[m].num );
    else return dfs( 2 * m + 1, p * t[m].num );
}

int main()
{
    int cas, t, i, j, k, q;
    char name[100];
    char w[100];
    double ans;
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-small-attempt0.out", "w", stdout );
    scanf("%d",&t);
    for( cas = 1; cas <= t; cas++ ){
       init( );
       i=0;
       while( st[i]!='(' ) i++;
       mark_tree( i+1 , 1 );
       scanf( "%d", &q );
       printf( "Case #%d:\n", cas );
       for( i = 0; i < q; i++ ){
           scanf( "%s", &name );
           r.clear( );
           scanf( "%d", &k );
           for( j = 0; j < k; j++ ){
               scanf( "%s", &w );
               r[w] = 1;
           }
           double ans = dfs( 1, 1.0 );
           printf( "%.7lf\n", ans );
       }
    }
    return(0);
}
