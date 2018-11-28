#include<vector>
#include<string>
#include<map>
#include<set>
#include<utility>
#include<algorithm>
#include<cmath>
#include<iostream>
#include<cstdio>

using namespace std;

#define FOR(A,B) for(int A;A<B.size();++A)
#define X first
#define Y second
#define LI size()-1
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=0;tt<t;++tt){
		int w,h;
		cin >> h >> w;
		vector< vector< char> > m(h, vector<char>(w));
		for(int i=0;i<h;++i){
			for(int j=0;j<w;++j){
				cin >> m[i][j];
			}
		}
		for(int i=0;i<h-1;++i){
			for(int j=0;j<w-1;++j){
				if (m[i][j]=='#' && m[i][j+1]=='#' && m[i+1][j]=='#' && m[i+1][j+1]=='#'){
					m[i][j]  ='/'; m[i][j+1]='\\';
					m[i+1][j]='\\';m[i+1][j+1]='/';
				}
			}
		}
		bool ok =true;
		for(int i=0;i<h &&  ok;++i){
			for(int j=0;j<w && ok ;++j){
				if (m[i][j]=='#'){
					ok = false;
					break;
				}
			}
		}
		cout << "Case #"<< tt+1 << ":" << endl;
		if (ok){
			for(int i=0;i<h;++i){
				for(int j=0;j<w;++j){
					cout << m[i][j];
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}