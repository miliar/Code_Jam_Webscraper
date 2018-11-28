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



int pts[300];
int vends[300];

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		double d;
		
		double x,y,z;
		
		fin >> n >> d;
		
		double mn = 0.0;
		
		double mx = 1e18;
		
		for(i=0; i<n; i++)
		{
			fin >> pts[i] >> vends[i];
		}
		
		while(mx > (mn+1e-9)*(1+1e-9))
		{
			double mid = (mx+mn)/2.0;
			bool isok = true;
			
			double currmin = -1e18;
			
			for(i=0; i<n; i++)
			{
				x = max((double)pts[i]-mid,currmin+d);
				y = x+d*((double)vends[i]-1.);
				if(y <= ((double)pts[i])+mid)
				{
					currmin=y;
				}
				else {
					isok=false;
					break;
				}
			}
			if(isok)
			{
				mx=mid;
			}
			else {
				mn=mid;
			}

		}
		cout.precision(15);
		fout.precision(15);
		cout << "Case #" << ct << ": " <<  mn << endl;
		fout << "Case #" << ct << ": " <<  mn << endl;
		
		
	}
	
	
	return 0;
}

