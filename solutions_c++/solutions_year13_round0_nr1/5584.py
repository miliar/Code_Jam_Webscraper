#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX (int)10e6

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;
typedef unsigned long long hash;

int n;
string in;
vector <string> v;
int solve(){
	// return 1 if x is the winner
	//return 2 if O is the winner
	//return 0 if is a draw;
	//return -1 otherwise

	//check row
	int sumx = 0 , sumo = 0;
	int dots = 0;
	// printf("row\n");
	for(int j=0; j<v.size(); ++j){
		for(int i=0; i<v[j].size(); ++i){
			// printf("%c ",v[j][i]);
			if(v[j][i] == 'X')
				sumx++;
			else if(v[j][i] == 'O')
				sumo++;
			else if(v[j][i] == '.') dots++;
			else{
				if(sumx > sumo) sumx++;
				else sumo++;
			}
		}
		// printf("\n");
		if(sumx == 4) return 1;
		else if(sumo == 4) return 2;
		sumx = 0;
		sumo = 0;

	}
	
	sumx = 0;
	sumo = 0;
	//check columns
	// printf("columns\n");
	for(int j=0; j<v.size(); ++j){
		for(int i=0; i<v[j].size(); ++i){
			if(v[i][j] == 'X')
				sumx++;
			else if(v[i][j] == 'O')
				sumo++;
			else if(v[i][j] == '.') dots++;
			else{
				if(sumx > sumo) sumx++;
				else sumo++;
			}
		}
		if(sumx == 4) return 1;
		else if(sumo == 4) return 2;
		sumx = 0;
		sumo = 0;
	}

	sumx = 0;
	sumo = 0;
	//check first diagonal
	// printf("main\n");
	for(int i=0; i<v.size(); ++i){
		if(v[i][i] == 'X')
			sumx++;
		else if(v[i][i] == 'O')
			sumo++;
		else if(v[i][i] == '.') dots++;
		else{
			if(sumx > sumo) sumx++;
			else sumo++;
		}
	}
	if(sumx == 4) return 1;
	else if(sumo == 4) return 2;

	sumx = 0;
	sumo = 0;
	// printf("secon\n");
	//check the second diagonal
	for(int i=0, j=v.size()-1; i<v.size(); ++i,--j){
		if(v[i][j] == 'X')
			sumx++;
		else if(v[i][j] == 'O')
			sumo++;
		else if(v[i][j] == '.') dots++;
		else{
			if(sumx > sumo) sumx++;
			else sumo++;
		}
	}
	if(sumx == 4) return 1;
	else if(sumo == 4) return 2;

	if(!dots) return 0;
	return -1;
}
int main (int argc,char *argv[]){
	scanf("%d",&n);
	for(int i=0; i<n; ++i){
		v.clear();
		for(int j=0; j<4; ++j){
			cin >> in;
			v.pb(in);
		}
		int ret = solve();
		printf("Case #%d: ",i+1);
		if(ret == 1) printf("X won\n");
		else if(ret == 2) printf("O won\n");
		else if(!ret) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
