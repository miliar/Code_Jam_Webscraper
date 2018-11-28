#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

const int maxX = 100;
const int maxT = 100;

struct asdf{
	int a;
	double b;
	double c;
};

double solve(){
	double x, sp, runSp;
	double t,N;
	cin >> x >> sp >> runSp >> t >> N;
	vector< pair<double,double> > times;
	vector<asdf>  quzz;
	int beg,end;
	double spI;
	double time = x/sp;
	int sumLen=0;
	for( int i = 0; i < N; i++ ){
		cin>>beg>>end>>spI;
		sumLen += end-beg;
		time -= (end-beg)/sp;
		time += (end-beg)/(spI+sp);
		pair<double,double> qwe;
		qwe.first = ((end-beg)/(spI+sp) - (end-beg)/(spI+runSp)) /((end-beg)/(spI+runSp));
		qwe.second = (end-beg)/(spI+runSp);
		times.push_back( qwe ) ;
		asdf asd;
		asd.a = i;
		asd.b = spI;
		asd.c = qwe.first;
		quzz.push_back( asd);
	}
	double dp [maxX][maxT];
	if( sumLen<x ){
		times.push_back( make_pair( ((x-sumLen)/sp - (x-sumLen)/runSp) / ((x-sumLen)/runSp), (x-sumLen)/runSp ));
	}
	else
		N--;
	sort( times.begin(), times.end(), greater<pair<double,double>>() );

	int k = 0;
	while( t > 0 && k < N+1){
		pair<double,double> qwer = times[k];
		double ert = time;
		time -= qwer.first * min( double(t), qwer.second );
		double iopg = ert - time;
		t -= qwer.second;
		k++;
	}
	return time;
}

int main(){
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T;
	scanf("%d", &T);
	for( int i = 1; i <= T; i++ ){
		printf("Case #%d: %.10lf\n", i, solve());
	}
}