#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <functional>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cstdio>

using namespace std;

///////////////////////Problem 3
static const double PI = 3.141592653;

///calculate the sequence of the squares that the fly could escape
static double get_escape_square(double R, double r, double g, double f, double t,
								vector<pair<double, double>>& centers)
{
	double lim = R - t + g / 2.0;
	double inc = g + 2 * r;
	////cause it's symmetric, thus we just consider the right top quater
	for(double i = r + g / 2.0; i < lim; i += inc)
	{
		for(double j = r + g / 2.0; j < lim; j += inc)
		{
			pair<double, double> p = make_pair(i, j);
			centers.push_back(p);
		}
	}

	return g - 2 * f;
}

static inline double get_triangle_area(pair<double, double> p1, pair<double, double> p2, pair<double, double> p3)
{
	double val = fabs((p1.first * p2.second + p2.first * p3.second + p3.first * p1.second 
		- p1.first * p3.second - p2.first * p1.second - p3.first * p2.second )/2.0);
	return val;
}

static double get_escape_area(pair<double, double>& center, double len, double f, double inner_rad)
{
	double x;
	double eff_rad  = inner_rad - f;
	double eff2 = eff_rad * eff_rad; 
	///////////divide into 6 situation
	double dist_ld, dist_lt, dist_rd, dist_rt;
	pair<double,double> pld, plt, prd, prt;

	/////make the nodes
	pld.first = center.first - len / 2.0;
	pld.second = center.second - len/ 2.0;
	plt.first = center.first - len / 2.0;
	plt.second = center.second + len/ 2.0;
	prd.first = center.first + len / 2.0;
	prd.second = center.second - len/ 2.0;
	prt.first = center.first + len / 2.0;
	prt.second = center.second + len/ 2.0;


	dist_ld = (pld.first)* (pld.first) + (pld.second) * (pld.second);
	dist_lt = (plt.first)* (plt.first) + (plt.second) * (plt.second);
	dist_rd = (prd.first)* (prd.first) + (prd.second) * (prd.second);
	dist_rt = (prt.first)* (prt.first) + (prt.second) * (prt.second);
	
	///1 that has no escape area
	if(dist_ld > eff2){
		return 0;
	}
	///2 that all the square is the area
	else if(dist_rt <= eff2){
		return len * len;
	}
	///3 that only right top is outside the circle
	else if(dist_rt > eff2 && dist_lt <= eff2 && dist_rd <= eff2){

		pair<double, double> cp1, cp2;
		cp1.second = prt.second;
		cp2.first = prt.first;
		cp1.first = sqrt(eff2 - cp1.second * cp1.second);
		cp2.second = sqrt(eff2 - cp2.first * cp2.first);

		double sita=  asin(prt.second/eff_rad) - acos(prt.first/eff_rad);
		 x = (len * len + eff2 *(sita - sin(sita)) / 2 - get_triangle_area(cp1, cp2, prt));
	}
	///4 that only the left down is in side the circle
	else if(dist_ld <= eff2 && dist_rd > eff2 && dist_lt > eff2){

		pair<double, double> cp1, cp2;
		cp1.first = pld.first;
		cp2.second = pld.second;
		cp1.second = sqrt(eff2 - cp1.first * cp1.first);
		cp2.first = sqrt(eff2 - cp2.second * cp2.second);

		double sita= acos(pld.first/eff_rad) - asin(pld.second/eff_rad);
		 x = eff2 *(sita - sin(sita)) / 2 + get_triangle_area(cp1, cp2, pld);
	}
	///5 that left down and left top in the circle
	else if(dist_lt <= eff2 && dist_rd > eff2){

		pair<double, double> cp1, cp2;
		cp1.second = plt.second;
		cp2.second = pld.second;
		cp1.first = sqrt(eff2 - cp1.second * cp1.second);
		cp2.first = sqrt(eff2 - cp2.second * cp2.second);

		double sita= asin(plt.second/eff_rad) - asin(pld.second/eff_rad);
		 x = eff2 *(sita - sin(sita)) / 2 + (cp1.first + cp2.first - plt.first * 2) * len /2;

	}else{

		pair<double, double> cp1, cp2;
		cp1.first = prd.first;
		cp2.first = pld.first;
		cp1.second = sqrt(eff2 - cp1.first * cp1.first);
		cp2.second = sqrt(eff2 - cp2.first * cp2.first);

		double sita= acos(pld.first/eff_rad) - acos(prd.first/eff_rad);
		 x = eff2 *(sita - sin(sita)) / 2 + (cp1.second + cp2.second - pld.second * 2) * len /2;
	}
	return x;

}


static double get_prob(double R, double r, double t, double f, double g)
{
	if(f * 2 > g) return 1;

	vector<pair<double, double>> centers;
	double escp_r = get_escape_square(R, r, g, f, t, centers);

	double sum = 0.0;
	for(vector<pair<double, double>> ::iterator i = centers.begin(); i != centers.end(); i++)
	{
		sum += get_escape_area(*i, escp_r, f, R - t);
		
	}
	return 1.0 - sum * 4 / (PI * R * R);
}

static void process_one_case3(int num)
{
	double R, r, t, g, f;
	in >> f >> R >> t >> r >> g;
	out << "Case #"<< num << ": " << get_prob(R, r, t, f, g) << endl;
}


int main(int argc, char** argv)
{
	int case_num;
	in >> case_num;

	for(int i = 1; i <= case_num; i++)
	{
		process_one_case3(i);
	}

	return 0;

}