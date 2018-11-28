#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <memory.h>
#include <ctime>
//#include <fstream>
using namespace std;
 
using namespace std;

#define INF 1000000000
#define MP make_pair
#define FILL(a,value) memset(a,value,sizeof(a))
#define MOD 1000000009
double const PI = acos(-1.0);
double const EPS=1e-7;

string a[4];

bool X(){
	for (int i=0; i<4; i++){
		bool ok=1;
		for (int j=0; j<4; j++){
			if (a[i][j]=='.' || a[i][j]=='O') ok=0;
		}
		if (ok) return 1;
	}

	for (int i=0; i<4; i++){
		bool ok=1;
		for (int j=0; j<4; j++){
			if (a[j][i]=='.' || a[j][i]=='O') ok=0;
		}
		if (ok) return 1;
	}

	bool ok=1;

	for (int i=0; i<4; i++){
		if (a[i][i]=='.' || a[i][i]=='O') ok=0;
	}

	if (ok) return 1;
	ok=1;

	for (int i=0; i<4; i++){
		if (a[i][3-i]=='.' || a[i][3-i]=='O') ok=0;
	}

	if (ok) return 1;
	return 0;
}

bool O(){
	for (int i=0; i<4; i++){
		bool ok=1;
		for (int j=0; j<4; j++){
			if (a[i][j]=='.' || a[i][j]=='X') ok=0;
		}
		if (ok) return 1;
	}

	for (int i=0; i<4; i++){
		bool ok=1;
		for (int j=0; j<4; j++){
			if (a[j][i]=='.' || a[j][i]=='X') ok=0;
		}
		if (ok) return 1;
	}

	bool ok=1;

	for (int i=0; i<4; i++){
		if (a[i][i]=='.' || a[i][i]=='X') ok=0;
	}

	if (ok) return 1;
	ok=1;

	for (int i=0; i<4; i++){
		if (a[i][3-i]=='.' || a[i][3-i]=='X') ok=0;
	}

	if (ok) return 1;
	return 0;
}

bool XO(){
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (a[i][j]=='.') return 1;
		}
	}
	return 0;
}

void solve(){
	cin>>a[0]>>a[1]>>a[2]>>a[3];

	if (X()) cout<<"X won"<<endl;
	else if (O()) cout<<"O won"<<endl;
	else if (XO()) cout<<"Game has not completed"<<endl;
	else cout<<"Draw"<<endl;
}

int main(){

	freopen("in.txt","r",stdin);
	freopen("OUTPUT.txt","w",stdout);

	int tt;
	cin>>tt;

	//string str;
	//getline(cin,str);

	for (int t=1; t<=tt; t++){
		cout<<"Case #"<<t<<": ";
		int time=clock();
		solve();
		cerr<<"\t\tCase #"<<t<<"\t time="<<clock()-time<<endl;
	}

}