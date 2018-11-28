// Paste me into the FileEdit configuration dialog

#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <ctime>
#include <queue>

using namespace std;

const int MAX = 10000;

vector<pair<int,double>> PointsTotal;

int W, L, U, G, n;

vector<pair<int,int>> PointsFirst[2];

int main(int argc, char *argv[]) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;

	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{	
		PointsTotal.clear();
		PointsFirst[0].clear();
		PointsFirst[1].clear();
				
		cin>>W>>L>>U>>G;
		
		int x, y, x1, x2, y1, y2;
		vector<double> ans;

		for (int i = 0; i < L; ++i){		
			cin>>x>>y;
			PointsFirst[0].push_back(make_pair(x, y));
		}
		
		for (int i = 0; i < U; ++i){			
			cin>>x>>y;
			PointsFirst[1].push_back(make_pair(x, y));
		}
		
		for (int num = 0; num < 2;num++)
		{
			for (int i = 0; i<PointsFirst[num].size(); ++i){				
				x=PointsFirst[num][i].first;
				y=PointsFirst[num][i].second;				
				int p=lower_bound(PointsFirst[1-num].begin(),
						PointsFirst[1-num].end(),
						make_pair(x,-100000000))
					-PointsFirst[1-num].begin();
				
				x2=PointsFirst[1-num][p].first;
				y2=PointsFirst[1-num][p].second;
				
				double q;

				if(x2==x) {
					q=y2;
				}
				else{
					x1=PointsFirst[1-num][p-1].first;
					y1=PointsFirst[1-num][p-1].second;
					q=((double)y1*(x2-x)+y2*(x-x1))/(x2-x1);
				}
				PointsTotal.push_back(make_pair(x, fabs(q-y)));
			}
		}

		sort(PointsTotal.begin(), PointsTotal.end());		

		double total_need_square=0;

		n=PointsTotal.size();

		for(int i = 0; i < n-1; ++i)
			total_need_square+=(PointsTotal[i+1].first-PointsTotal[i].first)*(PointsTotal[i].second+PointsTotal[i+1].second);
	
		double need_square=total_need_square/G;		
		
		double cur=0;
		for(int i= 0; i < n-1; ++i){
			double y1=PointsTotal[i].second;
			double y2=PointsTotal[i+1].second;
			double x1=PointsTotal[i].first;
			double x2=PointsTotal[i+1].first;
			
			double d=(x2-x1)*(y1+y2);

			while(cur+d>=need_square)\
			{
				double k=(y2-y1)/(x2-x1);
				double a,b,c;
				a=k;
				b=2*y1;
				c=-need_square+cur;
				double x;
				if (fabs(a)<1e-9)
					x=-c/b;
				else{
					double d=b*b-4*a*c;					
					d=sqrt(d);
					x=(-b+d)/(2*a);
				}				
				y1=y1+k*x;
				x1+=x;
				cur=0;
				ans.push_back(x1);				
				d=(x2-x1)*(y1+y2);
			}
			cur+=d;
		}
		
		if(ans.size()==G)
			ans.pop_back();
		
		cout << "Case #" << test_case << ":" << endl;
		for(int i = 0; i < ans.size(); ++i)
			printf("%.15lf\n", ans[i]);				
	
	}

	fclose(stdout);
}

