#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
#include <cstdarg>

using namespace std;

#define in(c) (c.first * c.first + c.second * c.second < t*t)
#define d(p) (sqrt(t*t - p*p))

double R, r, g, t, f;
int i,j;

double A(vector<pair<double, double> > v){
	double r = 0.;
	for(size_t i=0; i<v.size(); ++i){
		r += (v[i].first + v[(i+1)%v.size()].first) * (v[i].second - v[(i+1)%v.size()].second);
	}
	return .5*abs(r);
}

vector<pair<double, double> > V(pair<double, double> a, pair<double, double> b, pair<double, double> c){
	vector<pair<double, double> > p;
	p.push_back(a);
	p.push_back(b);
	p.push_back(c);
	return p;
}

vector<pair<double, double> > V(pair<double, double> a, pair<double, double> b, pair<double, double> c, pair<double, double> d){
	vector<pair<double, double> > p;
	p.push_back(a);
	p.push_back(b);
	p.push_back(c);
	p.push_back(d);
	return p;
}

vector<pair<double, double> > V(pair<double, double> a, pair<double, double> b, pair<double, double> c, pair<double, double> d, pair<double, double> e){
	vector<pair<double, double> > p;
	p.push_back(a);
	p.push_back(b);
	p.push_back(c);
	p.push_back(d);
	p.push_back(e);
	return p;
}

double S(pair<double, double> a, pair<double, double> b){
	return .5 * t * t * (atan(b.second/b.first)-atan(a.second/a.first)) - A(V(make_pair(0., 0.), a, b));
}

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc< tcs; ++tc){
		double erg = 0;
		//32
		//01
		pair<double, double> c[4];
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		if(2.*f >= g){
			erg = 1.;
			printf("Case #%d: %.6lf\n", tc+1, erg);
			continue;
		}
		r += f;
		g -= f+f;
		t = R-t-f;

		int co = 0;
		j=0;
		for(c[0].second = r; c[0].second < t; c[0].second += g+2.*r, ++j){
			double y = c[0].second + g;
			double l = y >= t ? 0. : d(y);
			i = static_cast<int>((l+r)/(g+2.*r));
			co += i;
			c[0].first = r + (g+2.*r) * i;

			c[1].second = c[0].second;
			c[3].first = c[0].first;
			c[2].first = c[0].first + g;
			c[2].second = c[0].second + g;
			c[3].second = c[2].second;
			c[1].first = c[2].first;

			pair<double, double> s0, s1;
			vector<pair<double, double> > v;
			
			while(in(c[0])){
				if(in(c[2])){
					s0 = make_pair(1., 0);
					s1 = make_pair(1., 0);
					v = V(c[0], c[1], c[2], c[3]);
				}else if(in(c[3]) && in(c[1])){
					s0 = make_pair(c[1].first, d(c[1].first));
					s1 = make_pair(d(c[3].second), c[3].second);
					v = V(c[0], c[1], s0, s1, c[3]);
				}else if(in(c[3]) && !in(c[1])){
					s0 = make_pair(d(c[0].second), c[0].second);
					s1 = make_pair(d(c[3].second), c[3].second);
					v = V(c[0], s0, s1, c[3]);
				}else if(!in(c[3]) && in(c[1])){
					s0 = make_pair(c[1].first, d(c[1].first));
					s1 = make_pair(c[0].first, d(c[0].first));
					v = V(c[0], c[1], s0, s1);
				}else if(!in(c[3]) && !in(c[1])){
					s0 = make_pair(d(c[0].second), c[0].second);
					s1 = make_pair(c[0].first, d(c[0].first));
					v = V(c[0], s0, s1);
				}
				erg += S(s0, s1);
				erg += A(v);
				c[0].first += g + 2.*r;
				c[1].first += g + 2.*r;
				c[2].first += g + 2.*r;
				c[3].first += g + 2.*r;
			}
		}
		erg += (g*g) * co;
		erg *= 4.;
		erg = (R*R*M_PI - erg) / (R*R*M_PI);
		printf("Case #%d: %.6lf\n", tc+1, erg);
	}
}
