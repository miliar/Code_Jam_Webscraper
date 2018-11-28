#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define forn(i,n) for (int i=0;i<n;++i)
#define all(a) a.begin(),a.end()
#define and 1


int col[1000000+10];
int can[1000000+10];
int type[1000000+10];
int ans[1000000+10][2];
int n;
void dfs(int v){
	if (v>(n-1)/2){
		ans[v][col[v]]=0;
		ans[v][1-col[v]]=-1;
		return;
	}
	dfs(v*2);
	dfs(v*2+1);
	ans[v][0]=-1;
	ans[v][1]=-1;

	if (type[v]==1){
		if (ans[v*2][1]!=-1&&ans[v*2+1][1]!=-1&&(ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][1]<ans[v][1]))ans[v][1]=ans[v*2][1]+ans[v*2+1][1];
		if (ans[v*2][0]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][0]==-1||ans[v*2][0]+ans[v*2+1][0]<ans[v][0] ))ans[v][0]=ans[v*2][0]+ans[v*2+1][0];
		if (ans[v*2][0]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][0]==-1||ans[v*2][0]+ans[v*2+1][1]<ans[v][0] ))ans[v][0]=ans[v*2][0]+ans[v*2+1][1];
		if (ans[v*2][1]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][0]==-1||ans[v*2][1]+ans[v*2+1][0]<ans[v][0] ))ans[v][0]=ans[v*2][1]+ans[v*2+1][0];
	}else {
		if (ans[v*2][0]!=-1&&ans[v*2+1][0]!=-1&&(ans[v][0]==-1||ans[v*2][0]+ans[v*2+1][0]<ans[v][0]))ans[v][0]=ans[v*2][0]+ans[v*2+1][0];
		if (ans[v*2][1]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][1]<ans[v][1] ))ans[v][1]=ans[v*2][1]+ans[v*2+1][1];
		if (ans[v*2][0]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][1]==-1||ans[v*2][0]+ans[v*2+1][1]<ans[v][1] ))ans[v][1]=ans[v*2][0]+ans[v*2+1][1];
		if (ans[v*2][1]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][0]<ans[v][1] ))ans[v][1]=ans[v*2][1]+ans[v*2+1][0];
	}
	if (can[v]){
		type[v]=1-type[v];
		if (type[v]==1){
			if (ans[v*2][1]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][1]+1<ans[v][1]))ans[v][1]=ans[v*2][1]+ans[v*2+1][1]+1;
			if (ans[v*2][0]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][0]==-1||ans[v*2][0]+ans[v*2+1][0]<ans[v][0]))ans[v][0]=ans[v*2][0]+ans[v*2+1][0]+1;
			if (ans[v*2][0]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][0]==-1||ans[v*2][0]+ans[v*2+1][1]<ans[v][0]))ans[v][0]=ans[v*2][0]+ans[v*2+1][1]+1;
			if (ans[v*2][1]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][0]==-1||ans[v*2][1]+ans[v*2+1][0]<ans[v][0]))ans[v][0]=ans[v*2][1]+ans[v*2+1][0]+1;
		}else {
			if (ans[v*2][0]!=-1&&ans[v*2+1][0]!=-1 && (ans[v][0]==-1 || ans[v*2][0]+ans[v*2+1][0]+1<ans[v][0]))ans[v][0]=ans[v*2][0]+ans[v*2+1][0]+1;
			if (ans[v*2][1]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][1]<ans[v][1] ))ans[v][1]=ans[v*2][1]+ans[v*2+1][1]+1;
			if (ans[v*2][0]!=-1&&ans[v*2+1][1]!=-1  && (ans[v][1]==-1||ans[v*2][0]+ans[v*2+1][1]<ans[v][1] ))ans[v][1]=ans[v*2][0]+ans[v*2+1][1]+1;
			if (ans[v*2][1]!=-1&&ans[v*2+1][0]!=-1  && (ans[v][1]==-1||ans[v*2][1]+ans[v*2+1][0]<ans[v][1] ))ans[v][1]=ans[v*2][1]+ans[v*2+1][0]+1;
		}
	}

}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nn;
	cin >> nn ;
	forn(ii,nn){
		int v;
		cin >> n  >> v;
		for (int i=1;i<=(n-1)/2;++i){
			int u,l;
			cin >> u >> l;
			can[i]=l;
			type[i]=u;
		}
		for (int i=(n-1)/2+1;i<=n;++i){
			int u;
			cin >> u;
			col[i]=u;
		}
		dfs(1);
		cout << "Case #" << ii+1 <<": ";
		if (ans[1][v]==-1)cout<<"IMPOSSIBLE"; else cout << ans[1][v];
		cout << endl;
	}
	return 0;
}