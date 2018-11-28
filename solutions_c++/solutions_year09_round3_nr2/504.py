// Round1.cpp : Defines the entry point for the console application.
// 
#include <vector>
#include <string>
#include <stack>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std ;

struct firefly
{
	signed int x,y,z,vx,vy,vz ;
};
 
 
int main( )
{
	int group;
	cin>>group;
	string signline; 
	getline(cin,signline) ; 
 
	for( size_t i=0;i<group;i++ )
	{    
		int c ;
		cin >> c ;
		vector<firefly> fs(c) ;

		for ( size_t k=0;k<c;k++)
			cin>>fs[k].x>>fs[k].y>>fs[k].z>>fs[k].vx>>fs[k].vy>>fs[k].vz ;
		
		// 系数 : 
		signed long long temp = 0 ,temp1 = 0 ,temp2 = 0; 
		signed long long  temp3 = 0 ,temp4 = 0 ,temp5 = 0; 
        for( size_t k =0;k<c;k++ )
		{
			temp += fs[k].vx ; 
			temp1 += fs[k].vy ;
			temp2 += fs[k].vz ;
			temp3 += fs[k].x ;temp4 += fs[k].y ;temp5 += fs[k].z ;
		}
		
		signed long long  a ,b ,constv ;
		a = temp*temp  + temp1*temp1 + temp2*temp2;  //  二次项系数
		b = 2 * ( temp3*temp + temp4*temp1 + temp5*temp2 ) ;  // 一次项系数
		constv = temp3 * temp3 + temp4*temp4 + temp5*temp5;  // 常数
		// a * t2 + b*t  求导数 ;
		long double t  ;
		if ( !a )
		{  
			t = 0 ;
			long double distance = temp3 * temp3 + temp4 * temp4 + temp5 * temp5 ;
			distance = sqrt(distance) / c ;
			printf("Case #%d: %lf %lf\n",i+1 ,distance, t) ;
			continue ;
		}

		t  =(long double)(b)*(-1.0) / (a*2.0) ; 
		if ( t < 0 )
		{
			t = 0 ;
			long double distance = temp3 * temp3 + temp4 * temp4 + temp5 * temp5 ;
			distance = sqrt(distance) / c ;
			printf("Case #%d: %lf %lf\n",i+1 ,distance, t) ;
			continue ;
		}
		else
		{
			long double distance   =  constv - ( b *b  / (4.0*a) )  ;
			distance = sqrt(distance) / c ; 
			printf("Case #%d: %lf %lf\n",i+1 ,distance, t) ; 
		}
	}

	return 0;
}

