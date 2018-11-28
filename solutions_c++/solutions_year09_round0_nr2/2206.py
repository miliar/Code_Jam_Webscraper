#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
#define FOR0(i,n) for (i = 0; i < n; i++) 
#define FOR1(i,n) for (i = 1; i <= n; i++)
#define INF 1000000000
int i,j,k;

int T,H,W;
int maps[101][101];
char dp[101][101];
char label;

char DFS(int i,int j);
int main()
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);
	cin>>T;
	FOR1(i,T){
		label = 'a';
		memset(dp,'A',sizeof(dp));
		cin>>H>>W;
		FOR0(j,H)
			FOR0(k,W)
				cin>>maps[j][k];
		
		FOR0(j,H)
			FOR0(k,W)
				DFS(j,k);

		cout<<"Case #"<<i<<":"<<endl;
		FOR0(j,H)
		{
			FOR0(k,W){
				if(k != 0) cout<<" "<<dp[j][k];
				else cout<<dp[j][k];
			}
			cout<<endl;
		}
	}
	return 0;
}

char DFS(int i,int j)
{
	if(dp[i][j] != 'A') return dp[i][j];
	int north = INF,south = INF,west = INF,east = INF;
	if((i - 1) >= 0) north = maps[i - 1][j];
	if((i + 1) < H) south = maps[i + 1][j];
	if((j - 1) >= 0) west = maps[i][j - 1];
	if((j + 1) < W) east = maps[i][j + 1];
	char tmp;
	if(north == INF && south == INF && west == INF && east == INF)
		tmp = label++;
	else if(maps[i][j] > north && north <= south && north <= west && north <= east) 
		tmp = DFS(i - 1,j);
	else if(maps[i][j] > west &&west <= south && west <= north && west <= east)  
		tmp = DFS(i,j - 1);
	else if(maps[i][j] > east && east <= south && east <= west && east <= north)  
		tmp = DFS(i,j + 1);
	else if(maps[i][j] > south && south <= north && south <= west && south <= east)  
		tmp = DFS(i + 1,j);
	else
		tmp = label++;
	return dp[i][j] = tmp;
}