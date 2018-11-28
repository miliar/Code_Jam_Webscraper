#include<cstdio>
#include<map>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<algorithm>
#include<limits>
#include<cassert>
#define INT_MAX (numeric_limits<int>::max())
#define see(x) //(cerr<<"Line:["<<__LINE__<<"]:"<<#x<<" = "<<x<<"\n")
using namespace std;
#define EPS 1e-8
vector<pair<int,int> >arr;
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		int D,C;
		arr.clear();
		scanf("%d%d",&D,&C);
		for(int i=0;i<D;i++){
			int P,V;
			scanf("%d%d",&P,&V);
			arr.push_back(make_pair(P,V));
		}
		sort(arr.begin(),arr.end());
		double low=0,high=1e11,mid,ret;
		int st=-1;
		for(int i=0;i<D;i++){
			if(arr[i].second!=0){
				st=i;
				break;
			}
		}
		while(low<high){
			mid=(low+high)/2;
			double L=arr[st].first-mid;
			bool succ=true;
			see(mid);
			for(int i=0;i<D;i++){
				for(int j=0;j<arr[i].second;j++){
					if(arr[i].first-mid>=L){
						L=arr[i].first-mid;
					}else if(arr[i].first+mid<L){
						succ=false;
						break;
					}
					L+=C;
				}
				if(succ==false)break;
			}
			if(succ){
				high=mid-EPS;
				ret=mid;
			}else{
				low=mid+EPS;
			}
		}
		printf("Case #%d: %.7lf\n",cas,ret);
	}
}
