#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

#define forn(i,n) for( int i=0 ; i<(n) ; ++i )
#define forall(i,c) for( typeof( (c).begin() ) i = (c).begin() ; i != (c).end() ; ++i )
#define all(c) (c).begin() , (c).end()
#define entre(a,b,c) (((a)<=(b))&&((b)<(c)))
#define debug(x) cout << __LINE__ << " => " << __func__/*__PRETTY_FUNCTION__*/ << " => " << #x << " = " << (x) 
using namespace std;

template <class T> ostream& operator<<( ostream& o , vector<T>& v ){
	o << '[';
	for( int i=0 ; i < v.size() ; ++i )
		o << v[i] << ',';
	o << "\b]\n";
	return o;
}

template <class U, class V> ostream& operator<<( ostream& o , pair<U,V>& p ){
	o << '(' << p.first << ',' << p.second << ')';
	return o;
}

#define wel(n) if(welcome[n-1]) welcome[n]=(welcome[n]+welcome[n-1])%10000

int N;
string s;

int main(){
	cin >> N;
	getline( cin, s );
	forn( i, N ){
		vector<int> welcome(19,0);
		getline( cin, s);
//		debug(s);
		forall(j,s){
			switch (*j){
				case 'w':
					welcome[0]++;
					break;
				case 'e':
					wel(1);
					wel(6);
					wel(14);
					break;
				case 'l':
					wel(2);
					break;
				case 'c':
					wel(3);
					wel(11);
					break;
				case 'o':
					wel(4);
					wel(9);
					wel(12);
					break;
				case 'm':
					wel(5);
					wel(18);
					break;
				case ' ':
					wel(7);
					wel(10);
					wel(15);
					break;
				case 't':
					wel(8);
					break;
				case 'd':
					wel(13);
					break;
				case 'j':
					wel(16);
					break;
				case 'a':
					wel(17);
					break;
			}
//			debug(welcome);
		}
		cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << welcome[18] << endl;
	}
}