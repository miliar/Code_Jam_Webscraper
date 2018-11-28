/*
  Name: 高精度 
  Copyright:Liu Qipeng
  Author:   Liu Qipeng
  Date: 29-10-09
  Description: + - * / % 
               == < <=
               gcd lcm 
*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<bitset>
using namespace std;
FILE *fin=freopen( "B.in" , "r"  ,stdin );
FILE *fout=freopen( "B.out" , "w" ,stdout );
const long long mod=1000000;
struct bignum{
       long long a[ 100 ];
       int l;
       bignum( int t=0 ){
                memset( a , 0 , sizeof a );
                l=0;
                for(  ; t ; t/=mod )
                  a[ l++ ]=t%mod;
       }
       void read(){   //  读入 
            char s[ 1100 ];
            fscanf( fin , "%s" , s);
            for( int i=strlen( s )-1 ; i>=0 ; i=max( i-6 , -1 ) ){
                 long long tmp=0;
                 for( int j=max( 0 , i-5 ) ; j<=i ; j++)
                   tmp=tmp*10+s[ j ]-'0';
                 a[ l++ ]=tmp;
            }
            if( !l ) l=1;  //  0 的情况 
       }
       void carry(){
            l+=5;  //  补长度 
            for( int i=0 ; i<l ; i++)
              if( a[ i ]>=mod ){
                  a[ i+1 ]+=a[ i ]/mod;
                  a[ i ]%=mod;
              }
            while( l>1 && !a[ l-1 ] ) l--;
       }    
       bool operator<=( const bignum&t ) const{
            if( l!=t.l ) return l<t.l;
            for( int i=l-1 ; i>=0 ; i--)
              if( a[ i ]!=t.a[ i ] ) return a[ i ]<t.a[ i ];
            return 1;
       }
       bool operator==( const bignum&t ) const{
            if( l!=t.l ) return 0;
            for( int i=l-1 ; i>=0 ; i--)
              if( a[ i ]!=t.a[ i ] ) return 0;
            return 1;
       }
       bool operator!=( const bignum&t ) const{
            if( l!=t.l ) return 1;
            for( int i=l-1 ; i>=0 ; i--)
              if( a[ i ]!=t.a[ i ] ) return 1;
            return 0;
       }
       bool operator<( const bignum&t ) const{
            if( l!=t.l ) return l<t.l;
            for( int i=l-1 ; i>=0 ; i--)
              if( a[ i ]!=t.a[ i ] ) return a[ i ]<t.a[ i ];
            return 0;
       }
       bignum operator+( const int&t ) const{
              bignum c=*this;
              c.a[ 0 ]+=t;
              c.carry();
              return c;
       }
       bignum operator+( const bignum&t ) const{
              bignum c;
              c.l=max( l , t.l );
              for( int i=0 ; i<c.l ; i++)
                c.a[ i ]=a[ i ]+t.a[ i ];
              c.carry();
              return c;
       }
       bignum operator*( const bignum&t ) const{
              bignum c;
              c.l=l+t.l;
              for( int i=0 ; i<l ; i++)
                for( int j=0 ; j<t.l ; j++)
                  c.a[ i+j ]+=a[ i ]*t.a[ j ];   //  乘法 
              c.carry();
              return c;
       }
       bignum operator/( const int&t ) const{
              bignum c;
              c.l=l;
              long long ret=0;
              for( int i=l-1 ; i>=0 ; i--){  //  模拟除法 
                   ret=ret*mod+a[ i ];
                   c.a[ i ]=ret/t;
                   ret%=t;
              }
              c.carry();
              return c;
       }
       bignum operator/( const bignum&t ) const{ //  *this>=t 有bug
            //    if( t==(*this) ) return bignum(1);   //  特判 
                bignum l , r=*this , mid , tmp;
                r=r+1;    //  注意 r>=*this+1 不是 *this 
                while( l+1<r ){   //  二分除法 
                       mid=(l+r)/2;
                       tmp=t*mid;
                       if( tmp<=*this ) l=mid;
                       else r=mid;
                }
                return l;
       }
       bignum operator-( const bignum &t ) const{
              bignum c;
              c.l=max( l , t.l ); //  最大位数 
              for( int i=0 ; i<c.l ; i++)
                c.a[ i ]=a[ i ]-t.a[ i ];
              for( int i=1 ; i<c.l ; i++)  //  从最低位开始进位 
                while( c.a[ i-1 ]<0 ){
                       c.a[ i-1 ]+=mod;
                       c.a[ i ]--;
                }
              c.l+=5;
              while( c.l>1 && !c.a[ c.l-1 ] ) c.l--;
              return c;
       }
       bignum operator%( const bignum &t ) const{   //  取模 
              bignum c=*this/t;
              return *this-t*c;
       }
       void print(){
            fprintf( fout , "%lld" , a[ l-1 ] );
            for( int i=l-2 ; i>=0 ; i--)
              fprintf( fout , "%06lld" , a[ i ] );
            fprintf( fout , "");
       }
}a[1111],b[1111];

bignum gcd( bignum a , bignum b )
{
       if( a<b ) swap( a , b );  //     强制 a > b 
       if( b.a[ 0 ]==0 && b.l==1 ) return a;
       return gcd( b , a%b );
}

bignum lcm( bignum a , bignum b )
{
       return a/gcd( a , b )*b;
}


int main(){
	int Test,N;
	cin >> Test;
	for(int c=1;c<=Test;c++){
		cin >> N;
		printf("Case #%d: ",c);
		memset(a,0,sizeof(a));
		for(int i=1;i<=N;i++)
			a[i].read();
		for(int i=1;i<N;i++){
			if(a[i]<a[i+1])
				b[i]=a[i+1]-a[i];
			else
				b[i]=a[i]-a[i+1];
		}
		bignum g=b[1];
		for(int i=2;i<N;i++)
			g=gcd(g,b[i]);
		bignum ans=(g-a[1]%g)%g;
		ans.print();
		printf("\n");
	}
	return 0;
}

