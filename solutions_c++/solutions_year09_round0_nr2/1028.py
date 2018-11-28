#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
#define MP make_pair
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}

struct node{
	int r,c;
	node(){}
	node(int rr,int cc){r=rr; c=cc;}
};

int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};

int H,W,a[105][105],b[105][105];
int k;

void bfs(int rr,int cc)
{
	if(b[rr][cc]!=-1) return;
	queue<node> q;
	q.push(node(rr,cc));
	while(!q.empty())
	{
		node t=q.front();
		q.pop();
		
		int r,c,h=a[t.r][t.c];
		for(int i=0;i<4;i++)
		{
			int rr,cc;
			rr=t.r+dr[i];
			cc=t.c+dc[i];
			if(rr<0 || cc<0 || rr>=H || cc>=W) continue;
			if(a[rr][cc]<h){
				r=rr;
				c=cc;
				h=a[rr][cc];
			}
		}
		if(h==a[t.r][t.c]){
			b[t.r][t.c]=k++;
			continue;
		}	
		if(b[r][c]==-1)
			q.push(node(r,c));
		else
			b[t.r][t.c]=b[r][c];
	}
}
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>H>>W;
		for(int r=0;r<H;r++)
			for(int c=0;c<W;c++)
				cin>>a[r][c];
		
		memset(b,-1,sizeof(b));
		k=0;
		
		vector< pair<int,pii> > v;
		for(int r=0;r<H;r++)
			for(int c=0;c<W;c++)
				v.PB(MP(a[r][c],MP(r,c)));
		sort(all(v));
		for(int i=0;i<v.size();i++)
			bfs(v[i].second.first,v[i].second.second);
			
		char res[105][105];
		char ch='a';
		char mp[30];	
		bool done[30];
		memset(done,0,sizeof(done));
		for(int r=0;r<H;r++){
			for(int c=0;c<W;c++){
				if(done[b[r][c]]) continue;
				done[b[r][c]]=1;
				mp[b[r][c]]=ch++;
			}	
		}
		for(int r=0;r<H;r++)
			for(int c=0;c<W;c++)
				res[r][c]=mp[b[r][c]];		
				
		printf("Case #%d:\n",t);
		for(int r=0;r<H;r++){
			cout<<res[r][0];
			for(int c=1;c<W;c++)
				cout<<" "<<res[r][c];
			cout<<endl;
		}			
	}
}