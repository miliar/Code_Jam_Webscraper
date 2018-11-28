///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define formn(i,m,n) for(int i=m;i<(int)n;i++)
#define dformn(i,m,n) for(int i=n-1;i>=m;i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

string state[4]={"Draw","X won","O won","Game has not completed"};

int t[4][4];

int main(){
freopen("AlargeInput.txt","r",stdin);
freopen("AlargeOutput.txt","w",stdout);
	int TC;cin>>TC;
	formn(tc,1,TC+1){
		
		int res = 0;///El tablero esta lleno.
		forn(i,4) forn(j,4){
			char c;cin>>c;
			if(c=='X') t[i][j] = 1000;
			else if(c=='O') t[i][j] = 100;
			else if(c=='T') t[i][j] = 10;
			else{
				t[i][j] = 1;
				res = 3;///El tablero no esta lleno.
			}
		}
		
		///Filas.
		forn(r,4){
			int sum = 0;
			forn(c,4) sum += t[r][c];
			if(sum == 4000 || sum == 3010) res = 1;
			if(sum == 400 || sum == 310) res = 2;
		}
		
		///Columnas.
		forn(c,4){
			int sum = 0;
			forn(r,4) sum += t[r][c];
			if(sum == 4000 || sum == 3010) res = 1;
			if(sum == 400 || sum == 310) res = 2;
		}
		
		///Diag Dom.
		int sum = 0;
		forn(i,4) sum += t[i][i];
		if(sum == 4000 || sum == 3010) res = 1;
		if(sum == 400 || sum == 310) res = 2;
		
		///Diag No Dom.
		sum = 0;
		forn(i,4) sum += t[i][3-i];
		if(sum == 4000 || sum == 3010) res = 1;
		if(sum == 400 || sum == 310) res = 2;
		
		cout<<"Case #"<<tc<<": "<<state[res]<<endl;
		
	}
    return 0;
}
