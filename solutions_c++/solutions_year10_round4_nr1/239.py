#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>
#define mp make_pair
#define pb push_back                     
#define int64 long long
#define ld long double  
#define setval(a,v) memset(a,v,sizeof(a))
using namespace std;

int n;
int a[60][60];

void readdata(){
	cin>>n;
	for (int i=0;i<5*n;i++)
		for (int j=0;j<5*n;j++)
			a[i][j]=10;
	vector<vector<int> > v(2*n);
	for (int i=0;i<2*n-1;i++){
		int sz;
		if (i<n)
			sz=i+1;
		else
			sz=2*n-i-1;
		v[i].resize(sz);
		for (int j=sz-1;j>=0;j--)
			scanf("%d",&v[i][j]);
	}
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
		{
			a[i+2*n][j+2*n]=v[i+j].back();
			v[i+j].pop_back();
		}
}

bool cmp(int a,int b){
	return a==b || a==10 || b==10;
}

void solve(){
	readdata();
	int ans=(1<<25);
	
	for (int i=0;i<=2*n;i++)
		for (int j=0;j<=2*n;j++)
			for (int sz=0;i+sz<=5*n && j+sz<=5*n;sz++){
				int x2=i+sz;
				int y2=j+sz;
				if (x2<3*n || y2<3*n)
					continue;
				bool q=true;
				for (int i1=i;i1<x2 && q;i1++)
					for (int j1=j;j1<y2 && q;j1++)
						{
							int xt=i1-i,yt=j1-j;
							q&=cmp(a[xt+i][yt+j],a[yt+i][xt+j]);
							q&=cmp(a[xt+i][yt+j],a[sz-yt-1+i][sz-xt-1+j]);
						}
				if (q)
					ans=min(ans,sz*sz-n*n);
			}
	cout<<ans<<endl;
}

int main()
{

  int t;
  cin>>t;
  for (int i=0;i<t;i++)
  {
  	printf("Case #%d: ",i+1);
  	solve();
  }
  return 0;
}