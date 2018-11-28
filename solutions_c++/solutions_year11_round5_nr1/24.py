#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


double xvals[250];
double yvals[250][2];
int n;
int lowlist[101][2];
int highlist[101][2];


double getvalue(double d)
{
	double ans = 0.0;
	
	int i,j,k;
	
	for(i=1; i<n; i++)
	{
		if(xvals[i] < d)
		{
			ans+= (xvals[i]-xvals[i-1])*( (yvals[i][1]-yvals[i][0])+(yvals[i-1][1]-yvals[i-1][0]));
		}
		else {
			double x = (d-xvals[i-1])/(xvals[i]-xvals[i-1])*((yvals[i][1]-yvals[i][0])-(yvals[i-1][1]-yvals[i-1][0]));
			//cerr << "X " << x << endl;
			ans+=(d-xvals[i-1])*(2*(yvals[i-1][1]-yvals[i-1][0])+x);
			break;
		}
		//cerr << "A " << ans << endl;

	}
	return ans;
}


double sol(double target,double wid)
{
	cout << "AIMING " << target << endl;
	double mn = 0.0;
	double mx = wid;

	while(mx - mn > 1e-10)
	{
		double mid = (mx+mn)/2.;
		double d = getvalue(mid);
		
		//cout << mid << " " << d << endl;
		
		if(d < target)
			mn=mid;
		else {
			mx=mid;
		}
	}
	return (mx+mn)/2.;
}

	
int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(16);
	fout.precision(16);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k,w,l,u,g;
		
		
		
		fin >> w >> l >> u >> g;
		
		for(i=0; i<l; i++)
		{
			fin >> lowlist[i][0] >> lowlist[i][1];
		}
		for(int i=0; i<u; i++)
			fin >> highlist[i][0] >> highlist[i][1];
		
		n=0;
		
		int currl = 0;
		int curru = 0;
		
		while(currl < l && curru < u)
		{
			j = min(lowlist[currl][0],highlist[curru][0]);
			
			xvals[n]=j;
			
			if(j==lowlist[currl][0])
			{
				yvals[n][0]=lowlist[currl][1];
				currl++;
			}
			else {
				yvals[n][0] = (((double)j)-((double)lowlist[currl-1][0]))/((double)lowlist[currl][0]-lowlist[currl-1][0]) * ((double)lowlist[currl][1]-lowlist[currl-1][1])+lowlist[currl-1][1];
			}
			if(j==highlist[curru][0])
			{
				yvals[n][1] = highlist[curru][1];
				curru++;
			}
			else {
				yvals[n][1] = (((double)j)-((double)highlist[curru-1][0]))/((double)highlist[curru][0]-highlist[curru-1][0]) * ((double)highlist[curru][1]-highlist[curru-1][1])+highlist[curru-1][1];
			}
			n++;
		}
		
		for(i=0; i<n; i++)
		{
			cout << xvals[i] << " " << yvals[i][0] << " " << yvals[i][1] << endl;
		}
	
		double tot = getvalue(w);
		
		cout << tot << endl;
		
		//cout << getvalue(4) << endl;
		
		cout << "Case #" << ct << ":"  << endl;
		fout << "Case #" << ct << ":"  << endl;
		
		for(i=1; i<g; i++)
		{
			double ret = sol(tot*((double)i)/((double)g),w);
			cout << ret << endl;
			fout << ret << endl;
		}
		
		
		
	}
	
	
	return 0;
}

