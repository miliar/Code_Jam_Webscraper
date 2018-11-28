#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <iterator>
#define EPS 1e-9
#pragma comment(linker, "/STACK:256000000")

using namespace std;

void solve(){
	int n,m;
	cin>>n>>m;
	char a[100][100];
	memset(a,0,sizeof(a));
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			cin>>a[i][j];
		}
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			if (a[i][j]=='#' && a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#'){
				a[i][j]='/';
				a[i+1][j+1]='/';
				a[i][j+1]='\\';
				a[i+1][j]='\\';
			}
			if (a[i][j]=='#'){
				cout<<endl<<"Impossible";
				return;
			}
		}
	}
	for (int i=0;i<n;i++){
		cout<<endl;
		for (int j=0;j<m;j++){
			cout<<a[i][j];
		}
	}
	return;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int z=1;z<=t;z++){
		cout<<"Case #"<<z<<":";
		solve();
		cout<<endl;
	}
	return 0;
	//cout.setf(ios::fixed);cout.precision(20);
}