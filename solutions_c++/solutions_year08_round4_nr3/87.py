#include<iostream>
#include<cmath>
using namespace std;

const int SIZE = 1000;
int x[SIZE], y[SIZE], z[SIZE], p[SIZE];
int N;

double f(double X, double Y, double Z){
	
	double P = 0;
	for(int i = 0 ; i < N ; i++)
		P = max(P, (fabs(x[i]- X) + fabs(y[i]-Y) + fabs(z[i]-Z)) / p[i]);
	return P;
}

double tz(double X, double Y){
	
	double left = 0, right = 1000000;
	double EPS = 1e-7;
	while(right-left > EPS) {
		double g=left+(right-left)/3, h=left+2*(right-left)/3;
		if(f(X, Y, g)<f(X, Y, h)) 
			right=h; 
		else left=g;    // change < to > if the fn inc then dec
	}
	return f(X, Y, (left+right)/2);
}

double ty(double X){
	
	double left = 0, right = 1000000;
	double EPS = 1e-7;
	while(right-left > EPS) {
		double g=left+(right-left)/3, h=left+2*(right-left)/3;
		if(tz(X,g)<tz(X,h)) 
			right=h; 
		else left=g;    // change < to > if the fn inc then dec
	}
	return tz(X, (left+right)/2);
}

double tx(){
	
	double left = 0, right = 1000000;
	double EPS = 1e-7;
	while(right-left > EPS) {
		double g=left+(right-left)/3, h=left+2*(right-left)/3;
		if(ty(g)<ty(h)) 
			right=h; 
		else left=g;    // change < to > if the fn inc then dec
	}
	return ty((left+right)/2);
}


int main(){

	//freopen("1.in", "rt", stdin);
	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> N;
		int i;
		for(i = 0 ; i < N ; i++)
			cin >> x[i] >> y[i] >> z[i] >> p[i];
		
		double pp = tx();
		cout.setf(ios::fixed);
		cout.setf(ios::showpoint);
		cout << "Case #" << t+1 << ": " << pp << endl;
	}

	return 0;	
}
