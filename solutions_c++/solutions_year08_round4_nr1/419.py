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

using namespace std;

int col[1000020], ch[1000020], ty[1000020], val[1000020][2], n;

int dfs(int v){
	if (v > (n - 1) / 2) {
		val[v][col[v]] = 0;
		val[v][1-col[v]] = -1;
		return 0;
	}
	dfs(v * 2);
	dfs(v * 2+1);
	val[v][0]=val[v][1]=-1;
	if (ty[v]==1){
		if (val[v*2][1]!=-1) {
			if (val[v*2+1][1]!=-1
					&&(val[v][1]==-1 || val[v*2][1]+val[v*2+1][1]<val[v][1]))
				val[v][1]=val[v*2][1]+val[v*2+1][1];
			if (val[v*2+1][0]!=-1
					&& (val[v][0]==-1||val[v*2][1]+val[v*2+1][0]<val[v][0]))
				val[v][0]=val[v*2][1]+val[v*2+1][0];
		}
		if (val[v*2][0]!=-1) {
			if (val[v*2+1][0]!=-1
				&& (val[v][0]==-1||val[v*2][0]+val[v*2+1][0]<val[v][0]))
			val[v][0]=val[v*2][0]+val[v*2+1][0];
			if (val[v*2+1][1]!=-1
				&& (val[v][0]==-1||val[v*2][0]+val[v*2+1][1]<val[v][0]))
			val[v][0]=val[v*2][0]+val[v*2+1][1];
		}
	} else {
		if (val[v*2][0]!=-1) {
			if (val[v*2+1][0]!=-1
				&&(val[v][0]==-1||val[v*2][0]+val[v*2+1][0]<val[v][0]))
				val[v][0]=val[v*2][0]+val[v*2+1][0];
			if (val[v*2+1][1]!=-1
				&& (val[v][1]==-1||val[v*2][0]+val[v*2+1][1]<val[v][1]))
				val[v][1]=val[v*2][0]+val[v*2+1][1];
		}
		if (val[v*2][1]!=-1) {
			if (val[v*2+1][0]!=-1
				&& (val[v][1]==-1||val[v*2][1]+val[v*2+1][0]<val[v][1]))
				val[v][1]=val[v*2][1]+val[v*2+1][0];
			if (val[v*2+1][1]!=-1
				&& (val[v][1]==-1||val[v*2][1]+val[v*2+1][1]<val[v][1]))
				val[v][1]=val[v*2][1]+val[v*2+1][1];
		}
	}
	if (ch[v]){
		ty[v]=1 - ty[v];
		if (ty[v]==1){
			if (val[v*2][0]!=-1) {
				if (val[v*2+1][0]!=-1
					&& (val[v][0]==-1||val[v*2][0]+val[v*2+1][0]<val[v][0]))
					val[v][0]=val[v*2][0]+val[v*2+1][0]+1;
				if (val[v*2+1][1]!=-1
					&& (val[v][0]==-1||val[v*2][0]+val[v*2+1][1]<val[v][0]))
					val[v][0]=val[v*2][0]+val[v*2+1][1]+1;
			}
			if (val[v*2][1]!=-1) {
				if (val[v*2+1][0]!=-1
					&& (val[v][0]==-1||val[v*2][1]+val[v*2+1][0]<val[v][0]))
					val[v][0]=val[v*2][1]+val[v*2+1][0]+1;
				if (val[v*2+1][1]!=-1
					&& (val[v][1]==-1||val[v*2][1]+val[v*2+1][1]+1<val[v][1]))
					val[v][1]=val[v*2][1]+val[v*2+1][1]+1;
			}
		}else {
			if (val[v*2][0]!=-1) {
				if (val[v*2+1][0]!=-1
					&& (val[v][0]==-1 || val[v*2][0]+val[v*2+1][0]+1<val[v][0]))
					val[v][0]=val[v*2][0]+val[v*2+1][0]+1;
				if (val[v*2+1][1]!=-1
					&& (val[v][1]==-1||val[v*2][0]+val[v*2+1][1]<val[v][1]))
					val[v][1]=val[v*2][0]+val[v*2+1][1]+1;
			}
			if (val[v*2][1]!=-1) {
				if (val[v*2+1][0]!=-1
					&& (val[v][1]==-1||val[v*2][1]+val[v*2+1][0]<val[v][1]))
					val[v][1]=val[v*2][1]+val[v*2+1][0]+1;
				if (val[v*2+1][1]!=-1
					&& (val[v][1]==-1||val[v*2][1]+val[v*2+1][1]<val[v][1]))
					val[v][1]=val[v*2][1]+val[v*2+1][1]+1;
			}
		}
	}
	return 0;
}

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);
     int test;
     cin >> test;
     for (int tt = 0; tt < test; ++tt) {
          int v;
          cin >> n >> v;
          for (int i = 1; i <= (n - 1) / 2; ++i){
               int g, c;
               cin >> g >> c;
               ch[i] = c;
               ty[i] = g;
          }
          for (int i = (n - 1) / 2 + 1; i <= n; ++i){
               int I;
               cin >> I;
               col[i] = I;
          }
          dfs(1);
          cout << "Case #" << tt+1 <<": ";
          if (val[1][v] == -1)
			  cout << "IMPOSSIBLE";
		  else
			  cout << val[1][v];
          cout << endl;
     }
     return 0;
}