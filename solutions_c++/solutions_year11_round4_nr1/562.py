#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <cstring>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

bool orden(pair <int, int> a, pair <int, int> b)
{
	if(a.second != b.second) return a.second < b.second;
	return a.first < b.first;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		int X, S, R, t, N;
		cin>>X>>S>>R>>t>>N;
		
		int dv = R-S, D = X;
		
		vector < pair <int, int> > DV;
		
		vector <int> B(N), E(N), V(N);
		for(int i=0; i<N; i++)
		{
			cin>>B[i]>>E[i]>>V[i];
			D -= E[i]-B[i];
			DV.push_back(make_pair(E[i]-B[i], V[i] + S));
		}
		
		DV.push_back(make_pair(D, S));
		
		sort(all(DV), orden);
		
		double x = 0, tq = t;
		
		for(int i=0; i<DV.size(); i++)
		{
			double dmax = tq*(DV[i].second + dv);
			
			double d1 = min(dmax, 1.0*DV[i].first);
			
			double t1 = d1 / (DV[i].second + dv);
			double t2 = (1.0*DV[i].first - d1) / DV[i].second;
			
			x += t1 + t2;
			tq -= t1;
		}
		
		printf("%.10lf\n", x);
		
	}
	
	return 0;
}

