#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define all(a) (a).begin(),(a).end()
#define FR(i,x,y) for(int i=x;i<y;++i)
#define FRZ(i,y) FR(i,0,y)
typedef long long int ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<string,string> ds;
typedef pair<int,ds> ii;
#define PB push_back
#define SZ(a) (int)(a).size()
#define GI ({int t ;scanf("%d",&t);t;})
int R,C;
int ip[102][102],val[102][102];
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int dfs(int x,int y, int no)
{
    if(val[x][y])
	return val[x][y];
    int mini = INT_MAX;
    FRZ(i,4)
    {
	int nx = x + dx[i];
	int ny = y + dy[i];
	if(nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
	if(ip[x][y] > ip[nx][ny])
	    mini <?= ip[nx][ny];
    }
    if(mini == INT_MAX)
    {
	val[x][y] = no;
	return no;
    }
    else
    {
	FRZ(i,4)
	{
	    int nx = x + dx[i];
	    int ny = y + dy[i];
	    if(nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
	    if(mini == ip[nx][ny])
		return val[x][y] = dfs(nx,ny,no);
	}
    }
}
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	printf("Case #%d:\n",nc);
	R = GI;
	C = GI;
	FRZ(i,R)
	    FRZ(j,C)
	    ip[i][j] = GI;
	int no = 1;
	memset(val,0,sizeof val);
	FRZ(i,R)
	    FRZ(j,C)
	    dfs(i,j,no++);
	map<int,int> mp;
	int ch = 0;
	FRZ(i,R)
	    FRZ(j,C)
		if(mp.find(val[i][j]) != mp.end());
		else
		    mp[val[i][j]] = ch++;
	FRZ(i,R)
	{
	    cout << (char)(mp[val[i][0]] + 'a');
	    FR(j,1,C)
		cout << " " << (char)(mp[val[i][j]] + 'a');
	    cout << endl;
	}
    }
}
