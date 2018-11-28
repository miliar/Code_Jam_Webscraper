#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <cstring>
#include <ctime>
#include <complex>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

int main()
{
// 	ifstream fin("A-sample.in");
// 	ofstream fout("A-sample.out");
// 	ifstream fin("A-small-attempt0.in");
// 	ofstream fout("A-small-attempt0.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;
	for(int zrz = 0; zrz < T; zrz++)
	{
		fout << "Case #" << zrz+1 << ":\n";
		
		int W,L,U,G;
		fin >> W >> L >> U >> G;
		
		
		set<int> coords;
		vector<int> xl;
		vector<int> yl;
		vector<int> xu;
		vector<int> yu;
		
		FOR(i,0,L)
		{
			int a,b;
			fin >> a >> b;
			xl.PB(a);
			yl.PB(b);
			coords.insert(a);
		}
				
		FOR(i,0,U)
		{
			int a,b;
			fin >> a >> b;
			xu.PB(a);
			yu.PB(b);
			coords.insert(a);
		}

		coords.insert(0);
		coords.insert(W);
		
		vector<int> V(coords.begin(),coords.end());
		vector<double> height;

		FOR(p,0,V.size())
		{
			double lowery = 0;
			double highery = 0;
			FOR(t,0,xl.size())
			if(xl[t] == V[p])
				lowery = yl[t];
			else if(xl[t] > V[p] && xl[t-1] < V[p])
				lowery = yl[t-1] + ((double)yl[t]-yl[t-1])*((double)V[p]-xl[t-1])/((double)xl[t]-xl[t-1]);
			
			FOR(t,0,xu.size())
			if(xu[t] == V[p])
				highery = yu[t];
			else if(xu[t] > V[p] && xu[t-1] < V[p])
				highery = yu[t-1] + ((double)yu[t]-yu[t-1])*((double)V[p]-xu[t-1])/((double)xu[t]-xu[t-1]);
	
			cout << V[p] << " " << lowery << " " << highery << endl;
			height.PB(highery-lowery);
		}
		
		FOR(p,0,V.size())
			cout << V[p] << " " << height[p] << endl;
		
		double totArea = 0;
		FOR(i,0,V.size()-1)
		totArea += 0.5*(V[i+1]-V[i])*(height[i+1]+height[i]);
		
		double eachArea = totArea/G;
		
		FOR(a,0,G-1)
		{
			double areaLeft = eachArea*(a+1);
			
			double maxix = W;
			double minix = 0;
			FOR(k,0,100)
			{
				double midix = (maxix+minix)/2;
				
				double area = 0;
				FOR(i,0,V.size()-1)
				{
					if(V[i+1] <= midix)
					{
						area += 0.5*(V[i+1]-V[i])*(height[i+1]+height[i]);
					}
					else
					{
						if(V[i] > midix) break;
						
						double nextHeight = height[i] + (height[i+1]-height[i])*(midix-V[i])/(V[i+1]-V[i]);
						area += 0.5*(midix-V[i])*(nextHeight+height[i]);
						break;
					}
				}
				
				if(area < areaLeft)
					minix = midix;
				else maxix = midix;
			}
			fout << setprecision(10) << fixed << minix << endl;
		}
			
					
		
		MSG(totArea);
	}

	return 0;
}






