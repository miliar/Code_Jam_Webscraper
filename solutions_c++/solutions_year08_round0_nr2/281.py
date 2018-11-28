#include<iostream>
#include<vector>
#include<string>
using namespace std;

class timetable{
public:
	int dept, ariv, type;
	timetable(){}
	timetable( string d, string a, int t ){
		dept = d[0]*60+d[1];
		ariv = d[3]*60+d[4];
		type = t;
	}

	int operator<( const timetable &b) const{
		const timetable &a = *this;
		if( a.dept != b.dept ) return a.dept < b.dept;
		if( a.ariv != b.ariv ) return a.ariv < b.ariv;
		return a,type < b.type;
	}
};

int main(){
	int n;
	for( int m=0; m<n; m++ ){
		int na,nb,t;
		cin >> t;
		cin >> na >> nb;

		vector<timetable> tt(0);
		for( int i = 0; i < na; i++ ){
			string d,a;
			cin >> d >> a;
			timetable ttt( d, a, 0);
			tt.push_back(ttt);
		}
		for( int i = 0; i < nb; i++ ){
			string d,a;
			cin >> d >> a;
			timetable ttt( d, a, 1);
			tt.push_back(ttt);
		}
		sort( tt.begin(), tt.end() );
	}
}
