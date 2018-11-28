#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <time.h>
using namespace std;
int main(){
	//double ti=clock();
	//freopen("B-small-attempt0.in","r",stdin); 
	//freopen("outputB_Small.txt","w",stdout);
	freopen("B-large.in","r",stdin); freopen("outputB_Large.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int n,w,l;
		cin>>n>>w>>l;
		vector<pair<int,int> > a(n);
		for(int i=0;i<n;i++){
			cin>>a[i].first;
			a[i].second=i;
		}
		sort(a.begin(),a.end());
		reverse(a.begin(),a.end());
		vector<pair<int,int> > d(n);
	if(w>l){
		int u=0;
		int x=0,y=0;
		for(int i=0;i<n;i++)
			if(w-x>=a[i].first){
				u=max(u,a[i].first);
				d[a[i].second]=make_pair(x,y);
				x+=a[i].first*2;
			}
			else{
				x=0;
				y+=u;
				u=0;
				y+=a[i].first;
				i--;
			}
	}
	else
	{
		int u=0;
		int x=0,y=0;
		for(int i=0;i<n;i++)
			if(l-y>=a[i].first){
				u=max(u,a[i].first);
				d[a[i].second]=make_pair(x,y);
				y+=a[i].first*2;
			}
			else{
				y=0;
				x+=u;
				u=0;
				x+=a[i].first;
				i--;
			}
	}
		//sort(d.begin(),d.end());
		printf("Case #%d:",t+1);
		for(int i=0;i<n;i++)
			printf(" %d %d",d[i].first,d[i].second);
		printf("\n");

	}
	//printf("%lf\n",(clock()-ti)/CLOCKS_PER_SEC);
}