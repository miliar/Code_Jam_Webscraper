#include <iostream>
#include <cmath>
using namespace std;
double h[1001];
double area[1001];
int W,G;
int n,m;
double get_area(double x){
	int t=(int)(floor(x)+1e-7);
	if (t>=W)
		return area[t];
	if (t<0)
		return 0;
	double r=x-t;
	return area[t]+((((1-r)*h[t]+r*h[t+1])+h[t])*r*0.5);
}
double bs(double a){
	double l=0,u=W;
	for (int i=0;i<300;++i){
		double m=(l+u)/2;
		if (get_area(m)<a)
			l=m;
		else
			u=m;
	}
	return (l+u)/2;
}
int main(){
	cout<<fixed;
	cout.precision(9);
	int tnum,tcou=0;
	cin>>tnum;
	while (tnum--){
		cin>>W>>n>>m>>G;
		int lx=0,ly=0;
		for (int i=0;i<n;++i){
			int x,y;
			cin>>x>>y;
			if (x>lx){
				for (int j=lx;j<=x;++j){
					h[j]=-(ly*(x-j)+y*(j-lx))/(double)(x-lx);
				}
			}
			lx=x;
			ly=y;
		}
		lx=0;ly=-10000;
		for (int i=0;i<m;++i){
			int x,y;
			cin>>x>>y;
			if (x>lx){
				for (int j=lx+1;j<=x;++j)
					h[j]+=(ly*(x-j)+y*(j-lx))/(double)(x-lx);
			}
			lx=x;
			ly=y;
			if (x==0)
				h[0]+=y;
		}
		//for (int i=0;i<=W;++i)
		//	cout<<h[i]<<' ';
		//cout<<endl;
		area[0]=0;
		for (int i=1;i<=W;++i)
			area[i]=area[i-1]+(h[i-1]+h[i])*0.5;
		double A=get_area(W);
		cout<<"Case #"<<++tcou<<":"<<endl;
		for (int i=1;i<G;++i)
			cout<<bs((A*i)/G)<<endl;
	}
	return 0;
}
