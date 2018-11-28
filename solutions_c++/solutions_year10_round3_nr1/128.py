#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

#define llong long long 
const double pi = acos(-1.0);
const int maxInt = 0x7fffffff;
const int minInt = ~maxInt;


const int N = 1005;
int a[N],b[N];
int n;

bool yes(int i,int j){
	int tmp = (a[i]-a[j])*(b[i]-b[j]);
	return tmp<0;
}
int main(){
	freopen("A-large.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(i = 0;i<n;i++){
			scanf("%d%d",&a[i],&b[i]);
		}
		int ans = 0;
		for(i = 0;i<n;i++){
			for(j = i+1;j<n;j++){
				if(yes(i,j))ans++;
			}
		}
		printf("Case #%d: %d\n",++nc,ans);
	}
    return 0;
}