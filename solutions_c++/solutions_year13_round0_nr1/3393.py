/*
ID: rohangu1
LANG: C++
TASK: 
*/

#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <set>
#include <string>
#include <queue>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef long long LL;

#define np next_permutation
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define tr(c, it) \
		for(typeof(c.begin()) it = c.begin() ; it != c.end() ; it++)
#define max(a,b) (a>b?(a):(b))
#define min(a,b) (a>b?(b):(a))
#define all(a) (a).begin(),(a).end()
#define mp(i,j) make_pair(i,j)
#define sz(a) a.size()
#define pb(i) push_back(i) 
#define fx first
#define sx second
#define MOD 1000000007

ifstream in("tictac.in",ifstream::in);
ofstream out("tictac.out",ios::out);

char a[6][6];

void print(){
	int i;
	FOR(i,1,4){
		cout<<a[i]+1<<endl;;
	}
	cout<<"\n";
}

bool isover(){
	int i,j;
	FOR(i,1,4){
		FOR(j,1,4){
			if(a[i][j]=='.')
				return false;
		}
	}
	return true;
}

int result(){
	int i,j;
	bool xwin,owin;
	FOR(i,1,4){
		xwin = owin = true;
		FOR(j,1,4){
			if((a[i][j]=='O'||a[i][j]=='T')&&owin)
				owin =true;
			else
				owin = false;
			if((a[i][j]=='X'||a[i][j]=='T')&&xwin)
				xwin =true;
			else
				xwin = false;
		}
		if(xwin)
			return 1;
		if(owin)
			return 2;
		xwin = owin = true;
		FOR(j,1,4){
			if((a[j][i]=='O'||a[j][i]=='T')&&owin)
				owin =true;
			else
				owin = false;
			if((a[j][i]=='X'||a[j][i]=='T')&&xwin)
				xwin =true;
			else
				xwin = false;
		}
		if(xwin)
			return 1;
		if(owin)
			return 2;
	}
	xwin = owin = true;
	FOR(i,1,4){
		if((a[i][i]=='O'||a[i][i]=='T')&&owin)
			owin =true;
		else
			owin = false;
		if((a[i][i]=='X'||a[i][i]=='T')&&xwin)
			xwin = true;
		else
			xwin = false;
	}
	if(xwin)
		return 1;
	if(owin)
		return 2;
	xwin = owin = true;
	FOR(i,1,4){
		if((a[i][5-i]=='O'||a[i][5-i]=='T')&&owin)
			owin =true;
		else
			owin = false;
		if((a[i][5-i]=='X'||a[i][5-i]=='T')&&xwin)
			xwin =true;
		else
			xwin = false;
	}
	if(xwin)
		return 1;
	if(owin)
		return 2;
	return 3;
}

int main(){
	int i,j;
	int n,c,t;
	bool over;
	in>>t;
	FOR(c,1,t){
		FOR(i,1,4){
			in>>a[i]+1;
		}
		over = isover();
		j = result();
		out<<"Case #"<<c<<": ";
		if(j==3){
			if(over)
				out<<"Draw"<<endl;
			else
				out<<"Game has not completed"<<endl;
		}
		else{
			if(j==1)
				out<<"X won"<<endl;
			if(j==2)
				out<<"O won"<<endl;
		}	
	}
	return 0;
}
