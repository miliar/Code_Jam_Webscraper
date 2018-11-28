// gcj_round1_ex.cpp : Defines the entry point for the console application.
//
 /*
#include <tchar.h>*/

#include <iostream>

using namespace std ;

struct point
{
	int x,y ;
};

bool same_side(point p1,point p2)
{
	if( (p1.x<p2.x&&p1.y<p2.y) || ( p1.x>p2.x&&p1.y>p2.y)  )
		return true;
	return false ;
}

int main( )
{
	size_t t ,n ;
	cin >> t;

	point ps[1000] ; 
	for(size_t i=0;i<t;i++)
	{
		int count = 0 ;
		cin >> n ;
		 
		cin >>ps[0].x >> ps[0].y ;
		// 
		for(size_t j=1;j<n;j++)
		{
			cin >> ps[j].x >> ps[j].y ;
			
			for( size_t k=0;k<j;k++ )
			{
				if( same_side(ps[j],ps[k]) )
					continue;
				else
					count ++ ;
			}
		}

		cout << "Case #" << i+1 << ": "<< count << endl ;
	}
	return 0;
}

