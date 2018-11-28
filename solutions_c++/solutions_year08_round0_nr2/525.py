#include <iostream>
#include <vector>
#include <queue>
using namespace std ;

struct train
{
	int start ;
	int arrive ;
};

struct node
{
	int start , end ;
	int num , val ;
	node(){}
	node( int start , int end , int num , int val ):start(start),end(end),num(num),val(val){}
};

struct cmp
{
	bool operator()( const node & a , const node & b )
	{
		return a.start > b.start ;
	}
};

struct cmq
{
	bool operator()( const int & a , const int & b )
	{
		return a > b ;
	}
};


int main(){
	int test ;
	freopen("B-large.in" , "r" , stdin) ;
	freopen("B-large.out" , "w" , stdout) ;
	cin >> test ;
	int t = 1 ;
	while( test -- )
	{
		int n ;
		int na , nb ;
		cin >> n >> na >> nb ;
		int i ;
		char s[2] ;
		int h , m ;
		int start , end ;
		priority_queue<node , vector<node> , cmp >Q ;
		priority_queue<int , vector<int> , cmq >A ;
		priority_queue<int , vector<int> , cmq >B ;
		for( i = 0 ; i < na ; i ++ )
		{
			cin >> h ;
			getchar () ;
			cin >> m ;
			start = h * 60 + m ;
			cin >> h ;
			getchar () ;
			cin >> m ;
			end = h * 60 + m ;
			Q.push( node( start , end , 0 ,1 ) ) ;
		}

		for( i = 0 ; i < nb ; i ++ )
		{
			cin >> h ;
			getchar () ;
			cin >> m ;
			start = h * 60 + m ;
			cin >> h ;
			getchar () ;
			cin >> m ;
			end = h * 60 + m ;
			Q.push( node( start , end , 1 ,1 ) ) ;
		}

		node pre ;
		int next ;
		int ca = 0 , cb = 0 ;
		while( !Q.empty () )
		{
			pre = Q.top () ;
			Q.pop() ;
			bool find ;
			if( pre.num == 0 )
			{
				find = false ;
				while( !A.empty () )
				{
					next = A.top () ;
					if( next <= pre.start )
					{
						find = true ;
						A.pop() ;
						break ;
					}
					else
						break ;
				}
				if( find )
				{
					next = pre.end + n ;
					B.push( next ) ;
				}
				else
				{
					ca ++ ;
					B.push( pre.end + n ) ;
				}
			}
			else
			{
				find = false ;
				while( !B.empty () )
				{
					next = B.top () ;
					if( next <= pre.start )
					{
						find = true ;
						B.pop() ;
						break ;
					}
					else
						break ;
				}
				if( find )
				{
					next = pre.end + n ;
					A.push( next ) ;
				}
				else
				{
					cb ++ ;
					A.push( pre.end + n ) ;
				}
			}
		}
		printf("Case #%d: %d %d\n" , t++ , ca , cb ) ;
	}
	return 0 ;
}