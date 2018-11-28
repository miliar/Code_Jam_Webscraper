#include <iostream>
#include <complex>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef complex<double> point;
double w;
int l, u, g;
vector<point> x, y;

double cross(point a,point b){
	return a.real() * b.imag() - a.imag() * b.real();
}

void norm(vector<point> a, vector<point> b){
	vector<double> v;
	for(int i=0;i<a.size();i++)
		v.push_back(a[i].real());
	for(int i=0;i<b.size();i++)
		v.push_back(b[i].real());
	sort(v.begin(),v.end());
	v.erase(unique(v.begin(),v.end()),v.end());
	
	int k = 1;
	x.push_back(a[0]);
	for(int i=1;i<a.size();i++){
		while(fabs(a[i].real()-v[k])>1e-6){
			x.push_back(a[i-1]+(a[i]-a[i-1])*(v[k]-a[i-1].real())/(a[i].real()-a[i-1].real()));
			k++;
		}
		x.push_back(a[i]);
		k++;
	}
	
	k = 1;
	y.push_back(b[0]);
	for(int i=1;i<b.size();i++){
		while(fabs(b[i].real()-v[k])>1e-6){
			y.push_back(b[i-1]+(b[i]-b[i-1])*(v[k]-b[i-1].real())/(b[i].real()-b[i-1].real()));
			k++;
		}
		y.push_back(b[i]);
		k++;
	}
}

double calc(double X){
	double ret = 0;
	for(int i=1;i<x.size();i++){
		if(X>=x[i].real()){
			ret += fabs(cross(x[i]-x[i-1],y[i]-x[i-1]));
			ret += fabs(cross(x[i-1]-y[i-1],y[i]-y[i-1]));
		}
		else{
			point a = x[i-1];
			point b = y[i-1];
			point c = x[i-1]+(x[i]-x[i-1])*(X-x[i-1].real())/(x[i].real()-x[i-1].real());
			point d = y[i-1]+(y[i]-y[i-1])*(X-y[i-1].real())/(y[i].real()-y[i-1].real());
			ret += fabs(cross(c-a, d-a));
			ret += fabs(cross(a-b, d-b));
			break;
		}
	}
	return ret;
}

void run(){
	cin >> w >> l >> u >> g;
	vector<point> lower(l), upper(u);
	for(int i=0;i<l;i++){
		cin >> lower[i].real() >> lower[i].imag();
	}
	for(int i=0;i<u;i++){
		cin >> upper[i].real() >> upper[i].imag();
	}

	vector<point> total;
	for(int i=0;i<lower.size();i++)
		total.push_back(lower[i]);
	for(int i=0;i<upper.size();i++)
		total.push_back(upper[upper.size()-1-i]);

	double area = 0;
	for(int i=0;i<total.size();i++){
		area += cross(total[i], total[(i+1)%total.size()]);
	}
	area = fabs(area)/g;
	
	x.clear();
	y.clear();
	norm(lower, upper);
	
//	for(int i=0;i<x.size();i++)
//		cerr << x[i] << " " ;
//	cerr << endl;
	
	double cur = 0;
	for(int i=0;i<g-1;i++){
		double lo = cur;
		double hi = w;
		for(int k=0;k<100;k++){
			double mid = (lo+hi)/2.0;
			if(calc(mid)<(i+1)*area)
				lo=mid;
			else
				hi=mid;
		}
		cout << lo << endl;
		cur = lo;
	}
}

int main(){
	int t;
	cin >> t;
	cout << fixed << setprecision(12); 
	for(int c=0;c<t;c++){
		printf("Case #%d:\n", c+1);
		run();
	}
	return 0;
}
