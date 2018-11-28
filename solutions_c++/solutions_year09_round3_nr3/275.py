#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cassert>
#include<climits>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int,int> ii;
typedef pair<int,ii> pii;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
int res,n;
void findSol(vi &arr,int index=0){
	if(index==sz(arr)){
			vb mark(n+1,1);int ans=0;
			for(int i=0;i<sz(arr);i++){
				for(int j=arr[i]-1;j>=1;j--){
					if(mark[j])
						ans++;
					else
						break;
				}
				for(int j=arr[i]+1;j<=n;j++){
					if(mark[j])
						ans++;
					else
						break;
				}
				mark[arr[i]]=0;
			}
			if(res>ans)
				res=ans;
	}
	else{
		for(int i=index;i<sz(arr);i++){
			swap(arr[i],arr[index]);
			findSol(arr,index+1);
			swap(arr[i],arr[index]);
		}
	}
}
int main(){

	int nt;
	cin>>nt;
	for(int g=1;g<=nt;g++){
		int k;
		scanf("%d%d",&n,&k);
		vi arr(k);
		res=INT_MAX;
		for(int i=0;i<k;i++){
			cin>>arr[i];
		}
		findSol(arr);
		printf("Case #%d: %d\n",g,res);
	}
return EXIT_SUCCESS;

}
