#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
		
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{		
		int x,s,r,n;
		double t;

		inf >> x >> s >> r >> t >> n;
		vector <pair <int, int> > sw;
		sw.clear();
		for (int i = 0; i < n; i++)
		{
			int b,e,w;
			inf >> b >> e >> w;
			sw.push_back(make_pair(w, e-b));
		}
		int sum = 0;
		for (int i = 0; i < n; i++) 
			sum += sw[i].second;
		sw.push_back(make_pair(0, x - sum));
		n++;
		sort(sw.begin(), sw.end());
		double anw = 0;
		for (int i = 0; i < n; i++)
		{
			int len;
			len = sw[i].second;
			double sp = sw[i].first;
			double rant = min(double(len)/(sp + r), t);
			anw += rant;
			t -= rant;
			double distleft = double(len) - rant*(sp + r);
			anw += distleft/(sp + s);
			
		}
		printf("Case #%d: %.9lf\n", test+1, anw);
		//outf << "Case #" << test+1 << ": " << anw << endl;
		

		

		
		
	}

	outf.close();
	return 0;
}
