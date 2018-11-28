#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<vector>
using namespace std;
#define see(x) (cerr<<"Line:["<<__LINE__<<"]: "<<#x<<" : "<<x<<"\n")
int vis[1024];
bool cmp(const pair<int,int>&a,const pair<int,int>&b){
	if(a.second!=b.second)return a.second>b.second;
	return a.first>b.first;
}
int main(){
	int T;
	freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&T);
	for(int tt=0;tt<T;tt++){
		int n;
		scanf("%d",&n);
		memset(vis,0,sizeof(vis));
		vector<pair<int,int> >arr;
		for(int i=0;i<n;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			arr.push_back(make_pair(a,b));
		}
		sort(arr.begin(),arr.end(),cmp);
		int tmp=0,cnt=0,a,b;
		for(int k=0;k<=3*n;k++){
			for(int i=0;i<n;i++){
				if(vis[i]==0&&arr[i].second<=tmp){
					tmp+=2;
					vis[i]=2;
					cnt++;
					goto end;
				}
			}
			for(int i=0;i<n;i++){
				if(vis[i]==1&&arr[i].second<=tmp){
					tmp+=1;
					vis[i]=2;
					cnt++;
					goto end;
				}
			}
			for(int i=0;i<n;i++){
				if(vis[i]==0&&arr[i].first<=tmp){
					tmp+=1;
					vis[i]=1;
					cnt++;
					goto end;
				}
			}
			end:
				a=b;
		}
		if(tmp!=2*n)printf("Case #%d: Too Bad\n",tt+1);
		else printf("Case #%d: %d\n",tt+1,cnt);
	}
}
