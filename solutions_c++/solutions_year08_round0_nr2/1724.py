

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std ;

struct h_m
{
	int h,m ;
};

struct node
{
	h_m A,D ;
	char c ;
};

FILE *in = fopen("B-large.in","r") ;
FILE *out = fopen("B-large.out","w") ;
vector <node> times ;
int N,T,a,b ;

bool cmp(node x,node y)
{
	if( x.D.h == y.D.h )
		return x.D.m < y.D.m ;
	return x.D.h < y.D.h ;
}

bool cmp2(h_m x,h_m y)
{
	if( x.h == y.h )
		return x.m > y.m ;
	return x.h > y.h ;
}

int main()
{
	int i,j,k,l,u,v,g ;
	node h ;
	vector <h_m> A,B ;
	h_m f ;
	
	fscanf(in,"%d",&N) ;
	for(g=1;g<=N;g++)
	{
		fscanf(in,"%d%d%d\n",&T,&a,&b) ;
		A.clear() ;
		B.clear() ;
		times.clear() ;

		for(i=0;i<a;i++)
		{
			fscanf(in,"%d:%d %d:%d\n",&k,&l,&u,&v) ;
			h.D.h = k , h.D.m = l ;
			h.A.h = u , h.A.m = v ;
			h.c = 'A' ;
			times.push_back( h ) ;
		}
		
		for(i=0;i<b;i++)
		{
			fscanf(in,"%d:%d %d:%d\n",&k,&l,&u,&v) ;
			h.D.h = k , h.D.m = l ;
			h.A.h = u , h.A.m = v ;
			h.c = 'B' ;
			times.push_back( h ) ;
		}
		
		sort( times.begin(), times.end(), cmp ) ;
		a = 0 ;
		b = 0 ;

		for(i=0;i<times.size();i++)
		{
			if( times[i].c == 'A' )
			{
				for(j=0;j<A.size();j++)
					if( A[j].h == -1 ) continue ;
					else if( A[j].h < times[i].D.h || ( A[j].h == times[i].D.h && A[j].m <= times[i].D.m ) )
					{
						A[j].h = -1 ;
						break ;
					}
				if( j == A.size() ) a ++ ;
				f.m = times[i].A.m + T ;
				l = f.m >= 60 ? 1:0 ;
				f.m %= 60 ;
				f.h = times[i].A.h + l ;
// 				f.h %= 24 ;
				B.push_back( f ) ;
				sort( B.begin(), B.end(), cmp2 ) ;
			}
			else
			{
				for(j=0;j<B.size();j++)
					if( B[j].h == -1 ) continue ;
					else if( B[j].h < times[i].D.h || ( B[j].h == times[i].D.h && B[j].m <= times[i].D.m ) )
					{
						B[j].h = -1 ;
						break ;
					}
				if( j == B.size() ) b ++ ;
				f.m = times[i].A.m + T ;
				l = f.m >= 60 ? 1:0 ;
				f.m %= 60 ;
				f.h = times[i].A.h + l ;
// 				f.h %= 24 ;
				A.push_back( f ) ;
				sort( A.begin(), A.end(), cmp2 ) ;
			}
		}
		
		fprintf(out,"Case #%d: %d %d\n",g,a,b) ;
	}

	return 0 ;
}

