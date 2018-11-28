
/** @author: Sourabh Daptardar */
#ifndef _CPPINCL_H
#define _CPPINCL_H

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cerrno>
#include <cstring>
#include <cmath>
#include <climits>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>


extern "C" {
#include <stdint.h>
}

using namespace std;
#if 0
#define __realloc__(type,var,sz) var = (type*)realloc(var,(sz)*sizeof(type)); assert(var)
#define __malloc__ __realloc__
#define __array__(type,var,sz) type *var = NULL; \
			__realloc__(type,var,sz); \
			int64_t  __##var##_sz = (sz); \
			int64_t __##var##_pb = 0

#define __resize__(type,var,sz) __realloc__(type,var,sz); \
							__##var##_sz = (sz)

#define __pb__(type,var,val) if( __##var##_sz <= __##var##_pb ) { \
							if( __##var##_sz == 0 ) __##var##_sz = 1; \
							else __##var##_sz <<= 1; \
							__realloc__(type,var,__##var##_sz); \
						 } \
						 var[__##var##_pb++] = (val);	
#endif

#define __out__(str) fprintf(stdout,"%s:%d:%s :: %s\n",__FILE__,__LINE__,__func__,str)
#define __err__(str) fprintf(stderr,"%s:%d:%s :: %s\n",__FILE__,__LINE__,__func__,str)

#define __printarr__(A,N,fmt) { int i_; for( i_ = 0 ; i_ < (N) ; i_++ ) printf(fmt " ", A[i_]);;; printf("\n");  }

#define __printmat__(A,M,N,fmt) { int i_,j_; printf("\n"); \
	for( i_ = 0 ; i_ < (M) ; i_++ ) { \
		for( j_ = 0 ; j_ < (N) ; j_++ ) { \
			printf(fmt " ", A[i_][j_]);\
		} \
		printf("\n"); \
	} \
}

#define __min__(a,b) (((a)<=(b))?(a):(b))
#define __min3__(a,b,c) __min__(__min__((a),(b)),(c))
#define __max__(a,b) (((a)>=(b))?(a):(b))
#define __max3__(a,b,c) __max__(__max__((a),(b)),(c))

#endif

const int NMAX = 1002;

int main(int argc, char *argv[])
{
	ios::sync_with_stdio(true);
	int T,N,par,X1,X2,Y1,Y2;
	int X[NMAX]; int Y[NMAX];
	cin >> T;
	for( int t = 0 ; t < T ; t++ ) {
		cin >> N;
		for( int n = 0 ; n < N ; n++ ) {
			cin >> X[n] >> Y[n];
		} 
		
		par = 0;
		for( int i = 0 ; i < N ; i++ ) {
			for( int j = 0 ; j < i ; j++ ) {
				if( X[i] < X[j] ) { X1 = X[i] ; X2 = X[j] ; Y1 =Y[i] ; Y2 = Y[j]; }
				else { X1 = X[j] ; X2 = X[i] ; Y1 = Y[j] ; Y2 = Y[i]; }
				if( Y1 < Y2 ) par++;	

			}		
		}
			
		cout << "Case #" << t+1 << ": " << (((N*(N-1))/2) - par) << endl; 
	}	

	return 0;
}
