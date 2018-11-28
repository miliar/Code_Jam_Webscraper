#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string a[100];

struct otr {
	int x1,y1,x2,y2;
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int n;
		cin>>n;
		string p;
		for (int i =0; i<n;++i) {
			string s; int t;
			cin >> s >> t;
			for (int j =0;j<t;++j)
				p+=s;
		}
		int x=0,y=0,d=0,_x=0,_y=0;
		vector<otr> a;
		for(int i=0;i<p.length();++i){
			
			if(p[i]=='F'){
				if (d==0)
					y++;
				else if(d==1)
					x++;
				else if(d==2)
					y--;
				else if(d==3)
					x--;
			}else if(p[i]=='L') {
				d=(d-1);
				if(d<0)
					d=3;
			}else if(p[i]=='R') {
				d=(d+1)%4;
			}
			if(p[i]!='F'&&(x!=_x||y!=_y))
			{
				otr ot = {_x,_y,x,y};
				a.push_back(ot);
				_x=x;
				_y=y;
			}
			
		}
		if((x!=_x||y!=_y))
			{
				otr ot = {_x,_y,x,y};
				a.push_back(ot);
				_x=x;
				_y=y;
			}

vector<pair<int,int> > pp;
pp.push_back(make_pair(0,0));
for (int i=0;i<a.size();++i){
pp.push_back(make_pair(a[i].x2, a[i].y2));
}

	long long sq = 0;
	for (int i = 1; i < pp.size(); i++) {
		sq += pp[i - 1].first * pp[i].second - pp[i].first * pp[i - 1].second;
	}

		int kol=0;
			for (int i=-100;i<=100;++i)
				for(int j=-100;j<=100;++j)
				{
					double x=i+0.5,y=j+0.5;
					bool up = false, down = false, left = false,right=false;
					int k;

					for (k=0;k<a.size();++k){
						if (a[k].x1==a[k].x2) {
							if (a[k].x1<x && 
								((a[k].y1<y&&a[k].y2>y)||(a[k].y2<y&&a[k].y1>y))) {
									left=true;
							} else if (a[k].x1>x &&
								((a[k].y1<y&&a[k].y2>y)||(a[k].y2<y&&a[k].y1>y))) {
								right=true;
							}
						} else {
							if (a[k].y1>y && 
								((a[k].x1<x&&a[k].x2>x)||(a[k].x2<x&&a[k].x1>x))) {
									up=true;
							} else if (a[k].y1<y &&
								((a[k].x1<x&&a[k].x2>x)||(a[k].x2<x&&a[k].x1>x))) {
								down=true;
							}
						}
						if ((up&&down)||(left&&right))
							break;
					}
					if(k!=a.size()) {
						++kol;

					}
					
				}

		cout << "Case #" << test+1 << ": " << kol-abs(sq)/2 << endl;
	}

	return 0;
}

