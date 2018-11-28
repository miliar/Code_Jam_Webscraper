#include<iostream>
#include<cmath>
#include<complex>
using namespace std;

#define CPX complex<double>
const double eps = 1e-9;
inline int dcmp(const double&a){return fabs(a) <= eps ? 0 : (a<0?-1 :1);}
int N;
double x[100], y[100], r[100];
double ans, lo, hi, R;
inline double sqr(double a){return a*a;}
const double pi = acos(-1);
int mark[100];

inline int calc(double R,int i,int j,CPX&p1, CPX&p2) {
	/*
	cout<<" R = "<<R<<endl;
	cout<<" o1 : ( "<<x[i]<<","<<y[i]<<")  o2 : ( "<<x[j]<<","<<y[j]<<")"<<endl;	
	cout<<" Circle of C#"<<i<<"  C#"<<j<<" :"<<endl;
	*/
	double A = sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));
	double B = R - r[i], C = R - r[j];
	double S = A + B + C, M = max(A, max(B, C));
	if(dcmp(M*2-S) > 0) {
	//	cout<<" >> None!"<<endl;
		return 0;
	}
	double deg = acos((sqr(A)+sqr(B)-sqr(C))/(2*A*B));
	CPX t(x[j]-x[i],y[j]-y[i]);
	p1 = t * CPX(cos(deg), sin(deg)) * B / A + CPX(x[i],y[i]);
	p2 = t * CPX(cos(2*pi-deg), sin(2*pi-deg)) * B / A + CPX(x[i],y[i]);
	/*cout<<"  P1 : "<<p1<<endl;
	cout<<"  P2 : "<<p2<<endl;*/
	return 1;
}

int arr[100], n;

int check1(double R) {
	if(!n) return true;
	if(n<2) return dcmp(R-r[arr[0]])>-1;
	
	for(int i=0;i<n;++i)
		for(int j=i+1;j<n;++j) {
			CPX o[2];
			if(!calc(R,arr[i],arr[j],o[0],o[1])) continue;
			for(int cc=0;cc<2;++cc) {
				double ox=o[cc].real(), oy=o[cc].imag();
				bool flag = true;
				for(int k=0;k<n && flag;++k)
					if(sqr(ox-x[arr[k]])+sqr(oy-y[arr[k]]) > sqr(R - r[arr[k]])+eps)
						flag = false;
				if(flag) return true;
			}
		}
	return false;
}

int check(double R) {
	for(int i=0;i<N;++i) {
		for(int j=i+1;j<N;++j) {
			CPX o[2];
			if(!calc(R,i,j,o[0],o[1])) continue;
			for(int cc=0;cc<2;++cc) {
			//	cout<<"Check "<<o[cc]<<endl;
				n = 0;
				double ox=o[cc].real(), oy=o[cc].imag();
				for(int k=0;k<N;++k)
					if(sqr(ox-x[k])+sqr(oy-y[k]) > sqr(R - r[k])+eps) {
						arr[n ++] = k;
			//			cout<<"  -> Extend : "<<k<<endl;
					}
				if(check1(R)) return true;
		//		cout<<"   >> False!"<<endl;
			}
		}
	}
	return false;
}

int run() {
	cin>>N;
	for(int i=0;i<N;++i)
		cin>>x[i]>>y[i]>>r[i];
	if(N==1) {
		cout<<r[0]<<endl; return 1;
	}
	if(N==2){
		cout<<max(r[0],r[1])<<endl; return 1;
	}
	double lo=*max_element(r,r+N), hi=2000, mid;
	//double lo=7, hi=7, mid;
	
	while(hi-lo > 1e-7) {
	//	for(int ii=0;ii<3;++ii) {
		mid = (hi + lo) / 2;
		
		
		
		if(check(mid)) {
		//	cout<<"OK! R = "<<mid<<endl;
			hi = mid; 
		}else {
		//	cout<<"Failed!  R = "<<mid<<endl;
			lo = mid;
		}
	}
	
	cout.setf(ios::fixed);
	cout.precision(7);
	cout<<lo<<endl;
}

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int test; cin>>test;
	for(int no=1;no<=test;++no) {
		cout<<"Case #"<<no<<": "; run();
	}
}
