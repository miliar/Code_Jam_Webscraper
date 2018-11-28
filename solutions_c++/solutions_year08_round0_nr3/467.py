// fsw2.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <assert.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <time.h>
using namespace std;

const double eps=1e-8;

inline bool almost_equ(const double d1,const double d2)
{
	return abs(d1-d2)<eps;
}


inline double space_under_circle(const double a, const double b,const double r)
{
	assert(a<=b);
	return 0.5*r*r*(acos(a/r)-acos(b/r))+0.5*b*sqrt(r*r-b*b)-0.5*a*sqrt(r*r-a*a);
}

inline double x_cross_qcircle_with_line(double r,double y_line)
{	
	return sqrt(r*r-y_line*y_line);
}

inline double rounded_rect_space(double x_start,double x_finish,double y_start,double y_finish,double xc_with_low_line,double xc_with_high_line,double r)
{
	if (xc_with_low_line<=x_start)
		return 0.0;
	double s=0;
	if (xc_with_high_line>x_start)
		s+=(min(xc_with_high_line,x_finish)-x_start)*(y_finish-y_start);
	double x_circle_start=max(x_start,xc_with_high_line);
	double x_circle_end=min(x_finish,xc_with_low_line);
	if (x_circle_start<x_circle_end)
		s+=(space_under_circle(x_circle_start,x_circle_end,r)-(x_circle_end-x_circle_start)*(y_start));
	return s;
}

inline double rounded_rect_space(double x_start,double x_finish,double y_start,double y_finish,double r)
{
	double xc_low=x_cross_qcircle_with_line(r,y_start);
	double xc_high=x_cross_qcircle_with_line(r,y_finish);
	return rounded_rect_space(x_start,x_finish,y_start,y_finish,xc_low,xc_high,r);
}

double fly_radius,Radius_outer,thickness,radius_string,gap,inner_radius;

void make_fly_small()
{
	thickness+=fly_radius;
	radius_string+=fly_radius;
	gap-=2*fly_radius;
	fly_radius=0;
	inner_radius=Radius_outer-thickness;
}

inline double gap_start(const int i)
{
	return radius_string+gap*i+2*radius_string*i;
}
inline double gap_finish(const int i)
{
	return gap_start(i)+gap;
}


double calc_gap_space()
{
	double S=0;
	for (int line_y=0;true;++line_y)
	{
		double y_low=gap_start(line_y);
		double y_high=y_low+gap;
		if (y_low>inner_radius)
			break;
		double xc_low=x_cross_qcircle_with_line(inner_radius,y_low);//cross of lines with with circle
		double xc_high=x_cross_qcircle_with_line(inner_radius,y_high);
		
		for (int line_x=0;true;++line_x)
		{
			double x_low=gap_start(line_x);
			double x_high=x_low+gap;
			if (x_low>xc_low)
				break;
			S+=rounded_rect_space(x_low,x_high,y_low,y_high,xc_low,xc_high,inner_radius);
		}
	}
	return S;
}

ostream &print_real(ostream &out,double v)
{	int i=int(v);
	double ost=(v-i)*1e6;
	int j=int(ost);
	//if (ost-j>0.5) ++j;	
	out<<i<<'.'<<std::setfill('0')<<std::setw(6)<<j;
	return out;
}

void test_math();
int main()
{
	//test_math();	
	//ifstream fin("d:/fun/qr/FlySwatter/sample.in");ofstream fout("d:/fun/qr/FlySwatter/sample.output");
	ifstream fin("d:/fun/qr/FlySwatter/C-small-attempt0.in");
	ofstream fout("d:/fun/qr/FlySwatter/C-small.output");
	
	int N;
	fin>>N;
	assert(fin.good());
	assert(fout.good());

	for (int i_case=1;i_case<=N;++i_case)
	{
		fin>>fly_radius>>Radius_outer>>thickness>>radius_string>>gap;
		make_fly_small();

		double gap_space=calc_gap_space();	
		double full_space=(M_PI*Radius_outer*Radius_outer)/4.0;
		double bad_space=full_space-gap_space;
		double p=bad_space/full_space;

		fout<<"Case #"<<i_case<<": ";
		print_real(fout,p)<<"\n";		
	}
	cout<<"\7Done\n";
	fout.flush();

	assert(fout.good());
	assert(fin.good() || fin.eof());

	int k;cin>>k;
	return 0;
}


/****************************************************
 * tests
 ****************************************************/

void test_math()
{
	cout<<"test_math start\n";
	assert( almost_equ(space_under_circle(0,1, 1) , M_PI_4 ) );
	assert( almost_equ(space_under_circle(-1,1, 1) , M_PI_2 ) );
	double d=space_under_circle(0,2, 2);
	assert( almost_equ(d , M_PI ) );
	d=space_under_circle(0,3, 3);
	assert( almost_equ(d , 9.0*M_PI/4.0 ) );

	assert( almost_equ(x_cross_qcircle_with_line(1,1),0) );
	double r=1.0;
	double x_cross=x_cross_qcircle_with_line(r,r/2);
	double awaited_x=sqrt(3.0/4.0)*r;
	assert( almost_equ(x_cross, awaited_x) );

	
	double s=rounded_rect_space(0,10,0,10,1);
	assert( almost_equ(s,M_PI_4) );

	s=rounded_rect_space(0,10,0,10,200);

	s=rounded_rect_space(0,10,0,10,200);
	assert( almost_equ(s,100) );

	s=rounded_rect_space(4,8,3,5,7);
	assert( abs(s-3.3)<0.4 );


	cout<<s<<"\n";

	cout<<"test_math done ok\n";
}