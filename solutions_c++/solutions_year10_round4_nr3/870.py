#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())

typedef long long  LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair< int, int > PII;

const int inf=1000000000;
int mat[110][110];
int main()
{
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		cout << "Case #" << (test) << ": ";
		for(int i=0;i<110;i++)for(int j=0;j<110;j++)	mat[i][j]=0;
		int r;
		scanf("%d",&r);
		int x1,y1,x2,y2,c=0,minx=inf,miny=inf,maxx=0,maxy=0;
		for(int i=0;i<r;i++){
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			if(x1>x2)swap(x1,x2);
			if(y1>y2)swap(y1,y2);
			minx=min(minx,x1);miny=min(miny,y1);maxx=max(maxx,x2);maxy=max(maxy,y2);
			for(int i=x1;i<=x2;i++)
			for(int j=y1;j<=y2;j++)
				if(!mat[i][j]){
					mat[i][j]=1;
					c++;
				}
		}	
		int ans=0;
		while(c){
			for(int i=maxx;i>=minx;i--)
			for(int j=maxy;j>=miny;j--)
			{
				if(mat[i][j]==0 && mat[i-1][j]==1 && mat[i][j-1]==1)	{mat[i][j]=1;c++;}
				else if(mat[i][j]==1 && mat[i-1][j]==0 && mat[i][j-1]==0)	{mat[i][j]=0;c--;}
			}
			ans++;
		}
		cout<<ans<<endl;		
				
	}	
	return 0;
}	


