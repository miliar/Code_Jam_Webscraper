#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cmath>

using namespace std ;

#define forsn(i, s, n) for (int i = s ; i < n ; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define fori(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define all(n) n.begin(), n.end()
#define pb push_back

#define x first
#define y second


#define eps 0.0001
#define INF 1000000
#define mp make_pair
#define dbg(x) cout<<#x<<' '<<x<<endl

typedef long double ldouble;

char tab[4][4];
int main()
{
	int t;
	cin>>t;
	forn(caso,t){
		forn(i,4)forn(j,4)cin>>tab[i][j];
		bool flagO=false;
		bool flagX=false;
		bool flagP=false;
		bool flag;
		
		//O
		forn(i,4){
			flag=true;
			forn(j,4)if(tab[i][j]=='X' || tab[i][j]=='.')flag=false;
			if(flag)flagO=true;
		} 
		forn(j,4){
			flag=true;
			forn(i,4)if(tab[i][j]=='X' || tab[i][j]=='.')flag=false;
			if(flag)flagO=true;
		} 
		flag=true;		
		forn(i,4)if(tab[i][i]=='X' || tab[i][i]=='.')flag=false;
		if(flag)flagO=true;
		flag=true;		
		forn(i,4)if(tab[i][3-i]=='X' || tab[i][3-i]=='.')flag=false;
		if(flag)flagO=true;
		
		//X
		forn(i,4){
			flag=true;
			forn(j,4)if(tab[i][j]=='O' || tab[i][j]=='.')flag=false;
			if(flag)flagX=true;
		} 
		forn(j,4){
			flag=true;
			forn(i,4)if(tab[i][j]=='O' || tab[i][j]=='.')flag=false;
			if(flag)flagX=true;
		} 
		flag=true;		
		forn(i,4)if(tab[i][i]=='O' || tab[i][i]=='.')flag=false;
		if(flag)flagX=true;
		flag=true;		
		forn(i,4)if(tab[i][3-i]=='O' || tab[i][3-i]=='.')flag=false;
		if(flag)flagX=true;
		//P
		forn(i,4)forn(j,4)if(tab[i][j]=='.')flagP=true;
		
		cout<<"Case #"<<caso+1<<": ";
		if(flagO)cout<<"O won"<<endl;
		else if(flagX)cout<<"X won"<<endl;
		else if(flagP)cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	}
}


