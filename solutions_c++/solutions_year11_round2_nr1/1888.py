#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <map>
#include <set>
using namespace std;

#define loop(I,V) for(I=0;I<V.size();I++)
#define fo(a,b,c) for( a = ( b ); a < ( c ); a ++ )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

double owpminus(int toss, string stats[], int teams){
	int i,j,k;
	double wp=0,nwp=0;
	double twp=0,ntwp=0;
	fi(teams){
		wp=nwp=0;
		if(i==toss) continue;
		if(stats[i][toss]=='.') continue;
		fk(stats[i].size()){
			if(k==toss) continue;
			if(stats[i][k]=='.') continue;
			if(stats[i][k]=='1') wp++;
			nwp++;
		}
		if(nwp)
			twp+=(wp/nwp);
		ntwp++;
	}
	if(ntwp==0)
		return 0;
	else
		return (twp/ntwp);
}

double wpcalc(int team, string stats[]){
	int i;
	double wp=0,nwp=0;
	loop(i,stats[team]){
		if(stats[team][i]=='.') continue;
		if(stats[team][i]=='1') wp++;
		nwp++;
	}
	if(nwp)
		wp=wp/nwp;
	return wp;
}

double rpi(int team, string stats[], int teams, double owp[], double wp[]){
	int i,j,k;
	double oowp=0,nwp=0,noowp=0;
	double temp;

	//cerr<<"WP for "<<team<<" is " <<wp[team]<<endl;
	//cerr<<"OWP for "<<team<<" is " <<owp[team]<<endl;
	fi(teams){
		if(i==team) continue;
		if(stats[i][team]=='.') continue;
		oowp+=owp[i];
		noowp++;
	}
	if(noowp>0)
		oowp=oowp/noowp;
	//cerr<<"OOWP for "<<team<<" is "<<oowp<<endl;
	return 0.25*wp[team]+0.50*owp[team]+0.25*oowp;
}

int main(){
	int T;
	int i,j,k;
	cin>>T;

	for(int t=0;t<T;t++){
		int N;
		cin>>N;
		string stats[N];
		double owp[N],wp[N];
		fi(N)
			cin>>stats[i];
		cout<<"Case #"<<(t+1)<<":"<<endl;
		fi(N)
			wp[i]=wpcalc(i,stats);
		fi(N)
			owp[i]=owpminus(i,stats,N);
		fi(N)
			cout<<rpi(i,stats,N,owp,wp)<<endl;
	}
	return 0;
}
