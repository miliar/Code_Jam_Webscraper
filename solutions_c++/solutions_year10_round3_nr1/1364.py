#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// #include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

typedef uint64_t UINT64;
typedef int64_t INT64;

typedef struct POINT_tag
{
	INT64 x;
	// x 座標
	INT64 y;
	// y 座標
} POINT_t;


typedef struct LINE_tag
{
	
	POINT_t a;
	// 始点
	POINT_t b;
	// 終点
} LINE_t;

typedef std::vector< POINT_t > VectorPoint;
typedef std::vector< LINE_t > VectorLine;

bool intersection( POINT_t& p1, POINT_t& p2,
				   POINT_t& p3, POINT_t& p4 )
{
    if (p1.x >= p2.x){
        if ((p1.x < p3.x & p1.x < p4.x) || (p2.x > p3.x && p2.x > p4.x)) {
			return false;
		}
	}
    else {
        if ((p2.x < p3.x && p2.x < p4.x) || (p1.x > p3.x && p1.x > p4.x)) {
			return false;
		}
	}
    if (p1.y >= p2.y){
        if ((p1.y < p3.y & p1.y < p4.y) || (p2.y > p3.y && p2.y > p4.y)) {
			return false;
		}
	}
    else {
        if ((p2.y < p3.y && p2.y < p4.y) || (p1.y > p3.y && p1.y > p4.y)) {
			return false;
		}
	}

    if (((p1.x - p2.x) * (p3.y - p1.y) + (p1.y - p2.y) * (p1.x - p3.x)) * 
        ((p1.x - p2.x) * (p4.y - p1.y) + (p1.y - p2.y) * (p1.x - p4.x)) > 0) {
		return false;
	}

    if (((p3.x - p4.x) * (p1.y - p3.y) + (p3.y - p4.y) * (p3.x - p1.x)) * 
        ((p3.x - p4.x) * (p2.y - p3.y) + (p3.y - p4.y) * (p3.x - p2.x)) > 0)  {
		return false;
	}
	return true;
}

int main( void )
{
    UINT64		T	  = 0;
	UINT64		N	  = 0;
	UINT64		a	  =	0;
	UINT64		b	  =	0;
	UINT64		index = 0;
	
	std::cin >> T;
	
	do {
		std::cin >> N;

		UINT64 result = 0;
		VectorLine vp;
		vp.resize( N );
		
		for ( VectorLine::iterator iter = vp.begin();
			  iter != vp.end();  ++iter ){
			std::cin >> iter->a.x >> iter->b.x;
			iter->a.y = 0;
			iter->b.y = 10;

		}

		for ( VectorLine::iterator iter = vp.begin();
			  iter != vp.end();  ++iter ){
			for ( VectorLine::iterator next = iter+1;
				  next != vp.end();  ++next ){
				if ( intersection( iter->a, iter->b,
								   next->a, next->b ) == true ) {
					++result;
				}
			}

		}
		++index;
        printf( "Case #%lld: %lld\n", index, result );
	} while( index != T );
	
	
	return EXIT_SUCCESS;
}
