#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
struct Time {
	int m,s;
	Time(int M = 0 ,int S = 0) {
		m = M;
		s = S;
	}
};
Time operator + ( Time a , Time b )
{
	Time res;
	res.m = a.m + b.m;
	res.s = a.s + b.s ;
	if( res.s >= 60 ) {
		res.m += res.s / 60;
		res.s %= 60;
	}
	return res;

}
bool operator < ( Time a , Time b )
{
	return a.m < b.m || a.m == b.m && a.s < b.s;	
}
bool operator > ( Time a , Time b )
{
	return a.m > b.m || a.m == b.m && a.s > b.s;	
}
bool operator == ( Time a , Time b)
{
	return a.m == b.m && a.s == b.s;
}

bool operator <= ( Time a , Time b )
{
	return a < b || a == b;	
}

struct node {
	Time start , end;
	int na;
};
bool operator < ( node a , node b )
{
	return a.start < b.start || a.start == b.start && a.end < b.end ;
}
bool check( deque < node> &list , int Na , int Nb  , Time T )
{
	int i , n = list.size();
	priority_queue < Time , vector<Time>, greater <Time>  > na , nb;
	for(i = 0; i < Na; i++)
		na.push( Time() );
	for(i = 0; i < Nb; i++)
		nb.push( Time() );


	for(i = 0; i < n; i++)
	{
		//cout <<na.top().m << " " << na.top().s<<endl;
		if( list[i].na == 1 )
		{
			if(na.size() && na.top() <= list[i].start ) 
			{
				//cout <<na.top().m << " " << na.top().s<<endl;
				nb.push( list[i].end + T );
				na.pop();
			}else return 0;
			
						
		}else {
			if(nb.size() && nb.top() <= list[i].start )
			{
				//cout <<nb.top().m << " " << nb.top().s<<endl;
				na.push(list[i].end + T );
				nb.pop();
			}else return 0;
		}
	}
	return 1;
}
int main ()
{
	int N, T , Na , Nb , i , j , test = 0;;
	Time tmp;
	freopen( "B-small-attempt2.in" , "r" , stdin );
	freopen( "out.txt" , "w" , stdout );
	scanf ("%d" , &N );
	while( N-- )
	{
		test ++;
		scanf( "%d" , &T );
		tmp.m = T;
		scanf ("%d%d", &Na, &Nb );
		deque < node > list ( Na + Nb ) ;
		for(i = 0; i < Na; i++)
		{
			scanf ("%d:%d %d:%d" , &list[i].start.m , &list[i].start.s , &list[i].end.m , &list[i].end.s ); 
			list[i].na = 1;
		}
		for(i = 0; i < Nb; i++)
		{
			scanf ("%d:%d %d:%d" , &list[i+Na].start.m , &list[i+Na].start.s , &list[i+Na].end.m , &list[i+Na].end.s ); 
			list[i+Na].na = 0;
		}
		sort( list.begin() , list.end() );
		int resa = 1000, resb = 1000;
		check( list , 0 , 1 , Time( 0, T ) ) ;

		for(i = 0; i <= Na; i++) 
		{
			for(j = 0; j <= Nb; j++)
			{
				if( check( list , i , j , Time( 0, T ) ) )
				{
					if( i + j < resa + resb ) 
					{
						resa = i ; resb = j;
						//break;
					}
				}
			}
		//	if( resa != 1000 && resb != 1000 ) break;
		}
		printf( "Case #%d: %d %d\n" ,test ,  resa , resb ); 
	}
	return 0;
}