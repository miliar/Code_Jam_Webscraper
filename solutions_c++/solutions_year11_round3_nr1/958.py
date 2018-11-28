#include<iostream>
#include<stack>
#include<algorithm>
#include<vector>
#include<map>
#include<cstdlib>
#include<cstdio>
#include<sstream>
#include<string>
#include<cassert>
#include<iomanip>
#include<ctime>
#include<set>
#include<cstring>
#include<cmath>
#include<queue>
#include<cassert>
#define ull unsigned long long
#define MP make_pair
#define pb push_back
#ifndef INT_MAX
#define INT_MAX (1<<30)
#endif
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

int R,C;
char g[60][60];
bool tr(int x,int y){
	if(x+1>=R||y+1>=C)return false;
	if(g[x+1][y]!='#'||g[x][y+1]!='#'||g[x+1][y+1]!='#')return false;
	g[x][y]='/';
	g[x+1][y]='\\';
	g[x][y+1]='\\';
	g[x+1][y+1]='/';
	return true;
}

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int Test;cin>>Test;
	for(int test=1;test<=Test;test++){
		cin>>R>>C;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				cin>>g[i][j];
			}
		}
		bool succ=true;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(g[i][j]=='#'){
					succ&=tr(i,j);
				}
			}
		}
		
		cout<<"Case #"<<test<<": ";
		cout<<endl;
		if(succ){
			for(int i=0;i<R;i++){
				for(int j=0;j<C;j++){
					cout<<g[i][j];
				}
				cout<<endl;
			}
		}
		else cout<<"Impossible"<<endl;

	}
	return 0;
}
