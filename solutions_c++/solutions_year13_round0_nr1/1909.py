#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<map>
#include<algorithm>
using namespace std;


typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define pb push_back
#define mp make_pair
#define snd second
#define fst first
#define debug printf("--%d--\n",__LINE__)

int T;

int main(void){
	cin >> T;
	bool orz;
	string c = "XO";
	string s[4];
	for(int cn=1;cn<=T;cn++){
		for(int i=0;i<4;i++){
			cin >> s[i];
		}
		
		bool winflg[2], full = true;
		for(int i=0;i<2;i++) winflg[i] = false;
		
		
		for(int h=0;h<2;h++){
			for(int i=0;i<4;i++){
				orz = false;
				for(int j=0;j<4;j++){
					if (s[i][j]!=c[h] && s[i][j]!='T') {orz = true;break;}
				}
				if (!orz) winflg[h] = true;
			}
			for(int i=0;i<4;i++){
				orz = false;
				for(int j=0;j<4;j++){
					if (s[j][i]!=c[h] && s[j][i]!='T') {orz = true;break;}
				}
				if (!orz) winflg[h] = true;
			}
			orz = false;
			for(int i=0;i<4;i++){
				if (s[i][i]!=c[h] && s[i][i]!='T') {orz = true;break;}
			}
			if (!orz) winflg[h] = true;
			orz = false;
			for(int i=0;i<4;i++){
				if (s[i][3-i]!=c[h] && s[i][3-i]!='T') {orz = true;break;}
			}
			if (!orz) winflg[h] = true;
		}
		
		
		cout << "Case #" << cn << ": ";
		
		if (winflg[0]) cout << "X won";
		else if (winflg[1]) cout << "O won";
		else{
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if (s[i][j]=='.') full = false;
				}
			}
			if (full) cout << "Draw";
			else cout << "Game has not completed";
		}
		cout << endl;
	}
	return 0;
}
