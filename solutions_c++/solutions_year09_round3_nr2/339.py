/*
ID: aditya21
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() 
{
	ifstream fin ("d:\\io\\B-large.in");
	ofstream fout ("d:\\io\\A-large.out");

	int a, b, c;
	int i, j, k;
	int p, q, r, x, y, z;
	int p1, q1, r1, x1, y1, z1;
	double dmin, tmin;
	unsigned long long ans;
	
	int cost,max,temp1,temp2;
	string str1,str2;
	char str[100],ch;

	char *pch,ch2;;
	vector<int> xc,yc,zc,vxc,vyc,vzc;
	int base;

	fin>>a;

	for(i=0;i<a;i++)
	{
		fin>>b;
		fout<<"Case #"<<i+1<<": ";
		cout<<"Case #"<<i+1<<": ";
		p1=0; q1=0; r1 = 0; x1=0; y1=0; z1=0;
		for(j=0;j<b;j++)
		{
			fin>>p>>q>>r>>x>>y>>z;
			p1+=p; q1+=q; r1+=r; x1+=x; y1+=y; z1+=z;
		}
		
		//p1/=b; q1/=b; r1/=b; x1/=b; y1/=b; z1/=b;
		temp1 = x1*x1+y1*y1+z1*z1;
		temp2 = p1*x1+q1*y1+r1*z1;

		if(temp1 == 0)
			tmin = 0;
		else
			tmin = -1*(double)temp2/(double)temp1;
		if(tmin <= 0)
			tmin = 0;
		dmin = sqrt((p1+tmin*x1) * (p1+tmin*x1) + (q1+tmin*y1) * (q1+tmin*y1) + (r1+tmin*z1) * (r1+tmin*z1) )/(double)b;
		sprintf(str, "%lf %lf", dmin, tmin);
		fout<<str<<endl;
	}
	
}

