#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <list>
#include <iostream> 
#include <cmath> 
#include <string> 
#include <cstring> 
#include <set> 
#include <map> 
#include <vector> 
#include <cstdio> 
using namespace std; 


#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset((a),(b),sizeof(a))

#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;


int main() {
 	freopen("A.txt","r",stdin);
 	freopen("AOUT.txt","w",stdout);
	int T, cI=1;
	cin >> T;
	while (T--)
	{
		
		int R,C;cin>>R>>C;
		char s[55][55];
		REP(i,R)REP(j,C)cin>>s[i][j];//[scanf("%c",&s[i][j]);
		bool vis[55][55];CL(vis,false);
		bool ok=true;
		REP(i,R)if(ok)REP(j,C)
		{
			if(vis[i][j])continue;
			if(s[i][j]=='#')
			{
				if(i==R-1||j==C-1)
				{
					ok=false;break;
				}
				if(s[i][j+1]!='#'||s[i+1][j]!='#'||s[i+1][j+1]!='#')
				{
					ok=false;break;
				}
				vis[i][j]=vis[i+1][j]=vis[i+1][j]=vis[i+1][j+1]=true;
				s[i][j]='/';s[i+1][j]='\\';
				s[i+1][j+1]='/';s[i][j+1]='\\';
			}
		
		}
		if(!ok)
		cout<<"Case #"<<cI++<<":"<<endl<<"Impossible"<<endl;
		else 
		{
				cout<<"Case #"<<cI++<<":"<<endl;
				REP(i,R)
				{REP(j,C)
				cout<<s[i][j];cout<<endl;}
		}
			
	}
    
	return 0;
}
