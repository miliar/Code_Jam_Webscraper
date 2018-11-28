#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e12,EPS=1e-9;

int main()
{
	int CS; cin>>CS;
	rep(cs,CS)
	{
		int n,k; cin>>n>>k;
		vs bd;
		rep(i,n)
		{
			string str,str2; cin>>str;
			rp(j,str)if(str[j]!='.')str2.pb(str[j]);
			
			bd.pb(str2);
		}
		
		//gravity and rotation
		vs tmp(n,string(n,'.'));
		rep(i,n)
		{
			int l=bd[i].size();
			rep(j,l)tmp[i][n-l+j]=bd[i][j];
		}
		bd=tmp;
		
		rep(i,n)rep(j,n)tmp[j][n-1-i]=bd[i][j];
		bd=tmp;
		
		rep(i,n)cerr<<tmp[i]<<endl;
		
		
		bool r=0,b=0;
		rep(i,n)rep(j,n)
		{
			if(bd[i][j]=='.'||r&&bd[i][j]=='R'||b&&bd[i][j]=='B')continue;
			
			int c,cx,cy;
			//row
			for(c=1,cy=i,cx=j;c<k;c++)
			{
				if(cx+1>=n||bd[cy][cx]!=bd[cy][cx+1])break;
				cx++;
			}
			if(c==k)
			{
				bd[i][j]=='R'?(r=1):(b=1);
				continue;
			}
			
			//col
			for(c=1,cy=i,cx=j;c<k;c++)
			{
				if(cy+1>=n||bd[cy][cx]!=bd[cy+1][cx])break;
				cy++;
			}
			if(c==k)
			{
				bd[i][j]=='R'?(r=1):(b=1);
				continue;
			}
			
			//dia1
			for(c=1,cy=i,cx=j;c<k;c++)
			{
				if(cx+1>=n||cy+1>=n||bd[cy][cx]!=bd[cy+1][cx+1])break;
				cx++,cy++;
			}
			if(c==k)
			{
				bd[i][j]=='R'?(r=1):(b=1);
				continue;
			}
			//dia1
			for(c=1,cy=i,cx=j;c<k;c++)
			{
				if(cx+1>=n||cy-1<0||bd[cy][cx]!=bd[cy-1][cx+1])break;
				cx++,cy--;
			}
			if(c==k)
			{
				bd[i][j]=='R'?(r=1):(b=1);
				continue;
			}
		}
		
		cout<<"Case #"<<cs+1<<": ";
		if(r&&b)cout<<"Both";
		else if(!r&&!b)cout<<"Neither";
		else cout<<(r?"Red":"Blue");
		
		cout<<endl;
	}
	
	return 0;
}
