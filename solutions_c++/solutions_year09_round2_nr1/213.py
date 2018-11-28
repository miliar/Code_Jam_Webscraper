#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

struct Miastowa {
	int parent, lewy, prawy;
	double prob;
	string feature;

	Miastowa(){
		clear();
	}

	void clear(){
		feature = "";
		parent = -1;
		lewy = -1;
		prawy = -1;
		prob = 0.0;
	}
};
Miastowa m[1000];

void wypisz(int gdzie){
	if( gdzie < 0 ) return;
	cout << "gdzie: " << gdzie << " feature: " << m[gdzie].feature << " prob: " << m[gdzie].prob << " lewy: " << m[gdzie].lewy << " prawy: " << m[gdzie].prawy << " parent: " << m[gdzie].parent << endl;
	wypisz( m[gdzie].lewy );
	wypisz( m[gdzie].prawy );
}

string nazwa;
int ileF;
string tmp;
set<string> mapa;
double res;

void go(int gdzie){
	res *= m[gdzie].prob;
//cerr << gdzie << " : " << res << endl;
	if( m[gdzie].lewy == -1 && m[gdzie].prawy == -1) return;		
	
	if( mapa.find( m[gdzie].feature ) != mapa.end() ){
		go( m[gdzie].lewy );
	} else {
		go( m[gdzie].prawy );
	}
}

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		fu(a,1000) m[a].clear();

		int ileLinii;
		scanf("%d",&ileLinii);
		int gdzie = 0, ile = 1;
		char c;
	
	while( 1 ){
		while( (c=getchar()) != '(' && c!=EOF );

		hell:

		while( (c=getchar()) < '0' || c > '9');
		m[gdzie].prob = c-'0';
		if( (c=getchar()) != '.' ){
			cerr << "Kuzwa nie ma kropki" << endl;
		}
		double wsp = 0.1;
		while( (c=getchar()) >= '0' && c <= '9' ){
			m[gdzie].prob += (c-'0') * wsp;
			wsp /= 10;
		}

//cerr << "sciagnelismy prob -> " << m[gdzie].prob << " || " << gdzie << endl;
		
		hell2:
		
		if( c != ')' && !(c>='a' && c<='z') && c != '(' )		
			while( (c=getchar()) != ')' && !(c>='a' && c<='z') && c != '(' );

		if( c == ')' ){
//cerr << "koniec sekcji || gdzie: " << gdzie << " parent: " << m[gdzie].parent << endl;
			gdzie = m[gdzie].parent;	
			while( gdzie >= 0 && m[gdzie].prawy != -1 ) gdzie = m[gdzie].parent;
			if( gdzie < 0 ){
//				cerr << "chyba koniec" << endl;
				break;
			}
			m[gdzie].prawy = ile;
			m[ile].parent = gdzie;
			gdzie = ile;
			ile++;
			continue;
		} else if( c >= 'a' && c <= 'z' ){
			m[gdzie].feature = c;
			while( (c=getchar()) >= 'a' && c <= 'z' ) m[gdzie].feature = m[gdzie].feature + c;	
//cerr << "sciagnelismy feature -> " << m[gdzie].feature << " || " << gdzie << endl;
			
			goto hell2;
		} else if( c == '(' ){
			m[gdzie].lewy = ile;
			m[ile].parent = gdzie;
			gdzie = ile;
			ile++;	
			goto hell;
		}
	}
		
		//wypisz(0);		
		
		int ileA;
		while( (c=getchar()) < '0' || c > '9') ;
		ileA = c-'0';
		while( (c=getchar()) >= '0' && c <= '9') ileA = ileA * 10 + c-'0';


//		scanf("%d",&ileA);

//		cerr << "ileA => " << ileA << endl;
		
		printf("Case #%d:\n",q);

		fu(a,ileA){
			mapa.clear();
				
			cin >> nazwa;
			cin >> ileF;
			fu(b,ileF){
				cin >> tmp;
				mapa.insert( tmp );
			}
			
			res = 1.0;	
			go(0);

			printf("%.7f\n",res);
		}

	}

	return 0;
}
